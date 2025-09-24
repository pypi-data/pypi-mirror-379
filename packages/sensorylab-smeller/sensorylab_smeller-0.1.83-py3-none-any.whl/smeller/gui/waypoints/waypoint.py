"""
Файл: # smeller/gui/waypoint.py
Описание: Модуль для отображения вейпоинтов и интерполяционных линий для нескольких каналов.
Обеспечивает как интерактивные (активного порта) точки, так и неинтерактивные для остальных.
"""

import sys
import numpy as np
import pyqtgraph as pg

from pathlib import Path
project_root = Path(__file__).resolve().parents[2]  # Поднимаемся на два уровня вверх
sys.path.append(str(project_root))


import pyqtgraph as pg
from PyQt6.QtCore import Qt, QTime, pyqtSignal, QPoint, QPointF, QPropertyAnimation, QRectF, QEasingCurve, QTimer, pyqtProperty
from PyQt6.QtGui import QPixmap, QCursor, QColor, QGradient, QLinearGradient, QPen, QBrush, QRadialGradient, QCursor
from PyQt6.QtWidgets import QLabel, QGraphicsItem, QGraphicsDropShadowEffect, QToolTip, QVBoxLayout, QHBoxLayout, QFrame
from smeller.dynamic_control.view_model import MainWindowViewModel # Import ViewModel
from smeller.config.constants import *
from smeller.dynamic_control.dynamic_block_controller import DynamicBlockController
from smeller.models.channel_control_config import ChannelControlConfig
from smeller.models.interpolation import InterpolationType
from typing import Dict, Optional, List, Callable, Union, Tuple
import logging

# Глобально включаем сглаживание (антиалиасинг) для более высокой визуальной четкости
pg.setConfigOptions(antialias=True, background='w')



logger = logging.getLogger(__name__)

class CustomToolTip(QFrame):
    def __init__(self, pixmap: QPixmap, text: str, parent=None, theme="light"):
        """
        Инициализирует кастомный тултип с эффектом glassmorphism, неоновой окантовкой и округлёнными углами.
        Аргументы:
            pixmap (QPixmap): изображение (например, кадр из видео) для отображения слева.
            text (str): текстовое содержимое тултипа.
            parent: родительский виджет (обычно основной виджет сцены).
            theme (str): тема ("light" или "dark"); здесь можно настроить изменения внешнего вида.
        """
        super().__init__(parent, Qt.WindowType.ToolTip)
        self.setWindowFlags(Qt.WindowType.ToolTip | Qt.WindowType.FramelessWindowHint)
        # Делаем фон окна полностью прозрачным (позволяет видеть полупрозрачный стиль, заданный в setStyleSheet)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        # Позволяет применять стили фоном по вызову setStyleSheet
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)  # Гарантированное уничтожение при закрытии
        
        self._current_theme = theme
        self._setup_ui(pixmap, text)

    def _setup_ui(self, pixmap: QPixmap, text: str):
        # Применяем стиль glassmorphism: полупрозрачный фон, неоновая окантовка и скруглённые углы
        self._apply_glassmorphism_style()
        # Создаем основной горизонтальный layout с отступами и интервалом между элементами
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        # Если изображение передано (и оно не пустое), добавляем его слева
        if pixmap and not pixmap.isNull():
            imageLabel = QLabel()
            imageLabel.setPixmap(pixmap.scaledToWidth(100, Qt.TransformationMode.SmoothTransformation))
            layout.addWidget(imageLabel)
        # Справа создаем вертикальный layout для текстового блока
        textLayout = QVBoxLayout()
        textLabel = QLabel(text)
        textLabel.setWordWrap(True)
        textLabel.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        textLayout.addWidget(textLabel)
        layout.addLayout(textLayout)
        self.adjustSize()
        self._set_neon_shadow()

    def _apply_glassmorphism_style(self):
        # Здесь мы задаем прозрачный фон, неоновую окантовку и скругляем углы
        # Обратите внимание: Qt не поддерживает backdrop-filter, поэтому блюр заднего фона здесь не производится
        style = """
        QFrame {
            background: rgba(255, 255, 255, 0.45);  /* полупрозрачный белый фон */
            border: 2px solid rgba(0,195,255,0.8);   /* неоновая окантовка (цвет – голубой) */
            border-radius: 15px;                     /* округлённые углы */
        }
        QLabel {
            color: #ffffff;
            font-size: 10pt;
        }
        """
        self.setStyleSheet(style)
        # Делает фон виджета прозрачным (по возможности – чтобы видеть эффект стекла)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

    def _set_neon_shadow(self):
        # Добавляем drop-shadow эффект, который создаёт неоновое свечение вокруг тултипа
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setColor(Qt.GlobalColor.cyan)  # neon-цвет (можно менять на другой при необходимости)
        shadow.setOffset(0)
        self.setGraphicsEffect(shadow)

    def set_theme(self, theme: str):
        # Метод для смены темы уже открытого тултипа (если требуется динамически менять стиль)
        self._current_theme = theme.lower() if theme else "light"
        self._apply_glassmorphism_style()
        
    
