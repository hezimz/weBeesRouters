# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import logging

from sqlCls import SqlFunctions
from view_defs import auth_defs, general_defs

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=general_defs['_logging_level'])


class MyPopupDialog(QDialog):
    def __init__(self, error_msg):
        super(MyPopupDialog, self).__init__()
        self.setLayoutDirection(Qt.RightToLeft)
        logging.error(error_msg)
        err_label = QLabel(error_msg)
        self.close_btn = QPushButton(auth_defs['h_close_popup'].decode(general_defs['_decoding']))
        self.setWindowTitle(auth_defs['h_error_msg'].decode(general_defs['_decoding']))
        self.setMinimumWidth(general_defs['popup_window_min_width'])
        grid = QGridLayout()
        grid.addWidget(err_label)
        grid.addWidget(self.close_btn)
        self.setLayout(grid)
        # set button event handler
        self.connect(self.close_btn, SIGNAL("clicked ()"), self.close_popup)

    def close_popup(self):
        self.accept()


class AuthForm(QDialog, SqlFunctions):

    # err_msgs_inst is a ErrorMsgs instance
    # with which i can pull any type of
    # error message that is written in the program XML
    # according to its type (authentication ,license,...)
    def __init__(self, err_msgs_inst):
        super(AuthForm, self).__init__()
        SqlFunctions.__init__(self)
        self._err_msgs_inst = err_msgs_inst
        self.setLayoutDirection(Qt.RightToLeft)
        self._uName = ""
        self._uNameIndex = "NA"
        # Gui layout
        label_font = QFont(auth_defs['label_font'], auth_defs['label_font_size'])
        header_font = QFont(auth_defs['label_font'], auth_defs['header_font_size'], QFont.Bold)
        align_r = Qt.AlignRight
        palette = QPalette()
        palette.setColor(QPalette.Foreground, Qt.darkBlue)

        # username
        u_label = QLabel(auth_defs['h_username'].decode(general_defs['_decoding']))
        u_label.setFont(label_font)

        # password
        p_label = QLabel(auth_defs['h_password'].decode(general_defs['_decoding']))
        p_label.setFont(label_font)

        # just for testing i can set the values for the user
        self.u_value = QLineEdit('BeeComm')
        self.p_value = QLineEdit('beecomm13')
        # self.u_value = QLineEdit('Retalix')
        # self.p_value = QLineEdit('Retalix1')

        # button for authentication
        self.auth_btn = QPushButton(auth_defs['h_login'].decode(general_defs['_decoding']))

        # set the widgets on the layout
        grid = QGridLayout()  # create grid Object
        grid.addWidget(u_label, 0, 0, align_r)  # add username label to grid
        grid.addWidget(self.u_value, 0, 1, align_r)  # add username textbox to grid

        grid.addWidget(p_label, 1, 0, align_r)  # add password label to grid
        grid.addWidget(self.p_value, 1, 1, align_r)  # add password textbox to grid

        grid.addWidget(self.auth_btn, 2, 4, align_r)  # add login button to the grid

        self.setLayout(grid)  # "close" grid

        # set the login button event handler
        self.connect(self.auth_btn, SIGNAL("clicked ()"), self.authenticate)

    def authenticate(self):
        # a method for handling the login button click event
        _username = self.u_value.text()
        _password = self.p_value.text()
        # if its ok data is username
        # if not ,data is an error msg to pass to popup window
        __auth_result, data = self.getUserId(unicode(_username), unicode(_password))
        if __auth_result == "err":
            _dialog = MyPopupDialog(self._err_msgs_inst.get_error_msg("Authentication"))
            _dialog.exec_()
        else:
            self.set_u_name(data)
            self.set_u_name_index(__auth_result)
            self.accept()

    def get_u_name(self):
        return self._uName

    def set_u_name(self, val):
        self._uName = val

    def get_u_name_index(self):
        return self._uNameIndex

    def set_u_name_index(self, val):
        self._uNameIndex = val