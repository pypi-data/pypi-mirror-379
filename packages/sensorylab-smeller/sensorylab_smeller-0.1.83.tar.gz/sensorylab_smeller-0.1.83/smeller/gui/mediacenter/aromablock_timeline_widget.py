# Содержимое файла: smeller/mediacenter/aromablock_timeline_widget.py
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parents[2]  # Поднимаемся на два уровня вверх
sys.path.append(str(project_root))

import logging
import math

from typing import Any

from PyQt6.QtCore import Qt, QRectF, QPointF, pyqtSignal, QTimer, QEvent
from PyQt6.QtGui import QColor, QBrush, QPen, QPalette, QPainter, QCursor, QMouseEvent, QTransform
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsObject,
    QMainWindow,
    QVBoxLayout,
    QGraphicsItem,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QGraphicsLineItem,
)

from smeller.models.aroma_block import AromaBlock  # Убедитесь, что данный модуль доступен


# Настройка модуля логирования
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


class ControlBarWidget(QWidget):
    """A custom widget for play/pause/stop controls and time display."""

    play_pause_signal = pyqtSignal()
    stop_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        self.play_pause_button = QPushButton("Play")
        self.stop_button = QPushButton("Stop")
        self.current_time_label = QLabel("0.00s")
        self.current_time_label.setFixedWidth(50)

        layout.addWidget(self.play_pause_button)
        layout.addWidget(self.stop_button)
        layout.addStretch(1)  # Push time to the right
        layout.addWidget(self.current_time_label)
        self.setFixedWidth(150)

        self.play_pause_button.clicked.connect(self.play_pause_signal)
        self.stop_button.clicked.connect(self.stop_signal)

    def set_time(self, time_str: str):
        self.current_time_label.setText(time_str)
    def set_playing_state(self, is_playing:bool):
        if is_playing:
            self.play_pause_button.setText("Pause")
        else:
            self.play_pause_button.setText("Play")
            
class TimelineHeaderWidget(QFrame):
    # Сигнал, передающий время (в секундах), соответствующее месту клика
    timelineClicked = pyqtSignal(float)
    
    def __init__(self, timeline_start=0, timeline_end=1000, zoom_level=1.0, parent=None):
        super().__init__(parent)
        self.timeline_start = timeline_start
        self.timeline_end = timeline_end
        self.zoom_level = zoom_level
        self.setFixedHeight(30)
        self.vertical_indicator_time = None  # Время для отображения вертикальной линии
        self.setStyleSheet("background-color: #323232;")
        
    def set_zoom_level(self, zoom: float):
        if zoom > 0:
            self.zoom_level = zoom
            self.update()    
            
    def set_vertical_indicator(self, time_value: float):
        self.vertical_indicator_time = time_value
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        widget_width = self.width()
        widget_height = self.height()
        # Вычисляем длину таймлайна в пикселях с учётом зума.
        effective_length = (self.timeline_end - self.timeline_start) * self.zoom_level
        # Чтобы при максимальном удалении (zoom out) длина не была меньше ширины виджета:
        effective_length = max(effective_length, widget_width)
        
        # Подбираем интервал между делениями: ориентировочно ~100 пикселей между делениями
        desired_tick_spacing = 100  
        duration = self.timeline_end - self.timeline_start
        tick_interval = duration / (effective_length / desired_tick_spacing)
        # Округлим до "красивого" числа:
        if tick_interval > 0:
            magnitude = 10 ** math.floor(math.log10(tick_interval))
            normalized = tick_interval / magnitude
            if normalized < 1.5:
                nice_tick = 1 * magnitude
            elif normalized < 3:
                nice_tick = 2 * magnitude
            elif normalized < 7:
                nice_tick = 5 * magnitude
            else:
                nice_tick = 10 * magnitude
        else:
            nice_tick = 1
        
        pen = QPen(QColor("#B4B4B4"))
        painter.setPen(pen)
        font = painter.font()
        font.setPointSize(8)
        painter.setFont(font)
        
        # Рисуем деления: начинаем с первого деления после timeline_start
        start_tick = self.timeline_start - (self.timeline_start % nice_tick) + nice_tick
        tick = start_tick
        while tick <= self.timeline_end:
            x = (tick - self.timeline_start) * self.zoom_level
            if x > widget_width:
                break
            painter.drawLine(int(x), 0, int(x), 10)
            time_text = str(int(tick))
            painter.drawText(int(x) + 2, 25, time_text)
            tick += nice_tick
        
        # Рисуем вертикальный индикатор, если он установлен
        if self.vertical_indicator_time is not None:
            indicator_x = (self.vertical_indicator_time - self.timeline_start) * self.zoom_level
            if 0 <= indicator_x <= widget_width:
                indicator_pen = QPen(QColor("red"))
                indicator_pen.setWidth(2)
                painter.setPen(indicator_pen)
                painter.drawLine(int(indicator_x), 0, int(indicator_x), widget_height)
            
        painter.end()
            
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            x = event.position().x() if hasattr(event, "position") else event.x()
            # Вычисляем время по x с учетом зума
            time_value = self.timeline_start + (x / self.zoom_level)
            self.timelineClicked.emit(time_value)
            self.set_vertical_indicator(time_value)
            event.accept()
        else:
            super().mousePressEvent(event)
        
        