class WaypointItem(pg.GraphicsObject):
    size = pyqtProperty(float, fget=lambda self: self.getSize(), fset=lambda self, value: self.setSize(value))

    def __init__(self, x, y, channel: int = None, base_size=10, hover_size=25,
                 normal_color: QColor | dict = None,
                 hover_color: QColor | dict = None,
                 cartridge_id: str = None,
                 cartridge_name: str = None,
                 theme: str = 'dark'):
        """
        При создании точки передаются дополнительные параметры для идентификации картриджа.
        """
        super().__init__()
        self.theme = theme
        self.channel = channel
        self.cartridge_id = cartridge_id
        self.cartridge_name = cartridge_name
        self.base_size = base_size
        self.hover_size = hover_size
        self._current_size = base_size
        self._animation = QPropertyAnimation(self, b"size")
        self._animation.setDuration(150)
        self._animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        self.normal_color = normal_color if normal_color is not None else QColor(0, 255, 255)
        self.hover_color = hover_color if hover_color is not None else QColor(0, 150, 255)
        self.neon_border_color = QColor(0, 195, 255)
        self._hovered = False
        self._selected = False
        self._tooltip_active = False  # Флаг, показывающий, активен ли тултип
        
        self.setPos(x, y)
        self.setAcceptHoverEvents(True)
        # Флаг, чтобы размер не менялся при зуме
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIgnoresTransformations, True)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(self.neon_border_color)
        shadow.setOffset(0)
        self.setGraphicsEffect(shadow)

    def boundingRect(self):
        r = self._current_size / 2.0
        return QRectF(-r, -r, self._current_size, self._current_size)

    def paint(self, painter, option, widget):
        # Определяем параметры градиента для заполнения круга
        rect = self.boundingRect()
        center = rect.center()
        radius = rect.width() / 2.0

        if self._hovered:
            hover_color = self.hover_color
            if isinstance(hover_color, dict):
                hover_color = QColor(hover_color['r'], hover_color['g'], hover_color['b'], hover_color['a'])
            # Для hovered-режима создаём яркий радиальный градиент
            gradient = QRadialGradient(center, radius)
            # Центр – более яркий оттенок, края – немного затемнены с эффектом прозрачности
            gradient.setColorAt(0, self.hover_color.lighter(120))
            gradient.setColorAt(1, self.hover_color.darker(150))
            base_width = 2
            pen_color = self.neon_border_color

        else:
            normal_color = self.normal_color
            if isinstance(normal_color, dict):
                normal_color = QColor(normal_color['r'], normal_color['g'], normal_color['b'], normal_color['a'])
            # Для обычного режима используем более мягкий градиент
            gradient = QRadialGradient(center, radius)
            gradient.setColorAt(0, normal_color.lighter(120))
            gradient.setColorAt(1, normal_color.darker(150))
            base_width = 1
            pen_color = QColor(128, 128, 128, 128)

        if self._selected:
            base_width += 4
            pen_color = QColor(128, 128, 255, 255)

        pen = QPen(pen_color, base_width)
        painter.setPen(pen)
        painter.setBrush(QBrush(gradient))
        painter.drawEllipse(rect)

    def capture_video_frame(self, time_secs: int) -> QPixmap | None:
        """
        Здесь вы должны реализовать логику захвата кадра из загруженного видео по указанному времени.
        Например, если ваш MediaView предоставляет метод capture_frame(time_secs) -> QPixmap,
        вы можете вызвать его здесь. В этом примере функция возвращает None, чтобы показать,
        что если кадр не получен, то картинка не отображается.
        """
        # Пример:
        # from smeller.gui.media_view import MediaViewInstance
        # pixmap = MediaViewInstance.capture_frame(time_secs)
        # return pixmap if pixmap and not pixmap.isNull() else None

        # Реализация по умолчанию – возвращает None (нет изображения)
        return None


    def mouseMoveEvent(self, event):
        if self._hovered:
            self.close_tooltip
        
        super().mouseMoveEvent(event)
    def hoverEnterEvent(self, event):
        if self._tooltip_active:
            return  # Если тултип уже активен, ничего не делаем
        self.setGraphicsEffect(None)

        self._hovered = True
        self._animation.stop()
        self._animation.setStartValue(self._current_size)
        self._animation.setEndValue(self.hover_size)
        self._animation.start()

        # Формирование всплывающей подсказки с информацией о точке:
        current_intensity = self.pos().y()
        current_time_secs = int(round(self.pos().x()))
        time_str = QTime(0, 0, 0).addSecs(current_time_secs).toString("hh:mm:ss")
        tooltip_text = (
            f"ID: {self.cartridge_id if self.cartridge_id else (str(self.channel+1) if self.channel is not None else 'N/A')}\n"
            f"Name: {self.cartridge_name if self.cartridge_name else 'unknown'}\n"
            f"Intensity: {current_intensity:.2f}%\n"
            f"Time: {time_str}"
        )
        # Пытаемся получить изображение из видео для заданного временного кадра
        pixmap = self.capture_video_frame(current_time_secs)

        # Создаем экземпляр кастомного тултипа с изображением (если получено) и текстом
        # Родительским виджетом передаем основной виджет сцены, чтобы тултип отображался поверх
        #self._custom_tooltip = CustomToolTip(pixmap, tooltip_text, parent=self.scene().views()[0], theme=self.theme) 
        # Располагаем тултип рядом с текущей позицией курсора с небольшим смещением
        #self._custom_tooltip.move(QCursor.pos() + QPoint(10, 10))
        #self._custom_tooltip.show()
        #QTimer.singleShot(3000, self.close_tooltip)  # Закрываем через 5 секунд

        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self._hovered = False
        self._animation.stop()
        self._animation.setStartValue(self._current_size)
        self._animation.setEndValue(self.base_size)
        self._animation.start()
        # Закрываем кастомный тултип, если он существует
        #if hasattr(self, "_custom_tooltip") and self._custom_tooltip:
        #    self._custom_tooltip.close()
        #    self._custom_tooltip = None
        self._tooltip_active = False  # Сбрасываем флаг
        
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(self.neon_border_color)
        shadow.setOffset(0)
        self.setGraphicsEffect(shadow)
        super().hoverLeaveEvent(event)
    
    def close_tooltip(self):
        """Закрывает тултип и сбрасывает флаг."""
        if hasattr(self, '_custom_tooltip') and self._custom_tooltip:
            self._custom_tooltip.close()  # Это вызовет deleteLater() благодаря WA_DeleteOnClose
            self._custom_tooltip = None
        self._tooltip_active = False  # Сбрасываем флаг
        
    def getSize(self):
        return self._current_size

    def setSelected(self, selected: bool):
        """
        Устанавливает состояние выделения элемента.
        """
        self._selected = selected
        self.update()
        
    def isSelected(self) -> bool:
        return self._selected
    
    def setSelected(self, selected: bool):
        """
        Устанавливает состояние выделения элемента.
        """
        self._selected = selected
        self.update()
        
    def isSelected(self) -> bool:
        return self._selected
      
    def setSize(self, value):
        self._current_size = value
        self.prepareGeometryChange()
        self.update()

    def delete(self):
        """
        Переопределение метода удаления, чтобы тултип тоже закрывался при удалении точки
        """
        self.close_tooltip()

        
