from PyQt4.QtGui import QIcon, QPixmap, QApplication, QStyleFactory
from PyQt4.QtCore import Qt
from PySide import QtGui
from PySide.QtGui import QWindowsStyle, QPlastiqueStyle, QCleanlooksStyle, QMotifStyle, QPalette, QColor
from view_defs import general_defs

def get_qicon(icon_file):
    qicon = QtGui.QIcon()
    qicon.addPixmap(QtGui.QPixmap(icon_file))
    return qicon


def get_scaled_pixmap(logo_file):
    my_pixmap = QPixmap(logo_file)
    my_scaled_pixmap = my_pixmap.scaled(general_defs['logoH'], general_defs['logoW'], Qt.KeepAspectRatio)
    return my_scaled_pixmap


def create_app(arguments):

    app = QtGui.QApplication(arguments)
    p = QPalette()
    p.setColor(QPalette.Window, QColor("#DDDDDD"))
    app.setPalette(p)

    app.setStyle(QtGui.QStyleFactory.create('gtk'))
    app.setWindowIcon(get_qicon(general_defs['icon']))

    return app
