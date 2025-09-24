# Содержимое файла: smeller/mediacenter/integrated_player.py

import sys
from pathlib import Path
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QPushButton, QHBoxLayout, QLabel,
                             QFileDialog, QSplitter)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal

from smeller.gui.mediacenter.aromablock_timeline_widget import AromaBlockTimelineWidget, DraggableAromaBlockItem
from smeller.gui.mediacenter.media_view import MediaView
from smeller.models.aroma_block import AromaBlock
            
class IntegratedPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Integrated Aroma Player")

        # --- Central Widget and Layout ---
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)

        # --- Splitter for resizable layout ---
        self.splitter = QSplitter(Qt.Orientation.Vertical)
        self.main_layout.addWidget(self.splitter)

        # --- 1. Media View ---
        self.media_view = MediaView()
        self.splitter.addWidget(self.media_view)

        # --- 2. AromaBlock Timeline ---
        self.timeline_widget = AromaBlockTimelineWidget(
            block_height=50,
            time_scale_pixels_per_sec=10,  # Adjust as needed
            zoom_level=1.0,
        )
        
        self.splitter.addWidget(self.timeline_widget)

        # --- Signals and Slots Connection ---
        self.timeline_widget.play_pause_signal.connect(self.toggle_play_pause)
        self.timeline_widget.stop_signal.connect(self.stop_playback)
        self.timeline_widget.block_time_changed.connect(self.handle_block_time_changed)  # Если нужно реагировать

        # --- Timer for Playback ---
        self.playback_timer = QTimer(self)
        self.playback_timer.setInterval(25)  # Update every 50 milliseconds (adjust as needed)
        self.playback_timer.timeout.connect(self.update_playback_time)
        self.current_time = 0  # Current playback time in seconds
        # --- Simulate Movie and Aroma Blocks ---
        self.simulate_movie_and_blocks()


    def simulate_movie_and_blocks(self):
        # 1. Simulate movie loading (2 minutes 30 seconds = 150 seconds)
        movie_duration = 3000.0
        self.media_view.load_media("Simulated Movie.mp4")  # Placeholder
        self.media_view.set_stop_time(movie_duration)
        #self.timeline_widget.set_timeline_range(0, movie_duration)

        # 2. Add some aroma blocks (for demonstration)
        block1 = AromaBlock(id=1, start_time=10.0, stop_time=20.0, name="Block 1")
        block2 = AromaBlock(id=2, start_time=50.0, stop_time=70.0, name="Block 2")
        block3 = AromaBlock(id=3, start_time=100.0, stop_time=130.0, name="Block 3")

        self.timeline_widget.add_aroma_block_item(block1, 0)  # Add to track 0
        self.timeline_widget.add_aroma_block_item(block2, 0)  # Add to track 0
        self.timeline_widget.add_aroma_block_item(block3, 1)  # Add to track 1

    def toggle_play_pause(self):
        if self.playback_timer.isActive():
            self.pause_playback()
        else:
            self.start_playback()

    def start_playback(self):
        if self.current_time >= self.media_view.get_stop_time():
            self.current_time = 0  # Reset if at the end

        self.playback_timer.start()
        self.media_view.play() #  Update the button in MediaView
        print(f"Playback started. Current time: {self.current_time}")

    def pause_playback(self):
        self.playback_timer.stop()
        self.media_view.pause()  #  Update the button in MediaView
        print(f"Playback paused. Current time: {self.current_time}")


    def stop_playback(self):
        self.playback_timer.stop()
        self.current_time = 0
        self.timeline_widget.update_time_indicator(self.current_time)
        self.media_view.stop() #  Update the button and state in MediaView
        print("Playback stopped and reset.")


    def update_playback_time(self):
        self.current_time += self.playback_timer.interval() / 1000.0  # Convert ms to seconds

        if self.current_time > self.media_view.get_stop_time():
            self.stop_playback()  # Stop automatically when movie ends
            return

        self.timeline_widget.update_time_indicator(self.current_time)
        # print(f"Current playback time: {self.current_time:.2f}") # Too much output, uncomment for debugging if necessary.


    def handle_block_time_changed(self, block_id: int, new_start_time: float, new_stop_time: float):
        #  Example implementation (adjust as needed)
        print(f"Block {block_id} time changed: Start={new_start_time}, Stop={new_stop_time}")
        #  You can update the AromaBlock object here if needed.
        #  Find the block and call methods to change start/stop time.

    def closeEvent(self, event):
        """Handle cleanup on window close"""
        self.playback_timer.stop()  # Make sure to stop the timer
        super().closeEvent(event)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    player = IntegratedPlayer()
    player.show()

    sys.exit(app.exec())