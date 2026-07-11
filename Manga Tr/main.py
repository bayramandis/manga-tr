import sys

from PySide6.QtWidgets import QApplication

from core.viewer import MangaViewer


def main():
    app = QApplication(sys.argv)

    window = MangaViewer()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()