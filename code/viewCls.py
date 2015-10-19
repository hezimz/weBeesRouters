# -*- coding: utf-8 -*-
# This Class contains all the UI/View definitions
# that are going to be used during the work of the app.
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import Qt


class View(QDialog):

    def __init__(self):
        super(View, self).__init__()
        self.setLayoutDirection(Qt.RightToLeft)
