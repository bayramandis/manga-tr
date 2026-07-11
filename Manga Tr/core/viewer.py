from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QFileDialog,
    QWidget,
    QVBoxLayout,
    QScrollArea,
)

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class MangaViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MangaTR v0.2")
        self.resize(1000, 700)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        self.scroll = QScrollArea()
        self.scroll.setWidget(self.label)
        self.scroll.setWidgetResizable(True)

        self.button = QPushButton("📂 Resim Aç")
        self.button.clicked.connect(self.open_image)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.scroll)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Resim Seç",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.webp)"
        )

        if file_name:
            pixmap = QPixmap(file_name)
            self.label.setPixmap(pixmap)
            self.label.resize(pixmap.size())