class StaticWaypointItem(WaypointItem):
    """
    Неинтерактивный (статичный) элемент вейпоинта.
    
    Используется для отображения точек каналов, которые не являются активными.
    Переопределяет обработчики событий для отключения интерактивности.
    """
    def __init__(self, x, y, channel: int = None, base_size=10, normal_color: QColor | dict = None):
        # Используем одинаковый размер для базового и hover-состояний, чтобы не было анимации
        normal_color_qcolor = normal_color
        if isinstance(normal_color, dict):
            normal_color_qcolor = QColor(normal_color['r'], normal_color['g'], normal_color['b'], normal_color['a'])
        super().__init__(x, y, channel=channel, base_size=base_size, hover_size=base_size,
                         normal_color=normal_color_qcolor, hover_color=normal_color)
        self.setAcceptHoverEvents(False)
    
    def hoverEnterEvent(self, event):
        event.ignore()
    
    def hoverLeaveEvent(self, event):
        event.ignore()
    
    def mousePressEvent(self, event):
        event.ignore()


class PlotWidget(pg.PlotWidget):
  """
  Виджет для отображения и управления вейпоинтами и интерполяционными линиями для нескольких каналов.
  
  Поддерживает:
    – Отображение вейпоинтов для каждого канала (хранятся в словаре channel_waypoints)
    – Отображение интерполяционной линии для каждого канала (словарь lines).
    – Активный канал (active_channel) отображается интерактивно (можно перемещать, добавлять и удалять точки),
      а его линия показывается сплошным стилем; линии других каналов – неинтерактивны и рисуются штриховыми.
  
  Сигналы:
    waypoint_moved(channel: int, waypoint_index: int, new_time_percent: float, new_intensity: float)
    waypoint_added(channel: int, time_percent: float, intensity: float)
    waypoint_deleted(channel: int, waypoint_index: int)
    interpolation_type_changed(str)
  """

  waypoint_moved = pyqtSignal(int, int, float, float) # (channel_idx, waypoint_idx, new_time_percent, new_intensity)
  """Signal emitted when a waypoint is moved. Args: (channel_index, waypoint_index, new_time_percent, new_intensity)"""
  waypoint_added = pyqtSignal(int, float, float)    # (channel_idx, time_percent, intensity)
  """Signal emitted when a waypoint is added. Args: (channel_index, time_percent, intensity)"""
  waypoint_deleted = pyqtSignal(int, int)        # (channel_idx, waypoint_idx)
  """Signal emitted when a waypoint is deleted. Args: (channel_index, waypoint_index)"""
  interpolation_type_changed = pyqtSignal(str)     # Signal об изменении типа интерполяции
  """Signal emitted when the interpolation type is changed. Args: (interpolation_type)"""


  def __init__(self, active_channel: int = 0, view_model: MainWindowViewModel = None, time_offset: float = 0, *args, **kwargs):
    """
    Инициализирует виджет для отображения вейпоинтов нескольких каналов.
    
    Аргументы:
      active_channel (int): Номер канала, который будет активным (интерактивным).
      view_model: Ссылка на модель представления (если требуется).
      time_offset (float): Смещение по времени (в секундах).
    """
    super().__init__(*args, **kwargs)
    # Отключаем стандартное контекстное меню при правом клике
    self.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
    self.getPlotItem().vb.setMenuEnabled(False)
        
    # Словари для хранения вейпоинтов и линий для каждого канала
    self.channel_waypoints = {}  # key: номер канала, value: список объектов точек
    self.lines = {}  # key: номер канала, value: объект PlotDataItem для линии
    self.active_channel = active_channel
    
    # Определяем цвета каналов (если не заданы – используем дефолтную палитру)
    self.channel_colors = {}
    self.default_colors = [
        QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255),
        QColor(255, 255, 0), QColor(255, 165, 0), QColor(128, 0, 128),
        QColor(0, 255, 255), QColor(255, 192, 203), QColor(0, 128, 128),
        QColor(128, 128, 0), QColor(0, 0, 0), QColor(128, 128, 128)
    ]
    if self.active_channel not in self.channel_colors:
        self.channel_colors[self.active_channel] = self.default_colors[self.active_channel % len(self.default_colors)]
    
    self.time_offset = time_offset
    self.total_duration = 0.0  # Начальное значение продолжительности (сек)
    self._needs_update = False
    
    self.current_time_marker = pg.InfiniteLine(
                                                pos=0,                      # начальная позиция на оси X (или Y, если horizontal)
                                                angle=90,                   # вертикальная линия
                                                pen=pg.mkPen(color=(255, 0, 0), width=1),  # здесь width=3 задаёт толщину линии
                                                movable=False,              # линия не перетаскивается мышью
                                                label=""         # метка, которая отобразится рядом (необязательно)
    )
    self.addItem(self.current_time_marker)
    self.current_time_marker.setPos(0)
    
    # Настройка внешнего вида осей
    self.getPlotItem().setLabel('left', 'Intensity', units='%')
    self.getPlotItem().hideAxis('bottom')
    self.getPlotItem().setXRange(0, self.total_duration)
    self.getPlotItem().setYRange(0, 100)
    self.getPlotItem().disableAutoRange(axis='y')
    self.setMouseEnabled(x=True, y=False)
    
    self.time_label_pool = []  # Пул для объектов TextItem
    self.max_time_labels = 15  # Максимальное количество видимых меток (примерное)
    self._init_time_label_pool()

    self.getPlotItem().vb.sigRangeChanged.connect(self.update_grid_lines)
    
    # Линии сетки и метки времени
    self.vertical_grid_lines = []
    self.time_labels = []
    
    self.set_theme('dark')
    self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
    
    # Вспомогательные переменные для обработки событий мыши
    self._dragging_waypoint_index = None
    self._press_pos = None
    self._is_pressed = False
    self._is_dragging = False

    # Ссылка на ViewModel для доступа к конфигурации канала
    self.view_model = view_model
    
  def _init_time_label_pool(self):
      """Инициализирует пул объектов TextItem."""
      for _ in range(self.max_time_labels):
          label = pg.TextItem(color=(200, 200, 200), anchor=(0.5, 1))
          label.setVisible(False)  # Скрываем метки при создании
          self.time_label_pool.append(label)
          self.getPlotItem().addItem(label) # Сразу добавляем на график, но делаем невидимыми
  
  def set_active_channel(self, channel: int):
      """
      Устанавливает активный канал и обновляет отображение вейпоинтов.
      
      Аргументы:
        channel (int): номер канала, который станет активным (интерактивным).
      """
      self.active_channel = channel
      if channel not in self.channel_colors:
          self.channel_colors[channel] = self.default_colors[channel % len(self.default_colors)]
      self.refresh_waypoints()
      self.update_plot()
      
          
  def refresh_waypoints(self):
      """
      Пересоздает объекты вейпоинтов для всех каналов с учётом того, какой канал активен.
      Для активного канала создаются интерактивные точки, для остальных – статичные.
      """
      for channel, items in list(self.channel_waypoints.items()):
          waypoints_data = [(item.pos().x(), item.pos().y()) for item in items]
          for item in items:
              self.removeItem(item)
          new_items = []
          for x, y in waypoints_data:
              if channel == self.active_channel:
                  config = self.view_model.channel_configs.get(channel) if self.view_model else None
                  wp = WaypointItem(x, y, channel=channel, base_size=10, hover_size=20,
                                    normal_color=self.channel_colors.get(channel, QColor(100,170,190)),
                                    hover_color=QColor(0, 0, 255),
                                    cartridge_id=config.cartridge_id if config and config.cartridge_id else str(channel+1), #XЧТО ТО ПОТЕНЦИАЛЬНО ОПАСНОЕ
                                    cartridge_name=config.cartridge_name if config and config.cartridge_name else "unknown")
              else:
                  wp = StaticWaypointItem(x, y, channel=channel, base_size=10,
                                          normal_color=self.channel_colors.get(channel, QColor(100,170,190)))
              self.addItem(wp)
              new_items.append(wp)
          self.channel_waypoints[channel] = new_items
      
      
                
  def set_channel_color(self, channel: int, color: QColor):
      # Если выбранный цвет из набора стандартных, проверяем уникальность
      if any(color == default_color for default_color in self.default_colors):
          # Собираем кортежи RGB всех дефолтных цветов, уже назначенных другим каналам
          used_default_colors = {
              col.getRgb() for ch, col in self.channel_colors.items()
              if ch != channel and any(col == dc for dc in self.default_colors)
          }
          # Если переданный цвет уже используется – выбираем первый цвет из дефолтного набора, которого ещё нет
          if color.getRgb() in used_default_colors:
              for default_color in self.default_colors:
                  if default_color.getRgb() not in used_default_colors:
                      color = default_color
                      break
      self.channel_colors[channel] = color
      self._needs_update = True
      self.update_plot()
      q_color = color if isinstance(color, QColor) else QColor(color['r'], color['g'], color['b'], color['a'])
      logger.debug(f"WaypointPlotWidget: цвет канала установлен в: {q_color.getRgb()}")
      
  def set_interpolation_type(self, interp_type: str):
    """
    Sets the interpolation type and redraws the plot.

    Args:
      interp_type (str): The interpolation type to set (from InterpolationType enum).
    """
    self.current_interpolation_type = interp_type
    self._needs_update = True

  def set_total_duration(self, duration: float):
        """
        Устанавливает общую продолжительность для динамического контроля.
        Обновляет диапазон оси X, пересчитывает ограничения и обновляет график.

        Аргументы:
            duration (float): Новая общая продолжительность в секундах.
        """
        old_duration = self.total_duration  # Сохраняем старую продолжительность
        self.total_duration = duration
        self.getPlotItem().setXRange(0, self.total_duration)
        self._update_x_limits()

        if old_duration > 0 and duration > 0: # Избегаем деления на ноль и пересчитываем только если есть старая и новая продолжительность
            channel_waypoints = self.channel_waypoints.get(self.active_channel, [])
            for wp in channel_waypoints:
                # Рассчитываем процент времени от старой продолжительности
                time_percent = wp.pos().x() / old_duration * 100
                # Вычисляем новую X-позицию, основываясь на проценте и новой продолжительности
                new_x = duration * time_percent / 100
                wp.setPos(new_x, wp.pos().y()) # Устанавливаем новую позицию

        self._needs_update = True
        self.update_plot()

  def _update_x_limits(self):
      """
      Обновляет ограничения по оси X (а также Y, если необходимо) в ViewBox графика.
      Устанавливает лимиты таким образом, чтобы ось X не выходила за пределы интервала [0, total_duration].
      """
      vb = self.getPlotItem().vb
      vb.setLimits(xMin=0, xMax=self.total_duration + 0.9, yMin=-9, yMax=109)

  def set_waypoints(self, channel: int, waypoints: list):
      """
      Устанавливает вейпоинты для указанного канала.
      
      Аргументы:
        channel (int): номер канала.
        waypoints (list): список кортежей (time_percent, intensity).
      """
      if channel in self.channel_waypoints:
          for item in self.channel_waypoints[channel]:
              self.removeItem(item)
      self.channel_waypoints[channel] = []
      for time_percent, intensity in waypoints:
          x = time_percent / 100 * self.total_duration
          y = intensity
          if channel == self.active_channel:
              config = self.view_model.channel_configs.get(channel) if self.view_model else None
              wp = WaypointItem(x, y, channel=channel, base_size=10, hover_size=20,
                                normal_color=self.channel_colors.get(channel, QColor(100,170,190)),
                                hover_color=QColor(0, 0, 255),
                                cartridge_id=config.cartridge_id if config and config.cartridge_id else str(channel+1), #И ТУТ
                                cartridge_name=config.cartridge_name if config and config.cartridge_name else "unknown")
          else:
              wp = StaticWaypointItem(x, y, channel=channel, base_size=10,
                                      normal_color=self.channel_colors.get(channel, QColor(100,170,190)))
          self.addItem(wp)
          self.channel_waypoints[channel].append(wp)
      self._needs_update = True
      self.update_plot()
    

  def get_waypoints(self, channel: int) -> list:
      """
      Возвращает список вейпоинтов для указанного канала в формате [(time_percent, intensity), ...].
      """
      waypoints = []
      if channel not in self.channel_waypoints:
          return waypoints
      for wp in self.channel_waypoints[channel]:
          pos = wp.pos()
          waypoints.append((pos.x() / self.total_duration * 100, pos.y()))
      waypoints.sort(key=lambda wp: wp[0])
      return waypoints

  def add_waypoint(self, x: float, y: float, emit_signal: bool = True):
      """
      Добавляет вейпоинт в активном канале.
      
      Аргументы:
        x (float): координата X (в секундах).
        y (float): координата Y (в процентах интенсивности).
        emit_signal (bool): флаг для отправки сигнала waypoint_added.
      """
      x = round(x)
      if not 0 <= y <= 100 or not 0 <= x <= self.total_duration:
          return
      config = self.view_model.channel_configs.get(self.active_channel) if self.view_model else None
      
      wp = WaypointItem(x, y, channel=self.active_channel, base_size=15, hover_size=20,
                        normal_color=self.channel_colors.get(self.active_channel, QColor(255,0,0)),
                        hover_color=QColor(0, 0, 255),
                        cartridge_id=config.cartridge_id if config and config.cartridge_id else str(self.active_channel+1), #ИТУТ
                        cartridge_name=config.cartridge_name if config and config.cartridge_name else "unknown")
      self.addItem(wp)
      if self.active_channel not in self.channel_waypoints:
          self.channel_waypoints[self.active_channel] = []
      self.channel_waypoints[self.active_channel].append(wp)
      self.channel_waypoints[self.active_channel].sort(key=lambda wp: wp.pos().x())
      if emit_signal:
          self.waypoint_added.emit(self.active_channel, x / self.total_duration * 100, y)
      self._needs_update = True
      self.update_plot()
    

  def clear_waypoints(self, channel: int = None):
      """
      Удаляет все вейпоинты для указанного канала.
      Если channel не указан, очищает активный канал.
      """
      if channel is None:
          channel = self.active_channel
      if channel in self.channel_waypoints:
          for item in self.channel_waypoints[channel]:
              self.removeItem(item)
          self.channel_waypoints[channel] = []
          if channel in self.lines and self.lines[channel] is not None:
              self.removeItem(self.lines[channel])
              self.lines[channel] = None
          self._needs_update = True
          self.update_plot()

  def update_plot(self):
      """
      Перерисовывает интерполяционные линии для всех каналов на основе текущих вейпоинтов.
      Для активного канала линия сплошная, для остальных – штриховая.
      """
      if not self._needs_update:
          return
      for channel, items in self.channel_waypoints.items():
          if len(items) < 2:
              if channel in self.lines and self.lines[channel] is not None:
                  self.lines[channel].setData([], [])
              continue
          
          sorted_items = sorted(items, key=lambda wp: wp.scenePos().x())
          x_coords = []
          y_coords = []
          
          interp_type = "linear"  # значение по умолчанию
          if self.view_model and channel in self.view_model.channel_configs:
              interp_type = self.view_model.channel_configs[channel].interpolation_type
              
          for i in range(len(sorted_items) - 1):
              start_x = sorted_items[i].pos().x()
              start_y = sorted_items[i].pos().y()
              end_x = sorted_items[i+1].pos().x()
              end_y = sorted_items[i+1].pos().y()
              if start_x == end_x:
                  continue
              segment_x = np.linspace(start_x, end_x, INTERPOLATION_POINTS)
              progress = (segment_x - start_x) / (end_x - start_x)
              segment_y = self._interpolate_y(start_y, end_y, progress, interp_type)
              x_coords.extend(segment_x)
              y_coords.extend(segment_y)
          x_coords.append(sorted_items[-1].pos().x())
          y_coords.append(sorted_items[-1].pos().y())
          
          if channel not in self.lines or self.lines[channel] is None:
              pen_style = Qt.PenStyle.SolidLine if channel == self.active_channel else Qt.PenStyle.DashLine
              size = 2 if channel == self.active_channel else 1
              channel_color = self.channel_colors.get(channel, QColor(100,170,190))
              if isinstance(channel_color, dict):
                channel_color = QColor(channel_color['r'], channel_color['g'], channel_color['b'], channel_color['a'])

              pen = pg.mkPen(channel_color, width=size, style=pen_style)
              line_item = pg.PlotDataItem(pen=pen)
              line_item.setZValue(-1)
              self.addItem(line_item)
              self.lines[channel] = line_item
          else:
              line_item = self.lines[channel]
              pen_style = Qt.PenStyle.SolidLine if channel == self.active_channel else Qt.PenStyle.DashLine
              size = 2 if channel == self.active_channel else 1
              channel_color = self.channel_colors.get(channel, QColor(100,170,190))
              if isinstance(channel_color, dict):
                channel_color = QColor(channel_color['r'], channel_color['g'], channel_color['b'], channel_color['a'])
              pen = pg.mkPen(channel_color, width=size, style=pen_style)
              line_item.setPen(pen)
          
          line_item.setData(x=np.array(x_coords), y=np.array(y_coords))
      self._needs_update = False
      
  def _interpolate_y(self, start_y: float, end_y: float, progress: np.ndarray, interp_type: str) -> np.ndarray:
    """
    Calculates Y values for interpolation based on the interpolation type.

    Args:
      start_y (float): Starting Y value.
      end_y (float): Ending Y value.
      progress (np.ndarray): Progress array (normalized time from 0 to 1).
      interp_type (str): Interpolation type (from InterpolationType enum).

    Returns:
      np.ndarray: Array of interpolated Y values.
    """
    if interp_type == LINEAR:
        return start_y + (end_y - start_y) * progress
    elif interp_type == EXPONENTIAL:
        factor = 2.0
        return start_y + (end_y - start_y) * (1 - (1 - progress) ** factor)
    elif interp_type == SINUSOIDAL:
        return start_y + (end_y - start_y) * (0.5 - 0.5 * np.cos(np.pi * progress))
    elif interp_type == STEP:
        return np.where(progress <= 1, start_y, end_y)
    else:
        return start_y + (end_y - start_y) * progress


  def find_closest_waypoint(self, x: float, y: float, waypoints: Optional[list] = None) -> Optional[int]:
      """
      Находит индекс ближайшей точки (вейпоинта) в списке waypoints к заданным координатам.
      Если waypoints не передан, ищем в активном канале.
      """
      if waypoints is None:
          waypoints = self.channel_waypoints.get(self.active_channel, [])
      if not waypoints:
          return None
      min_distance = float('inf')
      closest_index = None
      for index, wp in enumerate(waypoints):
          pos = wp.pos()
          distance = abs(pos.x() - x) + abs(pos.y() - y)
          if distance < min_distance:
              min_distance = distance
              closest_index = index
      return closest_index


  def mousePressEvent(self, event):
      if event.button() == Qt.MouseButton.LeftButton:
          pos = self.getPlotItem().vb.mapSceneToView(event.position())
          self.last_clicked_pos = pos
          self._press_pos = pos
          self._is_pressed = True
          self._is_dragging = False
          # Ищем ближайший интерактивный вейпоинт только для активного канала
          candidate_items = self.channel_waypoints.get(self.active_channel, [])
          min_distance = float('inf')
          candidate_index = None
          for i, wp in enumerate(candidate_items):
              wp_pos = wp.pos()
              distance = abs(wp_pos.x() - pos.x()) + abs(wp_pos.y() - pos.y())
              if distance < min_distance:
                  min_distance = distance
                  candidate_index = i
          DRAG_THRESHOLD = 10
          for wp in candidate_items:
              wp.setSelected(False)
        
          
          if candidate_index is not None and min_distance < DRAG_THRESHOLD:
              self._dragging_waypoint_index = candidate_index
              candidate_items[candidate_index].setSelected(True)
          else:
              self._dragging_waypoint_index = None
          event.accept()
      elif event.button() == Qt.MouseButton.RightButton:
          pos = event.position()
          if self.getPlotItem().sceneBoundingRect().contains(pos):
              mouse_point = self.getPlotItem().vb.mapSceneToView(pos)
              x, y = mouse_point.x(), mouse_point.y()
              candidate_items = self.channel_waypoints.get(self.active_channel, [])
              closest_index = None
              min_distance = float('inf')
              for i, wp in enumerate(candidate_items):
                  distance = abs(wp.pos().x() - x) + abs(wp.pos().y() - y)
                  if distance < min_distance:
                      min_distance = distance
                      closest_index = i
              if closest_index is not None:
                  wp_to_remove = candidate_items.pop(closest_index)
                  
                  wp_to_remove.delete()
                  self.removeItem(wp_to_remove)
                  self._needs_update = True
                  self.waypoint_deleted.emit(self.active_channel, closest_index)
                  self.update_plot()
          event.accept()
      super().mousePressEvent(event)
  
  def mouseMoveEvent(self, event):
      if event.buttons() & Qt.MouseButton.LeftButton and self._is_pressed:
          new_pos = self.getPlotItem().vb.mapSceneToView(event.position())
          dx = abs(new_pos.x() - self._press_pos.x())
          dy = abs(new_pos.y() - self._press_pos.y())
          DRAG_THRESHOLD = 3
          if not self._is_dragging and (dx + dy) >= DRAG_THRESHOLD and self._dragging_waypoint_index is not None:
              self._is_dragging = True
          if self._is_dragging and self._dragging_waypoint_index is not None:
              new_x = round(max(0, min(new_pos.x(), self.total_duration)))
              new_y = max(0, min(new_pos.y(), 100))
              wp = self.channel_waypoints[self.active_channel][self._dragging_waypoint_index]
              wp.setPos(new_x, new_y)
              self._needs_update = True
              self.update_plot()
          event.accept()
      else:
          super().mouseMoveEvent(event)
  
  def mouseReleaseEvent(self, event):
      if event.button() == Qt.MouseButton.LeftButton and self._is_pressed:
          if self._is_dragging and self._dragging_waypoint_index is not None:
              new_pos = self.getPlotItem().vb.mapSceneToView(event.position())
              new_x = round(max(0, min(new_pos.x(), self.total_duration)))
              new_y = max(0, min(new_pos.y(), 100))
              self.waypoint_moved.emit(self.active_channel, self._dragging_waypoint_index,
                                        new_x / self.total_duration * 100, new_y)
          self._is_pressed = False
          self._is_dragging = False
          self._dragging_waypoint_index = None
          self._needs_update = True
          self.update_plot()
          event.accept()
      else:
          super().mouseReleaseEvent(event)
  
  def mouseDoubleClickEvent(self, event):
      if event.button() == Qt.MouseButton.LeftButton:
          if hasattr(self, 'last_clicked_pos') and self.last_clicked_pos:
              x = round(max(0, min(self.last_clicked_pos.x(), self.total_duration)))
              y = max(0, min(self.last_clicked_pos.y(), 100))
              self.add_waypoint(x, y)
              self.last_clicked_pos = None
              event.accept()
      super().mouseDoubleClickEvent(event)
  
  def mouseWheelEvent(self, event):
      initial_range = self.getPlotItem().vb.viewRange()
      initial_x_range = initial_range[0]
      current_width = initial_x_range[1] - initial_x_range[0]
      min_width = max(0.1, self.total_duration - 2)
      delta = event.angleDelta().y()
      if delta > 0:
          super().mouseWheelEvent(event)
      else:
          if current_width < min_width:
              event.ignore()
              return
          else:
              scale_factor = 0.8 if delta < 0 else 1.2
              new_width_candidate = current_width * scale_factor
              if new_width_candidate < min_width:
                  center_x = sum(initial_x_range) / 2.0
                  new_x_min = center_x - min_width / 2.0
                  new_x_max = center_x + min_width / 2.0
                  self.getPlotItem().setXRange(new_x_min, new_x_max, padding=0)
                  event.ignore()
                  return
              else:
                  super().mouseWheelEvent(event)
      final_range = self.getPlotItem().vb.viewRange()
      final_x_range = final_range[0]
      x_min, x_max = final_x_range[0], final_x_range[1]
      if x_min < 0:
          offset = -x_min
          self.getPlotItem().setXRange(x_min + offset, x_max + offset, padding=0)
      if x_max > self.total_duration:
          offset = x_max - self.total_duration
          self.getPlotItem().setXRange(x_min - offset, x_max - offset, padding=0)


  def set_theme(self, theme: str):
      """
      Обновляет оформление графика в зависимости от выбранной темы.
      """
      self.theme = theme.lower()
      if theme.lower() == 'dark':
          self.setBackground(QColor(50, 50, 50, 0))
          self.getPlotItem().getAxis('bottom').setPen(QPen(QColor(200, 200, 200)))
          self.getPlotItem().getAxis('left').setPen(QPen(QColor(200, 200, 200)))
      elif theme.lower() == 'light':
          self.setBackground(QColor(50, 50, 50, 0))
          self.getPlotItem().getAxis('bottom').setPen(QPen(QColor(50, 50, 50)))
          self.getPlotItem().getAxis('left').setPen(QPen(QColor(50, 50, 50)))
          
  def update_grid_lines(self):
        """
        Оптимизированное создание линий-сетки и меток времени.
        """
        # Удаляем старые линии, которые больше не нужны.
        for line in self.vertical_grid_lines:
            self.getPlotItem().removeItem(line)
        self.vertical_grid_lines = []

        # Возвращаем метки времени в пул и скрываем их
        for label in self.time_labels:
            label.setVisible(False)
            if label not in self.time_label_pool:  # Если метка уже в пуле, не добавляем
                self.time_label_pool.append(label)

        self.time_labels = []

        view_range = self.getPlotItem().vb.viewRange()
        x_min, x_max = view_range[0]
        y_min, y_max = view_range[1]

        # Немного увеличим границы, чтобы линии не обрезались резко
        x_min = max(0, x_min - 1)
        x_max = min(self.total_duration, x_max + 1)
        
        offset = (y_max - y_min) * 0.05
        line_top = y_max - offset
        text_offset = 105

        p1 = self.getPlotItem().vb.mapViewToScene(QPointF(0, 0))
        p2 = self.getPlotItem().vb.mapViewToScene(QPointF(1, 0))
        pixels_per_sec = abs(p2.x() - p1.x())
        min_label_spacing_px = 50
        skip = max(1, int(np.ceil(min_label_spacing_px / max(pixels_per_sec, 1e-9))))

        label_index = 0
        for i in range(int(x_min), int(x_max) + 1):
            draw_line = (i == 0 or i == int(self.total_duration) or i % skip == 0)
            draw_label = (i % skip == 0 and i != 0 and i != int(self.total_duration))
            
            if draw_line:
                vertical_line = pg.InfiniteLine(
                    pos=i, angle=90,
                    pen=pg.mkPen((150, 150, 150, 100), width=1, style=Qt.PenStyle.DashLine)
                )
                vertical_line.setZValue(-10)
                self.getPlotItem().addItem(vertical_line)
                self.vertical_grid_lines.append(vertical_line)

            if draw_label:
                if label_index < len(self.time_label_pool):
                    time_label = self.time_label_pool[label_index] # Берем из пула
                    self.time_label_pool.pop(label_index)
                else:  # Если пул пуст (маловероятно, но на всякий случай)
                    time_label = pg.TextItem(color=(200, 200, 200), anchor=(0.5, 1))
                    self.getPlotItem().addItem(time_label)
                    
                hours = i // 3600
                minutes = (i % 3600) // 60
                seconds = i % 60
                time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                time_label.setText(time_str)
                time_label.setPos(i, line_top - text_offset)
                time_label.setVisible(True) # Показываем метку
                self.time_labels.append(time_label)
                label_index += 1

  def update_time_marker(self, current_time: float):
        """
        Перемещает маркер текущего времени в соответствии с текущим временем (в секундах).
        """
        if self.total_duration > 0:
            # Значение current_time соответствует оси X (от 0 до total_duration)
            self.current_time_marker.setPos(current_time)