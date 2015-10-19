# -*- coding: utf-8 -*-
# This Class contains all the UI/View definitions
# that are going to be used during the work of the app.

class View(object):

    def __init__(self):
        # font definitions
        self.font_name = "David"
        self.label_font_size = 18
        self.header_font_size = 20

        self.decoding = "utf-8"

        # Hebrew strings
        self.h_username = 'שם משתמש '
        self.h_password = 'סיסמא '
        self.h_error_msg = 'הודעת שגיאה '
        self.h_login = 'התחבר '
        self.h_identification_window = 'חלון הזדהות '
        self.h_initial_register = 'רישום ראשוני '
        self.h_close_popup = 'סגור חלון התראה '
