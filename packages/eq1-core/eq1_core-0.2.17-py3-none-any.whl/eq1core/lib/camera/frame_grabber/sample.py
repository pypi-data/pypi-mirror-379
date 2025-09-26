import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from eq1core.lib.camera.frame_grabber.worker import ImageGrabber
from eq1core.dto import CameraDTO


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(787, 632)
        self.lbl_window = QtWidgets.QLabel(Form)
        self.lbl_window.setGeometry(QtCore.QRect(20, 110, 531, 441))
        self.lbl_window.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_window.setText("")
        self.lbl_window.setObjectName("lbl_window")
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setText("Exit")
        self.btn_exit.setStyleSheet("background-color: red")
        self.btn_exit.setGeometry(QtCore.QRect(600, 110, 161, 51))
        self.btn_exit.clicked.connect(
            lambda: sys.exit()
        )


if __name__ == "__main__":
    import cv2
    import numpy as np
    from PyQt5.QtGui import QImage, QPixmap

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    mainWindow.setFixedSize(787, 632)
    ui = Ui_Form()
    ui.setupUi(mainWindow)

    camera_dto = CameraDTO(
        name='x',
        camera_serial='DA5002685',
        grabber_serial='DA4991652',
    )

    def convert_numpy_to_qimage(image: np.ndarray) -> QImage:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image_rgb.shape
        bytes_per_line = 3 * width  # 3채널(RGB) 경우
        qimage = QImage(image_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

        return qimage

    def show_image(image: np.ndarray):
        qimage = convert_numpy_to_qimage(image)
        ui.lbl_window.setPixmap(QPixmap.fromImage(qimage))

    grabber = ImageGrabber(camera_dto)
    grabber.connect()
    grabber.set_grab_callback_fn(show_image)
    grabber.start()

    mainWindow.show()
    app.exec_()

    sys.exit()
