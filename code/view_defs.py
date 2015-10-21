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
general_defs['ver'] = d('גרסה 1.0')
general_defs['_font'] = "David"
general_defs['_decoding'] = "utf-8"
general_defs['popup_window_min_width'] = 400
general_defs['_logging_level'] = logging.INFO
general_defs['_logo_small'] = "WeBees Logo - small.png"
general_defs['icon'] = "WebeesIcon.ico"
general_defs['label_font_size'] = 16
general_defs['header_font_size'] = 20
general_defs['button_font_size'] = 20
general_defs['support_font_size'] = 10
general_defs['logoH'] = 200
general_defs['logoW'] = 400
general_defs['en_support'] = d("Contact Us: Support @WeBees.co.il")

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
reg_defs['h_choose_cust'] = d('בחירת לקוח: ') # Customer
reg_defs['h_choose_fr'] = d('בחירת רשת: ') # frenchise
reg_defs['h_choose_br'] = d('בחירת סניף: ') # branch
reg_defs['h_choose_ip_grp'] = d('כתובת IP חיצוני (WAN):') # choose ip - group widget
reg_defs['h_local_ip_grp'] = d('כתובת IP מקומי (LAN):')  # choose ip - group widget
reg_defs['h_subnet_mask_grp'] = d('מסכת רשת(Subnet Mask):')  # choose ip - group widget
reg_defs['h_default_gateway_grp'] = d('כתובת הנתב (DG):')  # choose ip - group widget
reg_defs['h_pref_dns_grp'] = d('כתובת DNS ראשי: ')  # choose ip - group widget
reg_defs['h_alt_dns_grp'] = d('כתובת DNS משני: ')  # choose ip - group widget
reg_defs['dot'] = d('.') # a dot between the ip octets
reg_defs['h_geo_label'] = d('אזור גאוגרפי: ') # choose the geographic location
reg_defs['h_register_btn'] = d(' התקנה ')
reg_defs['h_exit_btn'] = d(' יציאה ')
reg_defs['h_initial_register_window'] = d('רישום ראשוני ')
reg_defs['h_network_card_info'] = d('מידע מכרטיס הרשת:')

#Qt Visual definitions
qt_v_defs = dict()
qt_v_defs['qt_label_font'] = QFont(general_defs['_font'], general_defs['label_font_size'])
qt_v_defs['qt_button_font'] = QFont(general_defs['_font'], general_defs['button_font_size'])
qt_v_defs['qt_header_font'] = QFont(general_defs['_font'], general_defs['header_font_size'], QFont.Bold)
qt_v_defs['align_r'] = Qt.AlignRight
qt_v_defs['align_l'] = Qt.AlignLeft


# Routine GUI
routine_defs = dict()


