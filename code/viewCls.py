# -*- coding: utf-8 -*-
# This Class contains all the UI/View definitions
# that are going to be used during the work of the app.
from PyQt4.QtGui import QDialog, QPalette, QFont, QLabel, QComboBox, \
    QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QPainter, QColor
from PyQt4.QtCore import Qt

from view_defs import general_defs, reg_defs


class View(QDialog):

    def __init__(self):
        super(View, self).__init__()
        self.setLayoutDirection(Qt.RightToLeft)

        self.palette = QPalette()
        self.palette.setColor(QPalette.Foreground, Qt.darkBlue)

        self.label_font = QFont(general_defs['_font'], general_defs['label_font_size'])
        self.button_font = QFont(general_defs['_font'], general_defs['button_font_size'])
        self.header_font = QFont(general_defs['_font'], general_defs['header_font_size'], QFont.Bold)

        self.painter = QPainter()


    def create_qlabel(self, string2Label):
        qlbl = QLabel(string2Label)
        qlbl.setFont(self.label_font)
        qlbl.setAlignment(Qt.AlignRight)
        if string2Label == "." : qlbl.setFixedWidth(15)
        return qlbl

    def create_combobox(self):
        comboboxMinWidth = 200
        cb = QComboBox()
        cb.setMinimumWidth(comboboxMinWidth)
        return cb

    def create_octet(self):
        octet = QLineEdit()
        octet.setMaxLength(3)
        octet.setMaximumWidth(30)
        octet.setPlaceholderText('0')
        return octet

    def create_button(self, buttonLabel):
        b = QPushButton(buttonLabel)
        b.setFont(self.button_font)
        return b

    def create_ip_style_group(self, groupName):

        group = dict()
        group['name'] = self.create_qlabel(groupName)
        group['octet1'] = self.create_octet()
        group['octet2'] = self.create_octet()
        group['octet3'] = self.create_octet()
        group['octet4'] = self.create_octet()

        group['dotLbl1'] = self.create_qlabel(reg_defs['dot'])
        group['dotLbl2'] = self.create_qlabel(reg_defs['dot'])
        group['dotLbl3'] = self.create_qlabel(reg_defs['dot'])

        group['grid'] = QGridLayout()
        name_h_box = QHBoxLayout()
        h_box = QHBoxLayout()

        group['grid'].addLayout(name_h_box, 0, 0)
        group['grid'].addLayout(h_box, 0, 1)

        name_h_box.addWidget(group['name'])
        h_box.addWidget(group['octet1'])
        h_box.addWidget(group['dotLbl1'])
        h_box.addWidget(group['octet2'])
        h_box.addWidget(group['dotLbl2'])
        h_box.addWidget(group['octet3'])
        h_box.addWidget(group['dotLbl3'])
        h_box.addWidget(group['octet4'])

        return group['grid']

    def line(self, x1, y1, x2, y2):
        self.painter.begin(self)
        qcolor = QColor()
        self.painter.setPen(qcolor.red())
        print self.painter.pen()
        self.painter.drawLine(x1, y1, x2, y2)

        self.painter.end()
