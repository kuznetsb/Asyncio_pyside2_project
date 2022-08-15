import asyncio
from PySide2 import QtWidgets, QtGui

import server  # DON`T REMOVE
import image



def client():
    path_to_image = "image"
    with open(path_to_image, "wb") as file:
        file.write(asyncio.run(image.connect()))
    return path_to_image


def main():
    path = client()
    app = QtWidgets.QApplication([])
    label = QtWidgets.QLabel()
    label.setMinimumSize(100, 100)
    label.setPixmap(QtGui.QPixmap(path))
    label.show()
    app.exec_()


if __name__ == '__main__':
    main()