class TrackInfoBlock(QFrame):

    mute_toggled = pyqtSignal(bool)  # Сигнал изменения состояния Mute
    solo_toggled = pyqtSignal(bool)  # Сигнал изменения состояния Solo

    def __init__(self, track_name: str, parent=None):
        super().__init__(parent)
        self.track_name = track_name

        layout = QVBoxLayout(self)
        buttons_layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        self.name_label = QLabel(track_name)
        self.mute_button = QPushButton("Mute")
        self.solo_button = QPushButton("Solo")

        # Устанавливаем фиксированный размер для блока информации,
        # чтобы он не изменялся при изменении размеров окна
        self.setFixedWidth(150)  # Подберите подходящую ширину


        # Делаем кнопки "чекбоксами" (с фиксацией нажатого состояния)
        self.mute_button.setCheckable(True)
        self.solo_button.setCheckable(True)

        layout.addWidget(self.name_label)
        buttons_layout.addWidget(self.mute_button)
        buttons_layout.addWidget(self.solo_button)
        layout.addLayout(buttons_layout) # убрал

        # Обработчики нажатия кнопок
        self.mute_button.toggled.connect(self.mute_toggled.emit)
        self.solo_button.toggled.connect(self.solo_toggled.emit)
        # self.setStyleSheet("background-color: #666;")  # Тёмно-серый цвет фона (по желанию)
        


