# -*- coding: utf-8 -*-
# This Class contains all the UI/View definitions
# that are going to be used during the work of the app.
from PyQt4.QtGui import QDialog, QPalette, QFont
from PyQt4.QtCore import Qt

from view_defs import general_defs

class View(QDialog):

    def __init__(self):
        super(View, self).__init__()
        self.setLayoutDirection(Qt.RightToLeft)

        self.palette = QPalette()
        self.palette.setColor(QPalette.Foreground, Qt.darkBlue)

        self.label_font = QFont(general_defs['_font'], general_defs['label_font_size'])
        self.button_font = QFont(general_defs['_font'], general_defs['button_font_size'])
        self.header_font = QFont(general_defs['_font'], general_defs['header_font_size'], QFont.Bold)
