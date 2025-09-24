# smeller/gui/channel_button.py
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QMouseEvent

class ChannelButton(QPushButton):
    long_press_activated = pyqtSignal(int) # Сигнал для долгого нажатия
    double_click_activated = pyqtSignal(int) # Сигнал для двойного клика
    hold_activated = pyqtSignal(int) # Сигнал для удержания (проверки устройства)

    def __init__(self, channel_index: int, parent=None):
        super().__init__(parent)
        self.channel_index = channel_index
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.long_press_event) # Обработчик таймера для долгого нажатия
        self.long_press_duration = 700  # 0.7 секунды в миллисекундах
        self.hold_duration = 500 # 0.5 секунды для удержания

        self.hold_timer = QTimer(self)
        self.hold_timer.setSingleShot(True)
        self.hold_timer.timeout.connect(self.hold_event)

        self.click_pos = None #  позиция клика для определения удержания

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.click_pos = event.pos() # Запоминаем позицию клика
            self.timer.start(self.long_press_duration) # Запускаем таймер долгого нажатия
            self.hold_timer.start(self.hold_duration) # Запускаем таймер удержания
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.timer.isActive(): # Если таймер долгого нажатия активен, значит, клик был коротким
                self.timer.stop()
                if self.hold_timer.isActive(): # Если таймер удержания еще активен, значит, это короткий клик, не удержание
                    self.hold_timer.stop()

        super().mouseReleaseEvent(event)

    #def mouseDoubleClickEvent(self, event: QMouseEvent):
    #    if event.button() == Qt.MouseButton.LeftButton:
    #        self.double_click_activated.emit(self.channel_index) # Emit double click signal
    #    super().mouseDoubleClickEvent(event)

    def long_press_event(self):
        """Вызывается при срабатывании таймера долгого нажатия."""
        if self.click_pos is not None: # Проверяем, что mousePressEvent был и позиция клика запомнена
            # Проверяем, что отпускание кнопки произошло примерно в том же месте, что и нажатие (чтобы отличить долгое нажатие от перетаскивания)
            release_pos = self.mapFromGlobal(self.cursor().pos())
            if (self.click_pos - release_pos).manhattanLength() < 10: #  Допуск в 10 пикселей
                self.long_press_activated.emit(self.channel_index) # Emit long press signal

    def hold_event(self):
        """Вызывается при срабатывании таймера удержания (hold)."""
        if self.mouse_is_pressed(): # Проверяем, что кнопка все еще нажата
            self.hold_activated.emit(self.channel_index) # Emit hold signal

    def mouse_is_pressed(self) -> bool:
        """Проверяет, нажата ли кнопка мыши на виджете."""
        return self.underMouse() and (self.mouseGrabber() is self or self.underMouse()) #  Более надежная проверка