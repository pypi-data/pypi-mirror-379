# smeller/services/mqtt_client.py
import paho.mqtt.client as mqtt
from PyQt6.QtCore import QThread, pyqtSignal
import ssl
import os
import time
# Добавляем импорт List из typing
from typing import List, Set


class MqttClient(QThread):

    message_received = pyqtSignal(str, str, str)  # Сигнал: chip_id, topic_suffix, message
    device_connected = pyqtSignal(str) # Добавляем сигнал для передачи наименования подключенного устройства

    def __init__(self, host='mstuca1.ru', port=1883, username=None, password=None, client_id_suffix: str = ""): # Добавлен client_id_suffix
        super().__init__()
        self.host = host
        self.port = port
        self.username = username# or os.environ.get('MQTT_USERNAME')
        self.password = password# or os.environ.get('MQTT_PASSWORD')

        # --- Добавлено хранилище для chip_id ---
        self._discovered_chip_ids: Set[str] = set()
        # --- Конец добавленного ---

        # Генерируем уникальный client_id, если суффикс задан
        client_id = mqtt.base62(os.urandom(6)) + client_id_suffix if client_id_suffix else ""
        self.client = mqtt.Client(client_id=client_id) # Используем сгенерированный ID

        self.is_connected = False
        self.last_message_times = {}

        # Настройка авторизации, если необходимо
        if self.username and self.password:
            self.client.username_pw_set(username=self.username, password=self.password)

        # Настройка SSL/TLS, если необходимо
        # self.client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS)

        # Привязка функций обратного вызова
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

    def run(self):
        # Цикл переподключения остается прежним
        while True:
            if not self.is_connected: # Добавлена проверка, чтобы не пытаться подключиться, если уже подключены
                try:
                    print(f"Attempting to connect to MQTT broker at {self.host}:{self.port}...")
                    self.client.connect(self.host, self.port, 60)
                    self.is_connected = True # Устанавливаем флаг перед входом в loop
                    print("Starting MQTT loop...")
                    self.client.loop_forever() # Блокирующий вызов
                    # loop_forever() выйдет только при вызове disconnect() или ошибке
                    print("MQTT loop finished.")
                    self.is_connected = False # Сбрасываем флаг после выхода из loop
                except ConnectionRefusedError:
                     print(f"Connection refused by MQTT broker at {self.host}:{self.port}. Retrying in 5 seconds...")
                except OSError as e: # Обработка сетевых ошибок
                     print(f"Network error connecting to MQTT broker: {e}. Retrying in 5 seconds...")
                except Exception as e:
                    print(f"Ошибка подключения к MQTT-брокеру: {e}. Retrying in 5 seconds...")

                if self.is_connected: # Если мы были подключены и вышли из loop, сбрасываем флаг
                    self.is_connected = False

            time.sleep(5)  # Пауза перед повторной попыткой подключения (если не подключены)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            # self.is_connected = True # Флаг теперь устанавливается перед loop_forever
            print("Connected with result code " + str(rc))
            # Подписываемся на топики
            client.subscribe("air/+/status")
            client.subscribe("air/+/in")
            client.subscribe("air/+/out")
            print("Subscribed to topics: air/+/status, air/+/in, air/+/out")
        else:
            self.is_connected = False # Убеждаемся, что флаг сброшен при ошибке подключения
            print(f"Ошибка подключения к MQTT-брокеру. Код ошибки: {rc}")

    def on_message(self, client, userdata, msg):
        try: # Добавляем блок try-except для надежности
            topic_parts = msg.topic.split('/')
            if len(topic_parts) >= 3 and topic_parts[0] == 'air':
                chip_id = topic_parts[1]
                topic_suffix = '/'.join(topic_parts[2:])
                message = msg.payload.decode('utf-8', errors='replace') # Добавляем errors='replace'

                # --- Добавляем chip_id в хранилище ---
                self._discovered_chip_ids.add(chip_id)
                # --- Конец добавленного ---

                # Обновляем время последнего сообщения для устройства
                self.last_message_times[chip_id] = time.time()

                # Логирование для отладки
                print(f"Получено сообщение от устройства {chip_id}: topic_suffix='{topic_suffix}', message='{message}'")

                # Испускаем сигнал о получении сообщения
                self.message_received.emit(chip_id, topic_suffix, message)
            else:
                print(f"Получено сообщение с неизвестного топика: {msg.topic}")
        except Exception as e:
             print(f"Error processing MQTT message on topic {msg.topic}: {e}")


    def on_disconnect(self, client, userdata, rc):
        self.is_connected = False
        print(f"Отключен от MQTT-брокера. Код возврата: {rc}")
        # Можно добавить логику автоматического переподключения здесь или положиться на цикл в run()

    def send_message(self, chip_id, message):
        if self.is_connected:
            topic = f"air/{chip_id}/in"
            # Добавляем \n, если его нет, чтобы соответствовать ожидаемому формату на устройстве
            if not message.endswith("\n"):
                message += "\n"
            result, mid = self.client.publish(topic, message) # Publish возвращает кортеж
            if result == mqtt.MQTT_ERR_SUCCESS:
                 print(f"Отправлено сообщение устройству {chip_id} (mid: {mid}): {message.strip()}")
            else:
                 print(f"Ошибка отправки сообщения устройству {chip_id}: {mqtt.error_string(result)}")
        else:
            print("MQTT-клиент не подключен. Сообщение не отправлено.")

    def stop(self):
        print("Stopping MQTT client...")
        if self.client: # Проверка, что клиент существует
            self.client.loop_stop() # Останавливаем фоновый поток Paho (если используется loop_start)
            self.client.disconnect() # Отправляем DISCONNECT брокеру
        self.quit() # Завершаем QThread
        print("MQTT client stopped.")

    # --- Добавлен метод get_discovered_chip_ids ---
    def get_discovered_chip_ids(self) -> List[str]:
        """
        Возвращает список уникальных Chip ID, от которых были получены сообщения.
        """
        # Возвращаем копию списка, чтобы избежать модификации извне
        return list(self._discovered_chip_ids)