import sys
from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon

import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class CustomStopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.resize(350, 250)
        self.setWindowIcon(QIcon(resource_path("Stopwatch.ico")))

        self.elapsed_time = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        self.drag_position = QPoint()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        self.background_widget = QWidget()
        self.background_widget.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                border-radius: 10px;
            }
        """)
        bg_layout = QVBoxLayout(self.background_widget)
        bg_layout.setContentsMargins(0, 0, 0, 0)

        self.title_bar = QWidget()
        self.title_bar.setFixedHeight(35)
        self.title_bar.setStyleSheet("""
            QWidget {
                background-color: #242424;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
        """)
        title_layout = QHBoxLayout(self.title_bar)
        title_layout.setContentsMargins(10, 0, 0, 0)

        title_label = QLabel(" ⏱  Секундомер")
        title_label.setStyleSheet("color: #CCCCCC; font-weight: bold; font-size: 13px; font-family: 'Segoe UI';")
        title_layout.addWidget(title_label)
        title_layout.addStretch()

        btn_minimize = QPushButton("—")
        btn_minimize.setFixedSize(35, 35)
        btn_minimize.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #333333;
            }
        """)
        btn_minimize.clicked.connect(self.showMinimized)
        title_layout.addWidget(btn_minimize)

        btn_close = QPushButton("✕")
        btn_close.setFixedSize(35, 35)
        btn_close.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                border-top-right-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #E81123;
            }
        """)
        btn_close.clicked.connect(self.close)
        title_layout.addWidget(btn_close)

        bg_layout.addWidget(self.title_bar)

        self.time_label = QLabel("00:00:00.00")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("color: white; font-size: 36px; font-weight: bold; font-family: 'Consolas';")
        bg_layout.addWidget(self.time_label, stretch=1)

        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(20, 0, 20, 20)

        self.btn_start = QPushButton("Старт")
        self.btn_start.setFixedHeight(35)
        self.btn_start.setStyleSheet("""
            QPushButton {
                background-color: #1F538D;
                color: white;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #14375E;
            }
        """)
        self.btn_start.clicked.connect(self.toggle_start)
        btn_layout.addWidget(self.btn_start)

        self.btn_reset = QPushButton("Сброс")
        self.btn_reset.setFixedHeight(35)
        self.btn_reset.setStyleSheet("""
            QPushButton {
                background-color: #D32F2F;
                color: white;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #9A0007;
            }
        """)
        self.btn_reset.clicked.connect(self.reset)
        btn_layout.addWidget(self.btn_reset)

        bg_layout.addLayout(btn_layout)
        main_layout.addWidget(self.background_widget)
        self.setLayout(main_layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and event.position().y() <= 35:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and not self.drag_position.isNull():
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_position = QPoint()

    def toggle_start(self):
        if not self.timer.isActive():
            self.timer.start(10)
            self.btn_start.setText("Пауза")
            self.btn_start.setStyleSheet("""
                QPushButton {
                    background-color: #E65100;
                    color: white;
                    border-radius: 6px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #B23C00;
                }
            """)
        else:
            self.timer.stop()
            self.btn_start.setText("Старт")
            self.btn_start.setStyleSheet("""
                QPushButton {
                    background-color: #1F538D;
                    color: white;
                    border-radius: 6px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #14375E;
                }
            """)

    def reset(self):
        self.timer.stop()
        self.elapsed_time = 0
        self.time_label.setText("00:00:00.00")
        self.btn_start.setText("Старт")
        self.btn_start.setStyleSheet("""
            QPushButton {
                background-color: #1F538D;
                color: white;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #14375E;
            }
        """)

    def update_time(self):
        self.elapsed_time += 10
        ms = (self.elapsed_time % 1000) // 10
        seconds = (self.elapsed_time // 1000) % 60
        minutes = (self.elapsed_time // (1000 * 60)) % 60
        hours = (self.elapsed_time // (1000 * 60 * 60))

        self.time_label.setText(f"{hours:02}:{minutes:02}:{seconds:02}.{ms:02}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomStopwatch()
    window.show()
    sys.exit(app.exec())