class TrackWidget(QWidget):
    """Represents a single track in the timeline."""

    track_muted = pyqtSignal(int, bool)
    track_soloed = pyqtSignal(int, bool)
    track_scrolled = pyqtSignal(int)
    
    def __init__(
        self,
        track_index: int,
        track_height: float,
        timeline_start: float,
        timeline_end: float,
        zoom_level: float,
        parent_timeline: 'AromaBlockTimelineWidget' = None, # Pass parent timeline here
        parent=None,
    ):
        super().__init__(parent)
        self.track_index = track_index
        self.track_height = track_height
        self.timeline_start = timeline_start
        self.timeline_end = timeline_end
        self.zoom_level = zoom_level
        self.parent_timeline = parent_timeline # Store parent timeline

        self.track_layout = QHBoxLayout(self)
        self.track_layout.setContentsMargins(0, 0, 0, 0)
        self.track_layout.setSpacing(0)

        self.info_block = TrackInfoBlock(f"Track {track_index + 1}")
        self.info_block.mute_toggled.connect(
            lambda muted: self.track_muted.emit(self.track_index, muted)
        )
        self.info_block.solo_toggled.connect(
            lambda soloed: self.track_soloed.emit(self.track_index, soloed)
        )

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setFrameStyle(QFrame.Shape.NoFrame)
        self.view.setFixedHeight(self.track_height)
        self.view.viewport().installEventFilter(
            self
        )  # Install event filter for clicks
        self.view.horizontalScrollBar().valueChanged.connect(self.track_scrolled.emit)

        self.track_layout.addWidget(self.info_block, alignment= Qt.AlignmentFlag.AlignLeft)
        self.track_layout.addWidget(
            self.view, alignment=Qt.AlignmentFlag.AlignLeft
        )

        self.indicator_pen = QPen(QColor("red"), 2)
        self.indicator_line = self.scene.addLine(
            0, -self.track_height, 0, self.track_height, self.indicator_pen
        )
        self.indicator_line.setZValue(100)
        self.indicator_line.setVisible(False)
        self.update_scene_rect()


    def update_scene_rect(self):
        """Updates the scene rectangle based on timeline range and zoom."""
        #  Ключевое изменение: сохраняем длину видимой области
        visible_duration = self.timeline_end - self.timeline_start
        self.scene.setSceneRect(
            self.timeline_start * self.zoom_level,
            0,
            visible_duration * self.zoom_level,  # Используем сохраненную длину
            self.track_height,
        )
        self.update_time_indicator(
            self.parent_timeline.get_current_time()
            if self.parent_timeline is not None
            else self.timeline_start
        )

    def set_zoom_level(self, zoom_level: float):
        """Sets the zoom level and updates the scene rectangle."""
        self.zoom_level = zoom_level
        self.update_scene_rect()
        for item in self.scene.items():
            if isinstance(item, DraggableAromaBlockItem):
                item.zoom_level = zoom_level
                item.update_block_geometry()


    def update_time_indicator(self, time_value: float):
        """Updates the position of the time indicator line."""
        x_position = (time_value - self.timeline_start) * self.zoom_level
        self.indicator_line.setLine(
            x_position, -self.track_height, x_position, self.track_height
        )
        self.indicator_line.setVisible(True)


    def add_aroma_block_item(self, aroma_block: AromaBlock):
        """Adds an aroma block item to the track."""
        item = DraggableAromaBlockItem(
            self.parent_timeline,  # Pass AromaBlockTimelineWidget instance here
            aroma_block,
            self.track_index,
        )
        # item.block_time_changed.connect(self.block_time_changed.emit)  # Connect if needed
        # item.track_changed.connect(self.handle_track_change) # Connect if needed
        self.scene.addItem(item)
        initial_x = (
            aroma_block.start_time * 10 * self.zoom_level
        )  # Use time_scale=10 as default
        item.setPos(QPointF(initial_x, 0))
        item._last_valid_position = item.pos()
        item.current_track_index = self.track_index
        return item  # Return the item

    def clear(self):
        """Clears all items from the scene."""
        self.scene.clear()
        # Re-add the indicator line after clearing:
        self.indicator_line = self.scene.addLine(
            0, -self.track_height, 0, self.track_height, self.indicator_pen
        )
        self.indicator_line.setZValue(100)
        self.indicator_line.setVisible(False)

    def eventFilter(self, watched, event):
        """Handles clicks outside of aroma blocks."""
        if (
            event.type() == QEvent.Type.MouseButtonPress
            and watched == self.view.viewport()
        ):
            view_pos = event.pos()
            scene_pos = self.view.mapToScene(view_pos)
            item_at_pos = self.scene.itemAt(scene_pos, QTransform())
            if item_at_pos is None or not isinstance(item_at_pos, DraggableAromaBlockItem):
                if self.parent_timeline:
                    self.parent_timeline.deselect_all_blocks() # Deselect all blocks on timeline
                    
        return super().eventFilter(watched, event)
    def get_scene(self):
        """ Get scene"""
        return self.scene
    def get_view(self):
        """Get view"""
        return self.view

    def resizeEvent(self, event):
        """
        Обработчик изменения размера виджета.
        Обновляем размер viewport, чтобы он соответствовал новому размеру виджета.
        """
        super().resizeEvent(event)
        self.update_scene_rect() # Важно обновить viewport при изменении размера!
        
        
