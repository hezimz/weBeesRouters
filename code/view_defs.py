# -*- coding: utf-8 -*-
# this file contains globals for the view part
# meaning GUI dimensions, colors, fonts, hebrew strings etc
import logging
from PyQt4.QtGui import QFont, QPalette
from PyQt4.QtCore import *

# Functions
def d(str2decode):
    """
    Function will decode string according to chosen decoding from general_defs

    :return: decoded string
    """

    return str2decode.decode(general_defs['_decoding'])

# general 
general_defs = dict()
general_defs['_font'] = "David"
general_defs['_decoding'] = "utf-8"
general_defs['popup_window_min_width'] = 400
general_defs['_logging_level'] = logging.INFO
general_defs['_logo_small'] = "WeBees Logo - small.png"
general_defs['icon'] = "WebeesIcon.ico"
general_defs['label_font_size'] = 18
general_defs['header_font_size'] = 20
general_defs['button_font_size'] = 20
general_defs['logoH'] = 200
general_defs['logoW'] = 400

# Authentication GUI
auth_defs = dict()
auth_defs['h_auth_header'] = d('מסך התחברות:')
auth_defs['h_username'] = d('שם משתמש ')
auth_defs['h_password'] = d('סיסמא ')
auth_defs['h_error_msg'] = d('הודעת שגיאה ')
auth_defs['h_login'] = d('התחבר ')
auth_defs['h_identification_window'] = d('חלון הזדהות ')
auth_defs['en_identification_window'] = d("login")
auth_defs['h_close_popup'] = d('סגור חלון התראה ')
auth_defs['label_font'] = general_defs['_font']
auth_defs['en_support'] = d("Contact Us: Support @WeBees.co.il")


# Register Gui
reg_defs = dict()
reg_defs['h_r_type'] = d('סוג ראוטר')
reg_defs['h_buss_det'] = d('פרטי העסק: ')

#Qt Visual definitions
qt_v_defs = dict()
qt_v_defs['qt_label_font'] = QFont(general_defs['_font'], general_defs['label_font_size'])
qt_v_defs['qt_button_font'] = QFont(general_defs['_font'], general_defs['button_font_size'])
qt_v_defs['qt_header_font'] = QFont(general_defs['_font'], general_defs['header_font_size'], QFont.Bold)
qt_v_defs['align_r'] = Qt.AlignRight
qt_v_defs['align_l'] = Qt.AlignLeft


# Register GUI
regsiter_defs = dict()
regsiter_defs['h_initial_register'] = 'רישום ראשוני '

# Routine GUI
routine_defs = dict()


