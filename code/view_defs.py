# -*- coding: utf-8 -*-
# this file contains globals for the view part
# meaning GUI dimensions, colors, fonts, hebrew strings etc
import logging
from PyQt4.QtGui import QFont, QPalette
from PyQt4 import Qt
from PyQt4.QtCore import *

# general 
general_defs = dict()
general_defs['_font'] = "David"
general_defs['_decoding'] = "utf-8"
general_defs['popup_window_min_width'] = 400
general_defs['_logging_level'] = logging.INFO
general_defs['_logo_small'] = "WeBees Logo - small.png"
# Authentication GUI
auth_defs = dict()
auth_defs['h_auth_header'] = 'מסך התחברות:'
auth_defs['h_username'] = 'שם משתמש '
auth_defs['h_password'] = 'סיסמא '
auth_defs['h_error_msg'] = 'הודעת שגיאה '
auth_defs['h_login'] = 'התחבר '
auth_defs['h_identification_window'] = 'חלון הזדהות '
auth_defs['en_identification_window'] = "login"
auth_defs['h_close_popup'] = 'סגור חלון התראה '
auth_defs['label_font'] = general_defs['_font']
auth_defs['label_font_size'] = 18
auth_defs['header_font_size'] = 20
auth_defs['en_support'] = "Contact Us: Support @WeBees.co.il"
auth_defs['logoH'] = 200
auth_defs['logoW'] = 400

#Qt Visual definitions
qt_v_defs = dict()
qt_v_defs['qt_label_font'] = QFont(auth_defs['label_font'], auth_defs['label_font_size'])
qt_v_defs['qt_header_font'] = QFont(auth_defs['label_font'], auth_defs['header_font_size'], QFont.Bold)
qt_v_defs['align_r'] = Qt.AlignRight
qt_v_defs['align_l'] = Qt.AlignLeft
qt_v_defs['palette'] = QPalette()
qt_v_defs['palette'].setColor(QPalette.Foreground, Qt.darkBlue)


# Register GUI
regsiter_defs = dict()
regsiter_defs['h_initial_register'] = 'רישום ראשוני '

# Routine GUI
routine_defs = dict()
