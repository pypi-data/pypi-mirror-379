# smeller/dynamic_control/dynamic_block_controller.py

import asyncio
import time
import logging
import math
from typing import Dict, Optional, List, Tuple

from smeller.models.channel_control_config import ChannelControlConfig
from smeller.models.interpolation import InterpolationType
from smeller.controllers.device_controller import DeviceController
from smeller.communication.multi_device_manager import MultiDeviceManager

logger = logging.getLogger(__name__)

class DynamicBlockController:
    def __init__(self, devices_manager: MultiDeviceManager, update_interval: float = 0.1):
        """
        Класс для динамического управления несколькими картриджами ОДНОГО устройства.
        Для каждого картриджа можно задать набор конфигураций каналов (вейпойнтов),
        и команда для каждого канала отправляется только при изменении параметров.
        Реализован механизм паузы/возобновления работы по каждому картриджу отдельно или для всех сразу.
        Args:
            device_controller:  Объект управляющего устройства (должен иметь метод set_channel_parameters).
            update_interval: Интервал обновления (в секундах).
        """
        self.devices_manager = devices_manager  #  ОДИН контроллер устройства
        self.update_interval = update_interval
        self._tasks: Dict[str, asyncio.Task] = {}  # Фоновая задача на каждый КАРТРИДЖ
        self._configs: Dict[str, Dict[int, ChannelControlConfig]] = {}  # cartridge_id -> {channel_id -> config}
        self._start_times: Dict[str, float] = {}   # время старта для каждого картриджа
        self._last_commands: Dict[str, Dict[int, Tuple[int, int]]] = {}  # cartridge_id -> {channel_id: (tick_on, tick_off)}
        self._paused: Dict[str, bool] = {}         # cartridge_id -> True/False
        self._paused_time: Dict[str, float] = {}     # время, когда картридж был поставлен на паузу
        self._is_running: Dict[str, bool] = {}       # флаг работы для каждого картриджа

    async def _run_cartridge(self, cartridge_id: str, total_duration: float) -> None:
        """
        Фоновый цикл для управления конкретным картриджем.
        Рассчитываются текущие параметры для каждого канала и отправляются команды,
        только если они изменились с предыдущего цикла.
        """
        self._is_running[cartridge_id] = True  # Флаг запуска
        try:
            while self._is_running[cartridge_id]:
                if self._paused.get(cartridge_id, False):
                    await asyncio.sleep(self.update_interval)
                    continue

                elapsed_time = time.time() - self._start_times[cartridge_id]
                progress = min(elapsed_time / total_duration, 1.0)

                for channel_id, config in self._configs[cartridge_id].items():
                    try:
                        current_percent = self._calculate_current_percent(config, progress)
                        tick_on, tick_off = self._percent_to_ticks(config.cycle_time, current_percent) # Пока что используем для расчета процентов
                        last_cmd = self._last_commands[cartridge_id].get(channel_id)
                        if last_cmd != (tick_on, tick_off):

                            if cartridge_id == -2: # Управление вентилятором
                                pwm_max, pwm_min, pwm_mode, period = self._percent_to_pwm_fan_config(current_percent) # Функция для преобразования процента в PWM
                                await self.devices_manager.set_fan_config(pwm_max, pwm_min, pwm_mode, period) # Используем set_fan для вентилятора
                                self._last_commands[cartridge_id][channel_id] = (tick_on, tick_off) # Сохраняем tick_on, tick_off для совместимости (можно изменить)
                                logger.debug(f"Fan speed set to PWM: {pwm_max, pwm_min, pwm_mode, period} (percent: {current_percent:.2f}%)")

                            else: # Управление аромаканалами (как и раньше)
                                if tick_on == 0: await self.devices_manager.channel_off(channel_id)
                                else: await self.devices_manager.set_channel_parameters(channel_id, tick_on, tick_off)
                                logger.debug(f"channel_id: {channel_id} #################################################")
                                self._last_commands[cartridge_id][channel_id] = (tick_on, tick_off)

                    except Exception as e:
                        logger.error(f"Cartridge {cartridge_id}, Channel {channel_id}: Error processing command: {e}", exc_info=True)

                if progress >= 1.0:
                    logger.info(f"Cartridge {cartridge_id}: Dynamic block control finished.")
                    self._is_running[cartridge_id] = False
                    break

                await asyncio.sleep(self.update_interval)
        except asyncio.CancelledError:
            logger.info(f"Cartridge {cartridge_id}: Dynamic block control cancelled.")
        except Exception as e:
            logger.error(f"Cartridge {cartridge_id}: Unhandled error: {e}", exc_info=True)
        finally:
            self._is_running[cartridge_id] = False  # Флаг остановки
            logger.info(f"Cartridge {cartridge_id}: Dynamic block control stopped.")
            pwm_max, pwm_min, pwm_mode, period = self._percent_to_pwm_fan_config(0) # Функция для преобразования процента в PWM
            await self.devices_manager.set_fan_config(pwm_max, pwm_min, pwm_mode, period)
            # **Проверка последнего вейпоинта после завершения управления:**
            if cartridge_id != -2: # Пропускаем для вентилятора (если для него не нужно выключение)
                for channel_id, config in self._configs[cartridge_id].items():
                    if config.waypoints:
                        last_waypoint = sorted(config.waypoints, key=lambda wp: wp[0])[-1] # Получаем последний вейпоинт по времени
                        last_intensity = last_waypoint[1]
                        if last_intensity > 0.01: #  Если интенсивность последнего вейпоинта > 0.01% (порог можно настроить)
                            logger.info(f"Cartridge {cartridge_id}, Channel {channel_id}: Last waypoint intensity is {last_intensity}%, sending channel_off command.")
                            await self.devices_manager.channel_off(channel_id)

                        else:
                            logger.info(f"Cartridge {cartridge_id}, Channel {channel_id}: Last waypoint intensity is {last_intensity}%, not sending channel_off command.")
                    else:
                        logger.warning(f"Cartridge {cartridge_id}, Channel {channel_id}: No waypoints, not checking last intensity.")
                        
    def _percent_to_pwm_fan_config(self, percent: float) -> Tuple[int, int, int, int]:
        """
        Преобразует процент интенсивности в значения PWM config для управления вентилятором.
        Возвращает кортеж (pwmMax, pwmMin, pwmMode, period).
        Вам нужно настроить диапазон PWM и другие параметры под ваше оборудование.
        """
        max_pwm_value = 2000  # Максимальное значение PWM (пример, настройте под Arduino и вентилятор)
        pwm_max = int(max_pwm_value * percent / 100)
        pwm_min = pwm_max          # Минимальное значение PWM (пример, можно сделать настраиваемым)
        pwm_mode = 1         # Режим PWM (пример, 0 - режим по умолчанию, проверьте документацию)
        period = 1000        # Период PWM (пример, в микросекундах, проверьте документацию)
        return pwm_max, pwm_min, pwm_mode, period
    
    def _calculate_current_percent(self, config: ChannelControlConfig, progress: float) -> float:
        """Вычисляет текущий процент интенсивности с учетом корректной шкалы."""
        # Преобразуем progress в проценты.
        progress_percent = progress * 100
        
        waypoints = config.waypoints
        interpolation_type = config.interpolation_type

        if not waypoints:
            return 0.0

        if progress_percent <= waypoints[0][0]:
            return 0.0
        if progress_percent >= waypoints[-1][0]:
            return 0.0

        for i in range(len(waypoints) - 1):
            start_waypoint = waypoints[i]
            end_waypoint = waypoints[i + 1]
            if start_waypoint[0] <= progress_percent <= end_waypoint[0]:
                segment_progress = (progress_percent - start_waypoint[0]) / (end_waypoint[0] - start_waypoint[0])
                start_percent = start_waypoint[1]
                end_percent = end_waypoint[1]
                logger.debug("--- DEBUG INTERPOLATION ---")
                logger.debug(f"Progress (in %): {progress_percent:.3f}")
                logger.debug(f"Start Waypoint: {start_waypoint}")
                logger.debug(f"End Waypoint: {end_waypoint}")
                logger.debug(f"Segment Progress: {segment_progress:.3f}")
                logger.debug(f"Interpolation Type: {interpolation_type}")
                calculated_percent = start_percent + (end_percent - start_percent) * segment_progress
            
                if interpolation_type == InterpolationType.LINEAR:
                    return calculated_percent
                elif interpolation_type == InterpolationType.EXPONENTIAL:
                    factor = 2.0
                    return start_percent + (end_percent - start_percent) * (1 - (1 - segment_progress) ** factor)
                elif interpolation_type == InterpolationType.SINUSOIDAL:
                    return start_percent + (end_percent - start_percent) * (0.5 - 0.5 * math.cos(math.pi * segment_progress))
                elif interpolation_type == InterpolationType.STEP:
                    return start_percent
                elif interpolation_type == InterpolationType.FUNCTION and config.interpolation_function:
                    return config.interpolation_function(segment_progress)
                else:
                    return calculated_percent
        return 0.0

    def _percent_to_ticks(self, cycle_time: int, percent: float) -> Tuple[int, int]:
        """
        Преобразует процент «on» в значения tick_on и tick_off.
        (Этот метод не изменился по сравнению с предыдущими версиями.)
        """
        tick_on = int(cycle_time * percent / 100)
        tick_off = cycle_time - tick_on
        return tick_on, tick_off

    def start(self, control_configs: Dict[str, List[ChannelControlConfig]], total_duration: float, start_time_offset: float = 0.0) -> None:
        """
        Запускает динамический блок управления для НЕСКОЛЬКИХ картриджей ОДНОГО устройства.

        Args:
            control_configs: Словарь, где ключ – идентификатор КАРТРИДЖА, а значение – список
                             объектов ChannelControlConfig для этого картриджа.
            total_duration: Общее время работы динамического блока в секундах (одинаковое для всех).
        """
        for cartridge_id, config_list in control_configs.items():
            # Валидируем и сортируем конфигурацию для каждого канала картриджа
            validated_configs: Dict[int, ChannelControlConfig] = {}
            for config in config_list:
                if not config.waypoints:
                    logger.warning(f"Cartridge {cartridge_id}, Channel {config.channel_id}: No waypoints provided, skipping.")
                    continue
                config.waypoints.sort(key=lambda wp: wp[0])
                last_time = -0.0001
                for time_percent, intensity_percent in config.waypoints:
                    logger.debug(f"##@#@#@# {time_percent}, {intensity_percent}")
                    if not 0.0 <= time_percent/100 <= 1.0:
                        raise ValueError(f"Cartridge {cartridge_id}, Channel {config.channel_id}: Waypoint time {time_percent} out of bounds [0, 1].")
                    if not 0.0 <= intensity_percent <= 100.0:
                        raise ValueError(f"Cartridge {cartridge_id}, Channel {config.channel_id}: Intensity {intensity_percent} out of bounds [0, 100].")
                    if time_percent <= last_time:
                        raise ValueError(f"Cartridge {cartridge_id}, Channel {config.channel_id}: Waypoints not in increasing order.")
                    last_time = time_percent
                validated_configs[config.channel_id] = config

            if not validated_configs:
                logger.warning(f"Cartridge {cartridge_id}: No valid channel configurations. Skipping this cartridge.")
                continue

            self._configs[cartridge_id] = validated_configs
            self._last_commands[cartridge_id] = {}  # Инициализируем хранилище последних команд
            self._start_times[cartridge_id] = time.time() - start_time_offset
            self._paused[cartridge_id] = False
            self._is_running[cartridge_id] = True # Устанавливаем флаг

            task = asyncio.create_task(self._run_cartridge(cartridge_id, total_duration))
            self._tasks[cartridge_id] = task
            logger.info(f"Cartridge {cartridge_id}: Dynamic block control started for {total_duration} seconds.")
    
    def pause(self, cartridge_id: Optional[str] = None) -> None:
        """
        Приостанавливает динамический блок управления и выключает каналы (channel_off).
        Если указан cartridge_id – приостанавливается только этот картридж, иначе все.
        """
        
        pwm_max, pwm_min, pwm_mode, period = self._percent_to_pwm_fan_config(0) # Функция для преобразования процента в PWM
        asyncio.create_task(self.devices_manager.set_fan_config(pwm_max, pwm_min, pwm_mode, period))
        if cartridge_id:
            if not self._paused.get(cartridge_id, False):
                self._paused[cartridge_id] = True
                self._paused_time[cartridge_id] = time.time()
                logger.info(f"Cartridge {cartridge_id}: Paused and channels turned off.")
                # Выключаем каналы для данного картриджа (channel_off)
                for channel_id in self._configs[cartridge_id].keys():
                    if cartridge_id != -2:
                        asyncio.create_task(self.devices_manager.channel_off(channel_id)) # Используем channel_off
        else:
            for cid in self._paused.keys():
                if not self._paused[cid]:
                    self._paused[cid] = True
                    self._paused_time[cid] = time.time()
                    logger.info(f"Cartridge {cid}: Paused and channels turned off.")
                    # Выключаем каналы для всех картриджей (channel_off)
                    for channel_id in self._configs[cid].keys():
                        if cartridge_id != -2:
                            asyncio.create_task(self.devices_manager.channel_off(channel_id)) # Используем channel_off

    def resume(self, cartridge_id: Optional[str] = None) -> None:
        """
        Возобновляет выполнение динамического блока управления и восстанавливает
        последние параметры каналов (set_channel_parameters).
        Если указан cartridge_id – возобновляется только этот картридж, иначе все.
        """
        if cartridge_id:
            if self._paused.get(cartridge_id, False):
                paused_duration = time.time() - self._paused_time[cartridge_id]
                self._start_times[cartridge_id] += paused_duration
                self._paused[cartridge_id] = False
                logger.info(f"Cartridge {cartridge_id}: Resumed and restoring last channel parameters.")
                # Восстанавливаем последние параметры для каналов данного картриджа
                for channel_id in self._configs[cartridge_id].keys():
                    last_cmd = self._last_commands[cartridge_id].get(channel_id) # Получаем последние параметры
                    if last_cmd: # Проверяем, есть ли сохраненные параметры
                        tick_on, tick_off = last_cmd
                        if cartridge_id != -2:
                            asyncio.create_task(self.devices_manager.set_channel_parameters(channel_id, tick_on, tick_off)) # Восстанавливаем параметры
                    else:
                        logger.warning(f"Cartridge {cartridge_id}, Channel {channel_id}: No last command found to restore.") # Предупреждение, если нет команды
        else:
            for cid in self._paused.keys():
                if self._paused[cid]:
                    paused_duration = time.time() - self._paused_time[cid]
                    self._start_times[cid] += paused_duration
                    self._paused[cid] = False
                    logger.info(f"Cartridge {cid}: Resumed and restoring last channel parameters.")
                    # Восстанавливаем последние параметры для каналов всех картриджей
                    for channel_id in self._configs[cid].keys():
                        last_cmd = self._last_commands[cid].get(channel_id) # Получаем последние параметры
                        if last_cmd: # Проверяем, есть ли сохраненные параметры
                            tick_on, tick_off = last_cmd
                            if cartridge_id != -2:
                                asyncio.create_task(self.devices_manager.set_channel_parameters(channel_id, tick_on, tick_off)) # Восстанавливаем параметры
                        else:
                            logger.warning(f"Cartridge {cid}, Channel {channel_id}: No last command found to restore.") # Предупреждение, если нет команды

    def stop(self) -> None:
        """
        Останавливает динамический блок для всех картриджей.
        """
        pwm_max, pwm_min, pwm_mode, period = self._percent_to_pwm_fan_config(0) # Функция для преобразования процента в PWM
        asyncio.create_task(self.devices_manager.set_fan_config(pwm_max, pwm_min, pwm_mode, period))
        for cartridge_id, task in self._tasks.items():
            if task and not task.done():  # Проверка, что task существует
                task.cancel()
                logger.info(f"Cartridge {cartridge_id}: Stopping dynamic block control.")
        asyncio.create_task(self.devices_manager.reset_channels()) # Восстанавливаем параметры
        self._tasks.clear()  # Очищаем словарь задач
        # Сбрасываем флаги
        self._is_running.clear()
        
    def is_running(self) -> dict:
        """
        Возвращает True, если динамический блок управления запущен, иначе False.
        """
        return self._is_running

    async def stop_all_tasks(self):
        """Gracefully stops all background tasks (if any)."""
        logger.info("DynamicBlockController: stop_all_tasks called.")
        tasks_to_cancel = list(self._tasks.values())  # Get a list of tasks to avoid dict modification during iteration

        for cartridge_id, task in self._tasks.items():
            if task and not task.done():
                task.cancel()  # Signal cancellation to the task
                logger.debug(f"Cartridge {cartridge_id}: Cancellation signaled.")

        if tasks_to_cancel:
            logger.debug("Awaiting task cancellation...")
            results = await asyncio.gather(*tasks_to_cancel, return_exceptions=True) # Wait for all tasks to cancel

            for cartridge_id, result in zip(self._tasks.keys(), results):
                if isinstance(result, asyncio.CancelledError):
                    logger.info(f"Cartridge {cartridge_id}: Task cancelled successfully.")
                elif isinstance(result, Exception):
                    logger.error(f"Cartridge {cartridge_id}: Task finished with exception: {result}", exc_info=result)
                else:
                    logger.info(f"Cartridge {cartridge_id}: Task finished normally.") # Should not happen after cancel

        asyncio.create_task(self.devices_manager.reset_channels()) # Reset channels after stopping tasks
        self._tasks.clear()  # Clear task dictionary
        self._is_running.clear() # Clear running flags
        logger.info("DynamicBlockController: All dynamic control tasks stopped.")