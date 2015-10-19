
from PyQt4.QtGui import QIcon, QPixmap
from view_defs import general_defs


def get_qicon(icon_file):
    qicon = QIcon()
    qicon.addPixmap(QPixmap(icon_file))
    return qicon

