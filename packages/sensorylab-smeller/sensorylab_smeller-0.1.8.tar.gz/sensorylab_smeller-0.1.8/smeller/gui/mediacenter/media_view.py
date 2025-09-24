# Содержимое файла: smeller/mediacenter/media_view.py
from PyQt6.QtWidgets import QSizePolicy, QVBoxLayout, QLabel, QFrame, QGraphicsDropShadowEffect, QPushButton, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal, QUrl, QFileInfo, QTimer
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QDragMoveEvent, QKeyEvent, QMouseEvent

from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
import logging

logger = logging.getLogger(__name__)

class MediaView(QFrame):
    mediaDropped = pyqtSignal(str)
    media_duration_changed = pyqtSignal(float) # <---  Определяем новый сигнал
    stop_pressed = pyqtSignal() # New signal for stop button
    """
    Placeholder виджет для отображения медиаконтента (видео, аудио).
    На данном этапе включает кнопки управления (Play/Pause, Stop) и методы-заглушки
    для имитации работы медиаплеера.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("mediaViewFrame")
        self.setAcceptDrops(True)  # Включаем поддержку drag & drop # Для стилизации через CSS
        self.media_path = None  # Путь к загруженному медиафайлу (пока не используется)
        self._is_fullscreen = False
        self._start_time = 0.0  # Время начала аромаблока (в секундах)
        self._stop_time = 10.0   # Время окончания аромаблока (в секундах)
        
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mediaPlayer = QMediaPlayer() # Инициализация QMediaPlayer
        
        self.audio_output = QAudioOutput()  # Создаем QAudioOutput
        self.mediaPlayer.setAudioOutput(self.audio_output) # Подключаем AudioOutput к MediaPlayer
        self.audio_output.setVolume(50)
        # QVideoWidget для показа видео
        self.video_widget = QVideoWidget()
        self.video_widget.setSizePolicy(QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Expanding)
        self.mediaPlayer.setVideoOutput(self.video_widget) #  Связываем MediaPlayer и VideoWidget
    
        self.layout.addWidget(self.video_widget, stretch=1)
        self.video_widget.hide()
        self.placeholder_label = QLabel("Media Player Placeholder")
        self.placeholder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.placeholder_label)
        self.placeholder_label.show()
        
        self.default_style = """
            QFrame#mediaViewFrame {
                background-color: #2b2b2b;
                border: 2px dashed #555;
                border-radius: 5px;
                min-height: 200px;
                color: #ddd;
                padding: 10px;
            }
            QVideoWidget {
                border-radius: 15px;
            }
            QPushButton {
                background-color: #555;
                color: #ddd;
                border: 1px solid #777;
                border-radius: 5px;
                padding: 5px 10px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #777;
            }
            QLabel {
                color: #ddd;
                margin: 5px 0;
            }
        """
        self.drag_active_style = """
            QFrame#mediaViewFrame {
                background-color: #3c3c3c;
                border: 2px solid #777;
                border-radius: 5px;
                min-height: 200px;
                color: #ddd;
                padding: 10px;
            }
            QVideoWidget {
                border-radius: 15px;
            }
        """
        self.setStyleSheet(self.default_style)
        self.mediaPlayer.errorOccurred.connect(self.handle_media_error) # Подключаем обработку ошибок

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setColor(Qt.GlobalColor.black)
        shadow.setOffset(0)
        self.setGraphicsEffect(shadow)
        # Обработка событий для QVideoWidget
        self.video_widget.setAcceptDrops(True)
        self.video_widget.dragEnterEvent = self.dragEnterEvent
        self.video_widget.dragMoveEvent = self.dragMoveEvent
        self.video_widget.dropEvent = self.dropEvent
        self.video_widget.dragLeaveEvent = self.dragLeaveEvent
                # Включаем обработку событий клавиатуры для MediaView
        self.video_widget.mouseDoubleClickEvent = self.handle_video_widget_double_click

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        
    def dragLeaveEvent(self, event):
        self.setStyleSheet(self.default_style)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            self.setStyleSheet(self.drag_active_style)  # Изменяем стиль на активный при перетаскивании
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)
            
    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragMoveEvent(event)
                    
    def dropEvent(self, event: QDropEvent):
        self.setStyleSheet(self.default_style)
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            file_path = url.toLocalFile()
            self.load_media(file_path) #  Загружаем медиа при drop
            self.mediaDropped.emit(file_path)
            event.acceptProposedAction()
            self.stop_pressed.emit()
            return
        else:
            super().dropEvent(event)

    def load_media(self, media_path):
        """Загрузка медиафайла."""
        self.media_path = media_path
        file_info = QFileInfo(media_path)
        if not file_info.exists() or not file_info.isFile():
            QMessageBox.warning(self, "Ошибка", f"Файл не найден или не является файлом: {media_path}")
            return

        self.mediaPlayer.setSource(QUrl.fromLocalFile(media_path))
        print(f"MediaView: load_media called with path: {media_path}")
        print(f"MediaView: mediaStatus after setSource: {self.mediaPlayer.mediaStatus()}") # Проверяем статус

        self.placeholder_label.hide()
        self.video_widget.show()
        self.video_widget.raise_()
        self.video_widget.update()

        # Получаем длительность после загрузки (через небольшой таймаут, если нужно)
        QTimer.singleShot(100, self.update_duration) # Запускаем через 100 мс

    def update_duration(self):
        """Обновляет продолжительность и передает ее в TimelinePlayer."""
        duration_ms = self.get_media_duration()
        duration_sec = duration_ms / 1000.0
        print(f"MediaView: Media Duration: {duration_sec} seconds")
        self.media_duration_changed.emit(duration_sec) #  Сигнал нужно определить ниже
        self._stop_time = duration_sec
            
    def play(self):
        self.video_widget.show()
        # Явно убедимся, что видео-виджет показывается
        self.mediaPlayer.play()
    def pause(self):
        """Пауза воспроизведения."""
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaPlayer.pause()

    def stop(self):
        try:
            # Если плеер находится не в состоянии "stopped", останавливаем его
            if self.mediaPlayer.playbackState() != QMediaPlayer.PlaybackState.StoppedState:
                self.mediaPlayer.pause()
                self.mediaPlayer.setPosition(0)
        except Exception as e:
            print(f"Ошибка при остановке медиаплеера: {e}")

        print("MediaView: stop вызван")

    def set_start_time(self, time_sec: float):
        """Устанавливает время начала аромаблока (в секундах)."""
        self._start_time = time_sec
        print(f"MediaView: set_start_time called with time: {time_sec}")

    def get_start_time(self) -> float:
        """Возвращает время начала аромаблока."""
        return self._start_time

    def set_stop_time(self, time_sec: float):
        """Устанавливает время окончания аромаблока (в секундах)."""
        self._stop_time = time_sec
        print(f"MediaView: set_stop_time called with time: {time_sec}")

    def get_stop_time(self) -> float:
        """Возвращает время окончания аромаблока."""
        return self._stop_time
    
    def set_position(self, position):
        """Устанавливает позицию воспроизведения (в миллисекундах)."""
        if self.mediaPlayer:
            self.mediaPlayer.setPosition(position)

    def get_media_duration(self):
        """Возвращает длительность загруженного медиафайла в миллисекундах."""
        if self.mediaPlayer and self.mediaPlayer.mediaStatus() == QMediaPlayer.MediaStatus.LoadedMedia:
            return self.mediaPlayer.duration()
        return 0
    def get_current_position(self):
        """Возвращает текущую позицию воспроизведения в миллисекундах."""
        if self.mediaPlayer:
            return self.mediaPlayer.position()
        return 0
    
    def set_volume(self, step):
        self.audio_output.setVolume(min(1.0, 
                                        self.audio_output.volume() + step
        ))
        
    def handle_media_error(self):
        """Обработчик ошибок медиаплеера."""
        error = self.mediaPlayer.error()
        error_string = self.mediaPlayer.errorString()
        QMessageBox.critical(self, "Ошибка медиаплеера", f"Произошла ошибка при воспроизведении медиа: {error_string} (код ошибки: {error})")
        print(f"MediaView: MediaPlayer error occurred: {error_string} (code: {error})")
            
            
    def connect_signals(self, main_window):
        self.media_duration_changed.connect(main_window.update_total_duration)
        self.stop_pressed.connect(main_window.control_panel.timeline_player.stop)
    
    def toggle_fullscreen(self):
        """Переключает полноэкранный режим."""
        if not self._is_fullscreen:
            self._is_fullscreen = True
            self.showFullScreen() # Вход в полноэкранный режим
        else:
            self._is_fullscreen = False
            self.showNormal() # Выход из полноэкранного режима
            # --- Обработка событий клавиатуры и мыши ---

    def toggle_fullscreen(self):
        """Переключает полноэкранный режим для QVideoWidget."""
        if not self.media_path:
            logger.warning("Cannot toggle fullscreen: No media loaded.")
            return # Не переключаем, если нет медиа

        # Определяем желаемое состояние
        target_fullscreen_state = not self._is_fullscreen

        logger.info(f"Toggling video fullscreen to: {target_fullscreen_state}")
        # Используем встроенный метод QVideoWidget
        self.video_widget.setFullScreen(target_fullscreen_state)

        # Обновляем наш флаг состояния. Фильтр событий тоже может это сделать,
        # но лучше обновить сразу для консистентности.
        self._is_fullscreen = target_fullscreen_state
        #self.fullscreen_changed.emit(self._is_fullscreen) # Сообщаем об изменении

        # Управление фокусом:
        if self._is_fullscreen:
            # В полноэкранном режиме фокус должен быть у video_widget или его viewport,
            # чтобы он мог обрабатывать события (например, Esc по умолчанию)
            # QTimer используется, чтобы дать время виджету перейти в fullscreen
            QTimer.singleShot(0, self.video_widget.setFocus)
            logger.debug("Focus set to video_widget for fullscreen.")
        else:
            # При выходе из fullscreen возвращаем фокус на MediaView
            # чтобы он снова мог обрабатывать клавиши громкости и т.д.
            QTimer.singleShot(0, self.setFocus)
            logger.debug("Focus set back to MediaView after exiting fullscreen.")

    # !!! НОВЫЙ МЕТОД: Обработчик двойного клика на video_widget !!!
    def handle_video_widget_double_click(self, event: QMouseEvent):
        """Обрабатывает двойной щелчок мыши на QVideoWidget."""
        if event.button() == Qt.MouseButton.LeftButton:
             logger.debug("Left double-click detected on video widget.")
             self.toggle_fullscreen()
             event.accept() # Сообщаем, что событие обработано
        else:
             event.ignore() # Игнорируем другие кнопки мыши

    def keyPressEvent(self, event: QKeyEvent):
        """Обрабатывает нажатия клавиш."""
        if event.key() == Qt.Key.Key_Plus:  # Увеличить громкость
            self.set_volume(+ 0.05)
        elif event.key() == Qt.Key.Key_Minus:  # Уменьшить громкость
            self.set_volume(- 0.05)
        else:
            super().keyPressEvent(event)