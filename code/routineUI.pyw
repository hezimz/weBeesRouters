# -*- coding: utf-8 -*-
# from paramsCls import ParamsLoader
# from ipv4Cls import Ipv4
# from recognizeCls import Recognize
# from routerCls import Router
from PyQt4.QtGui import *
import sys

from routineCls import RoutineForm


# Load Routine Form
app = QApplication(sys.argv)
form = RoutineForm()
#form.setFixedSize(400,150)
form.setWindowTitle('שגרה'.decode('utf-8'))
form.show()
app.exec_()
