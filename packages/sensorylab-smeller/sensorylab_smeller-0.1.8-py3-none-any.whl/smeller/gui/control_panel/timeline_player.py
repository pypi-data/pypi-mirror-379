# Содержимое файла: smeller/gui/timeline_player.py
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSlider, QLabel, QStyle, QStyleOptionSlider
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QKeyEvent
import time

class ClickableSlider(QSlider):
    is_dragging = False 
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # Создаем опцию для полученея параметров слайдера
            self.is_dragging = True
            opt = QStyleOptionSlider()
            self.initStyleOption(opt)
            # Вычисляем новое значение по горизонтали
            new_value = QStyle.sliderValueFromPosition(self.minimum(),
                                                        self.maximum(),
                                                        int(event.position().x()),
                                                        self.width())
            self.setValue(new_value)
            # Эмитируем событие перемещения слайдера (если требуется)
            self.sliderMoved.emit(new_value)
            event.accept()
        # Передаем событие родительскому методу
        super().mousePressEvent(event)
    def mouseMoveEvent(self, event):
        """
        Обработчик события перемещения мыши (перетаскивания).
        """
        if event.buttons() & Qt.MouseButton.LeftButton and self.is_dragging:
            opt = QStyleOptionSlider()
            self.initStyleOption(opt)
            new_value = QStyle.sliderValueFromPosition(self.minimum(),
                                                        self.maximum(),
                                                        int(event.position().x()),
                                                        self.width())
            # Устанавливаем новое значение
            self.setValue(new_value)
            # Эмитируем сигнал valueChanged (используем стандартный сигнал)
            self.valueChanged.emit(new_value)
            event.accept()
        super().mouseMoveEvent(event)
        
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False #  Сбрасываем флаг после отпускания кнопки
        super().mouseReleaseEvent(event)
              
