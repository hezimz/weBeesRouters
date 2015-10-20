from PyQt4.QtGui import QIcon, QPixmap
from PyQt4.QtCore import Qt
from view_defs import general_defs

def get_qicon(icon_file):
    qicon = QIcon()
    qicon.addPixmap(QPixmap(icon_file))
    return qicon

def get_scaled_pixmap(logo_file):
    my_pixmap = QPixmap(logo_file)
    my_scaled_pixmap = my_pixmap.scaled(general_defs['logoH'], general_defs['logoW'], Qt.KeepAspectRatio)
    return my_scaled_pixmap
