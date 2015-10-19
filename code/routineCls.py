# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from time import sleep

from routerCls import Router


class RoutineForm(QDialog, Router):
    def __init__(self):
        super(RoutineForm, self).__init__()
        Router.__init__(self)
        self.routerInst = ""


        # 1'st Headline Label
        lbl1 = QLabel(self.r_name)
        # 2'nd Headline Label
        lbl2 = QLabel("בחר את הכפתור המתאים".decode('utf-8'))
        # reset btn
        self.reset_btn = QPushButton("אתחול ראוטר".decode('utf-8'))
        # restore btn
        self.restore_btn = QPushButton("שחזור הגדרות".decode('utf-8'))
        # backup btn
        self.backup_btn = QPushButton("שמירת הגדרות".decode('utf-8'))
        # Quit btn
        self.quit_btn = QPushButton("יציאה".decode('utf-8'))

        # set the widgets on the layout
        grid = QGridLayout()
        grid.addWidget(lbl1, 0, 0)
        grid.addWidget(lbl2, 1, 0)
        v_box = QHBoxLayout()
        grid.addLayout(v_box, 2, 0)
        v_box.addWidget(self.reset_btn)
        v_box.addWidget(self.restore_btn)
        v_box.addWidget(self.backup_btn)
        grid.addWidget(self.quit_btn, 3, 0)
        self.setLayout(grid)

        self.connect(self.backup_btn, SIGNAL("clicked ()"), self.run_backup)
        self.connect(self.restore_btn, SIGNAL("clicked()"), self.run_restore)
        self.connect(self.reset_btn, SIGNAL("clicked()"), self.run_reset)
        self.connect(self.quit_btn, SIGNAL("clicked()"), self.accept)

    def run_backup(self):
        if not self.ready:
            self.routerInst = self.prepare_for_use()

        self.routerInst.set_selenium_driver()
        self.routerInst.backup()
        sleep(2)
        self.routerInst.driver.quit()

    def run_restore(self):
        if not self.ready:
            self.routerInst = self.prepare_for_use()

        self.routerInst.set_selenium_driver()
        self.routerInst.restore()
        sleep(2)
        self.routerInst.driver.quit()

    def run_reset(self):
        if not self.ready:
            self.routerInst = self.prepare_for_use()

        self.routerInst.set_selenium_driver()
        self.routerInst.reset()
        sleep(2)
        self.routerInst.driver.quit()
