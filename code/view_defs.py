# -*- coding: utf-8 -*-
# this file contains globals for the view part
# meaning GUI dimensions, colors, fonts, hebrew strings etc
import logging

# general 
general_defs = dict()
general_defs['_font'] = "David"
general_defs['_decoding'] = "utf-8"
general_defs['popup_window_min_width'] = 400
general_defs['_logging_level'] = logging.INFO

# Authentication GUI
auth_defs = dict()
auth_defs['h_username'] = 'שם משתמש '
auth_defs['h_password'] = 'סיסמא '
auth_defs['h_error_msg'] = 'הודעת שגיאה '
auth_defs['h_login'] = 'התחבר '
auth_defs['h_identification_window'] = 'חלון הזדהות '
auth_defs['h_close_popup'] = 'סגור חלון התראה '
auth_defs['label_font'] = general_defs['_font']
auth_defs['label_font_size'] = 18
auth_defs['header_font_size'] = 20

# Register GUI
regsiter_defs = dict()
regsiter_defs['h_initial_register'] = 'רישום ראשוני '

# Routine GUI
routine_defs = dict()