class TimelinePlayer(QWidget):
    # Сигнал для передачи текущего времени (в секундах)
    current_time_changed = pyqtSignal(float)
    manual_seeked = pyqtSignal(float)
    manual_aroma_seeked = pyqtSignal(float)
    manual_aroma_start = pyqtSignal()
    
    playback_paused_for_seek = pyqtSignal() # New signal to indicate pause for seeking
    playback_resumed_after_seek = pyqtSignal() 
    # Сигналы для уведомления о запуске / паузе (можно связать с динамическим контроллером)
    play_pressed = pyqtSignal()
    pause_pressed = pyqtSignal()
    stop_pressed = pyqtSignal() # New signal for stop button
    set_volume = pyqtSignal(float)

        
    def __init__(self, total_duration=10, parent=None):
        """
        total_duration – общая длительность «воспроизведения» (например, дорожки распыления) в секундах.
        """
        super().__init__(parent)
        self.total_duration = total_duration
        self.is_playing = False
        self.start_time = None
        self._is_fullscreen = False
        self.paused_elapsed = 0  # сколько времени уже прошло до паузы
        self._init_ui()
        self.timer = QTimer(self)
        self.timer.setInterval(30)  # обновление каждые 50 мс
        self.timer.timeout.connect(self.update_progress)
        self.is_slider_dragging = False  # Add this line

    def _init_ui(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.play_pause_btn = QPushButton("Play")
        self.play_pause_btn.setFixedWidth(80)
        self.play_pause_btn.clicked.connect(self.toggle_play_pause)
        self.layout.addWidget(self.play_pause_btn)

        self.stop_btn = QPushButton("Stop") # Separate Stop button
        self.stop_btn.clicked.connect(self.stop)
        self.stop_btn.setEnabled(False) # Initially disabled
        self.layout.addWidget(self.stop_btn)
        # Слайдер без интерактивности: только для отображения прогресса
        self.slider = ClickableSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, int(self.total_duration * 1000))
        self.slider.setValue(0)
        # Слайдер можно сделать неинтерактивным, если не нужна возможность перематывания вручную:
        self.slider.setEnabled(True)
        self.slider.setTracking(True)
        self.slider.sliderPressed.connect(self.on_slider_pressed) # <--- Добавляем сигнал sliderPressed
        self.slider.sliderReleased.connect(self.on_slider_released)
        self.slider.valueChanged.connect(self.on_slider_value_changed)
        self.slider.sliderMoved.connect(self.on_slider_moved)
        self.is_slider_dragging = False
        self.layout.addWidget(self.slider)
        
    
        # Небольшая метка, показывающая текущее время
        self.time_label = QLabel("0.0 ")
        self.layout.addWidget(self.time_label)

    def toggle_play_pause(self):
        if self.is_playing:
            self.pause()
        else:
            self.play()

    def play(self):
        self.is_playing = True
        self.play_pressed.emit()
        self.play_pause_btn.setText("Pause")
        self.stop_btn.setEnabled(True)
        # Если это первый запуск – запоминаем стартовое время
        if self.start_time is None:
            self.start_time = time.time()
        else:
            # При возобновлении – учитываем время, прошедшее до паузы
            self.start_time = time.time() - self.paused_elapsed
        self.timer.start()

    def pause(self):
        self.is_playing = False
        self.timer.stop()
        self.pause_pressed.emit()
        self.manual_aroma_seeked.emit(self.slider.value() / 1000)
        
        self.play_pause_btn.setText("Play")
        self.paused_elapsed = time.time() - self.start_time if self.start_time else 0
    
    def stop(self):
        self.is_playing = False
        self.timer.stop()
        self.stop_pressed.emit() # Emit stop signal
        self.play_pause_btn.setText("Play")
        self.play_pause_btn.setEnabled(True)  # Enable Play when stopped
        self.stop_btn.setEnabled(False)  # Disable Stop
        self.start_time = None # Reset start time
        self.paused_elapsed = 0 # Reset paused elapsed time
        self.slider.setValue(0) # Reset slider position to 0
        self.time_label.setText("0.0 ") # Reset time label
        self.current_time_changed.emit(0.0) # Emit 0.0 time for plot reset
        self.manual_aroma_seeked.emit(0.0)

    def update_progress(self):
        if self.is_playing and not self.slider.isSliderDown() and not self.is_slider_dragging:
            elapsed = time.time() - self.start_time
            if elapsed > self.total_duration:
                elapsed = self.total_duration
                self.pause()  # если время закончено, стоп
            # Обновляем положение ползунка программно (это тоже вызовет сигнал valueChanged)
            self.slider.blockSignals(True)  # блокируем сигнал, чтобы не произошёл конфликт с ручной установкой
            self.slider.setValue(int(elapsed * 1000))
            self.slider.blockSignals(False)
            self.time_label.setText("{:.1f} ".format(elapsed))
            # Посылаем сигнал о текущем времени для обновления графического маркера
            self.current_time_changed.emit(elapsed)
            if not self.stop_btn.isEnabled:
                self.stop_btn.setEnabled(True)

    def set_total_duration(self, duration):
        """Позволяет задать общую длительность воспроизведения в секундах."""
        self.total_duration = duration
        self.slider.setRange(0, int(duration * 1000))
        self.time_label.setText("0.0 ")
        
    def on_slider_pressed(self): # <--- Обработчик sliderPressed
        self.is_slider_dragging = True #  Устанавливаем флаг, когда слайдер начинают двигать
        self.timer.stop()
        self.pause()

    def on_slider_released(self): # <--- Обработчик sliderReleased
        self.is_slider_dragging = False #  Сбрасываем флаг, когда слайдер отпускают
        new_time = self.slider.value() / 1000
        self.manual_aroma_seeked.emit(new_time)
        self.manual_seeked.emit(new_time)
        self.current_time_changed.emit(new_time)
        self.time_label.setText("{:.1f} ".format(new_time))
        if self.is_playing == True:
            self.timer.start()
            self.play_pressed.emit()
            self.manual_aroma_start.emit()

    def on_slider_moved(self, value):
        """
        Обработчик события sliderMoved (возникает при *перемещении* слайдера мышью).
        """
        
        if self.is_slider_dragging == True:  # Только если слайдер действительно перемещается
            new_time = value / 1000.0
            self.current_time_changed.emit(new_time)
            #self.manual_seeked.emit(new_time)  # Сигнал для смены изображения
            self.time_label.setText("{:.1f} ".format(new_time)) # обновляем
            self.paused_elapsed = new_time
            
    def on_slider_value_changed(self, value):
        """
        Вызывается, когда пользователь перемещает ползунок.
        Преобразуем значение слайдера (мс) в секунды и обновляем маркер на графике.
        Если плеер на паузе, обновляем внутреннее состояние.
        """
        if self.is_slider_dragging == False:
            new_time = value / 1000.0
            # Посылаем сигнал о новом времени (например, для обновления маркера в графике)
            #self.paused_elapsed = new_time
            if self.is_playing == True: self.start_time = time.time() - new_time
            else: self.paused_elapsed = new_time
            self.current_time_changed.emit(new_time)
            self.time_label.setText("{:.1f} ".format(new_time))

    def closeEvent(self, event):
        """Handle cleanup on window close"""
        self.stop()  # Make sure to stop the timer
        super().closeEvent(event)

    def toggle_fullscreen(self):
        """Переключает полноэкранный режим."""
        if not self._is_fullscreen:
            self._is_fullscreen = True
            self.showFullScreen() # Вход в полноэкранный режим
        else:
            self._is_fullscreen = False
            self.showNormal() # Выход из полноэкранного режима
            # --- Обработка событий клавиатуры и мыши ---
            
    def mouseDoubleClickEvent(self, event):
        """Обработчик двойного клика для полноэкранного режима."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.toggle_fullscreen()
        super().mouseDoubleClickEvent(event)
        
    def keyPressEvent(self, event: QKeyEvent):
        """Обрабатывает нажатия клавиш."""
        if event.key() == Qt.Key.Key_Plus:  # Увеличить громкость
            self.set_volume.emit(+ 0.05)
        elif event.key() == Qt.Key.Key_Minus:  # Уменьшить громкость
            self.set_volume.emit(- 0.05)
        elif event.key() == Qt.Key.Key_Space: # Пауза / плей
            self.toggle_play_pause()
        elif event.key() == Qt.Key.Key_Escape:
            if self._is_fullscreen: # Выходим из полноэкранного режима по нажатию Esc только если он активен
                self.toggle_fullscreen()     
        else:
            super().keyPressEvent(event)