class DraggableAromaBlockItem(QGraphicsObject):

    block_time_changed = pyqtSignal(int, float, float)
    track_changed = pyqtSignal(int, int)

    def __init__(self, timeline_widget: 'AromaBlockTimelineWidget', aroma_block: AromaBlock, track_index: int, block_height: float = 50, time_scale_pixels_per_sec: float = 10, zoom_level: float = 1, parent=None):
        super().__init__(parent)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges, True)
        self.setAcceptHoverEvents(True)
        
        self.timeline_widget = timeline_widget
        self.aroma_block = aroma_block
        self.current_track_index = track_index
        
        self.block_height = block_height
        self.time_scale_pixels_per_sec = time_scale_pixels_per_sec
        self.zoom_level = zoom_level
        
        self.collision_highlight_pen = QPen(QColor("white"), 4)
        self.collision_side = None
        
        self._last_mouse_pos = None
        self._last_valid_position = self.pos()
        self._selected = False
        
        self.update_block_style()
        self._update_rect()
        
    def update_block_style(self):
        # Проверяем, является ли текущий блок выделенным через timeline_widget
        self._border_color = QColor(255, 255, 0) if self._selected else QColor(Qt.GlobalColor.transparent)
        self._fill_color = QColor(100, 149, 237, 200) if self._selected else QColor(100, 149, 237, 150)
        self.update()
        
    def _update_rect(self):
        start_x_scaled = self.aroma_block.start_time * self.time_scale_pixels_per_sec * self.zoom_level
        stop_x_scaled = self.aroma_block.stop_time * self.time_scale_pixels_per_sec * self.zoom_level
        width = max(stop_x_scaled - start_x_scaled, 10)
        self._rect = QRectF(0, -self.block_height / 2, width, self.block_height)

    def update_block_geometry(self):
        self._update_rect()
        self.prepareGeometryChange()
        self.update()

    def boundingRect(self) -> QRectF:
        return self._rect

    def paint(self, painter: QPainter, option, widget=None):
        painter.setBrush(QBrush(self._fill_color))
        pen = QPen(self._border_color)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawRect(self._rect)
        if self.collision_side and self._selected == True:
            painter.setPen(self.collision_highlight_pen)
            if self.collision_side == "left":
                painter.drawLine(QPointF(0, -self.block_height / 2), QPointF(0, self.block_height / 2))
            elif self.collision_side == "right":
                painter.drawLine(QPointF(self._rect.width(), -self.block_height / 2), QPointF(self._rect.width(), self.block_height / 2))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._last_mouse_pos = event.scenePos()
            self._last_valid_position = self.pos()
            # Вызываем select_block у timeline_widget
            self.timeline_widget.select_block(self)
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
            self._initial_mouse_y = event.scenePos().y()
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        delta = event.scenePos() - self._last_mouse_pos
        candidate_x = self._last_valid_position.x() + delta.x()
        if self.timeline_widget is not None:
            left_limit = self.timeline_widget.timeline_start * self.timeline_widget.zoom_level
            right_limit = self.timeline_widget.timeline_end * self.timeline_widget.zoom_level - self.boundingRect().width()
            candidate_x = max(left_limit, min(candidate_x, right_limit))
        new_track_index = self.current_track_index
        timeline_widget = self.timeline_widget
        if timeline_widget is not None and isinstance(timeline_widget, AromaBlockTimelineWidget):
            if 0 <= self.current_track_index < len(timeline_widget.tracks): # Check track index
                current_track = timeline_widget.tracks[self.current_track_index] # Get TrackWidget
                current_view = current_track.get_view() # Get view from TrackWidget
                pos_in_view = current_view.mapFromScene(event.scenePos())
                new_y_scene = event.scenePos().y()
            if abs(new_y_scene - self._initial_mouse_y) > self.block_height / 2:
                new_track_index = timeline_widget.get_track_index_at(pos_in_view.y())
                if new_track_index != self.current_track_index:
                    self.change_track(new_track_index, timeline_widget, event.scenePos())
        candidate = QPointF(candidate_x, self._last_valid_position.y())
        self.setPos(candidate)
        self.handle_collisions(event)
        self._last_mouse_pos = event.scenePos()
        self.update()
        event.accept()

    def change_track(self, new_track_index: int, parent_widget: 'AromaBlockTimelineWidget', mouse_scene_pos: QPointF):
        QTimer.singleShot(110, lambda: self._do_change_track(new_track_index, parent_widget, mouse_scene_pos))

    def _do_change_track(self, new_track_index: int, parent_widget: 'AromaBlockTimelineWidget', mouse_scene_pos: QPointF):
        old_scene = self.scene()
        if old_scene:
            old_scene.removeItem(self)
        new_scene = parent_widget.track_scenes[new_track_index]
        new_scene.addItem(self)
        self.current_track_index = new_track_index
        self.setY(0)
        current_view = parent_widget.track_views[new_track_index]
        global_pos = QCursor.pos()
        view_pos = current_view.mapFromGlobal(global_pos)
        self._last_mouse_pos = current_view.mapToScene(view_pos)
        self._last_valid_position = self.pos()
        simulated_press = QMouseEvent(
            QEvent.Type.MouseButtonPress,
            self.mapFromScene(mouse_scene_pos),
            mouse_scene_pos,
            Qt.MouseButton.LeftButton,
            Qt.MouseButton.LeftButton,
            Qt.KeyboardModifier.NoModifier
        )
        QApplication.postEvent(self, simulated_press)
        self.track_changed.emit(self.aroma_block.id, new_track_index)

    def mouseReleaseEvent(self, event):
        self.unsetCursor()
        self.setPos(self._last_valid_position)
        self.collision_side = None
        self.update()
        self.block_time_changed.emit(self.aroma_block.id, self.aroma_block.start_time, self.aroma_block.stop_time)
        event.accept()

    def handle_collisions(self, event):
        self.collision_side = None
        colliding_blocks = [item for item in self.collidingItems() if isinstance(item, DraggableAromaBlockItem)]
        if colliding_blocks:
            other_block = colliding_blocks[0]
            if event.scenePos().x() < other_block.sceneBoundingRect().left():
                self.collision_side = "right"
                new_x = other_block.sceneBoundingRect().left() - self.boundingRect().width() - 2
            elif event.scenePos().x() > other_block.sceneBoundingRect().right():
                self.collision_side = "left"
                new_x = other_block.sceneBoundingRect().right() + 2
            else:
                self.collision_side = None
                new_x = self._last_valid_position.x()
            self.setX(new_x)
            self._last_valid_position = self.pos()
        else:
            self._last_valid_position = self.pos()
            
class AromaBlockTimelineWidget(QFrame):
    play_pause_signal = pyqtSignal( bool)
    stop_signal = pyqtSignal(bool)
    block_time_changed = pyqtSignal(int, float, float)
    track_muted = pyqtSignal(int, bool)
    track_soloed = pyqtSignal(int, bool)

    def __init__(
        self,
        block_height: float,
        time_scale_pixels_per_sec: float,
        zoom_level: float,
        parent=None,
    ):
        super().__init__(parent)
        logging.debug("Инициализация AromaBlockTimelineWidget...")
        self.block_height = block_height
        self.time_scale_pixels_per_sec = time_scale_pixels_per_sec
        self.zoom_level = zoom_level
        self.track_scenes = []
        self.track_views = []
        self.info_blocks = []
        self.num_tracks = 1
        self.track_spacing = 0
        self.track_height = 60
        self.timeline_start = 0
        self.timeline_end = 1000
        self.tracks = (
            []
        )  # Store TrackWidget instances

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(self.track_spacing)
        main_layout.setContentsMargins(0, 0, 0, 0)


        timeline_layout = QHBoxLayout()

        # --- Control Bar (replace placeholder) ---
        self.control_bar = ControlBarWidget()
        self.control_bar.play_pause_signal.connect(self.toggle_play_pause)
        self.control_bar.stop_signal.connect(self.stop_playback)
        self.control_bar.setFixedWidth(150)
        timeline_layout.setContentsMargins(0, 0, 0, 0)
        # Добавляем новый виджет с разметкой времени (TimelineHeaderWidget) сверху
        self.timeline_header = TimelineHeaderWidget(self.timeline_start, self.timeline_end, self.zoom_level, self)
        timeline_layout.addWidget(self.control_bar)
        timeline_layout.addWidget(self.timeline_header)
        main_layout.addLayout(timeline_layout)
        # При клике в timelineHeader обновляем вертикальный индикатор
        self.timeline_header.timelineClicked.connect(self.update_time_indicator)
    
        self.add_track()  # Add initial track

        self.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Sunken)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(50, 50, 50))
        self.setPalette(palette)
        logging.debug("AromaBlockTimelineWidget инициализирован.")
                    
    def add_track(self):
        """Adds a new track to the timeline."""
        track = TrackWidget(
            len(self.tracks),
            self.track_height,
            self.timeline_start,
            self.timeline_end,
            self.zoom_level,
            parent_timeline=self # Pass self here
        )
        track.track_muted.connect(self.track_muted.emit)  # Connect track signals
        track.track_soloed.connect(self.track_soloed.emit)
        self.tracks.append(track)
        self.layout().addWidget(track, alignment= Qt.AlignmentFlag.AlignLeft)  # Add to layout
        self.num_tracks += 1
        
    def toggle_play_pause(self):
        self.play_pause_signal.emit(True)

    def stop_playback(self):
        self.stop_signal.emit(True)
            
    def clear_timeline(self) -> None:
        """Clears all tracks."""
        for track in self.tracks:
            track.clear()
            
    def set_zoom_level(self, zoom: float) -> None:
        if zoom > 0:
            min_zoom = self.width() / (self.timeline_end - self.timeline_start)
            self.zoom_level = max(zoom, min_zoom)
            self.timeline_header.set_zoom_level(self.zoom_level)
            for track in self.tracks:
                track.set_zoom_level(self.zoom_level)
            self.update_time_indicator(
                self.get_current_time()
            )  # Update indicator after zoom


    def update_time_indicator(self, time_value: float):
        """Updates the time indicator on all tracks and the header."""
        for track in self.tracks:
            track.update_time_indicator(time_value)
        self.timeline_header.set_vertical_indicator(time_value)
       
    def get_current_time(self) -> float:
        """Gets the current time from the first track's indicator (if exists)."""
        if self.tracks:
            # Extract time from the first track's indicator line position
            return (
                self.timeline_start
                + self.tracks[0].indicator_line.line().x1() / self.zoom_level
            )
        return self.timeline_start  # Default to start if no tracks     
            
    def add_aroma_block_item(self, aroma_block: AromaBlock, track_index: int):
        """Adds an aroma block to the specified track."""
        if 0 <= track_index < len(self.tracks):
            item = self.tracks[track_index].add_aroma_block_item(aroma_block)
            item.block_time_changed.connect(
                self.block_time_changed.emit
            )  # Connect signals if needed
            item.track_changed.connect(self.handle_track_change)
            return item


    def set_zoom_level(self, zoom: float) -> None:
        if zoom > 0:
            self.zoom_level = zoom
            for scene in self.track_scenes:
                for item in scene.items():
                    if isinstance(item, DraggableAromaBlockItem):
                        item.zoom_level = zoom
                        item.update_block_geometry()
                self.update_timeline_labels(scene)
                for item in scene.items():
                    if isinstance(item, QGraphicsLineItem):
                         item.setLine(self.timeline_start * self.zoom_level, 0, self.timeline_end * self.zoom_level, 0)


    def get_track_index_at(self, y: float) -> int:
        """Get track index"""
        for index, track in enumerate(self.tracks):
            if track.geometry().contains(track.mapFromGlobal(QCursor.pos())):
                return index
        return 0

    def handle_track_change(self, block_id: int, new_track_index: int):
        print(f"Block {block_id} moved to track {new_track_index}")


    def select_block(self, block):
        """Select block"""
        self.deselect_all_blocks()
        block._selected = True
        block.update_block_style()

                    
    def deselect_all_blocks(self):
        """Deselect all blocks"""
        for track in self.tracks:
            scene = track.get_scene()
            for item in scene.items():
                if isinstance(item, DraggableAromaBlockItem):
                    item._selected = False
                    item.update_block_style()
            
    def resizeEvent(self, event):
        """Called when resize event"""
        super().resizeEvent(event)
        self.set_zoom_level(self.zoom_level)


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Aroma Timeline Test")

            central_widget = QWidget()
            self.setCentralWidget(central_widget)

            layout = QVBoxLayout(central_widget)
            timeline_widget = AromaBlockTimelineWidget(
                block_height=50,
                time_scale_pixels_per_sec=10,
                zoom_level=1.0
            )
            layout.addWidget(timeline_widget, alignment= Qt.AlignmentFlag.AlignLeft)
            # Создаём два блока для размещения на одной линии
            block1 = AromaBlock(id=1, name="Block 1", start_time=1.0, stop_time=6.0, channel_configurations={})
            block2 = AromaBlock(id=2, name="Block 2", start_time=8.0, stop_time=15.0, channel_configurations={})
            block3 = AromaBlock(id=3, name="Block 3", start_time=1.0, stop_time=5.0, channel_configurations={})
            timeline_widget.add_aroma_block_item(block2, track_index=0)
            timeline_widget.add_aroma_block_item(block1, track_index=0)


    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())