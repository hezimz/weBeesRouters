# -*- coding: utf-8 -*-
import logging
from PyQt4.QtGui import *
import sys

from generalFunctions import get_qicon
from manageXml import XmlParser
from errorMsgsCls import ErrorMsgs
from authCls import AuthFormCtrl, ViewAuthForm
from registerCls import RegisterForm
from view_defs import auth_defs, general_defs, regsiter_defs

# set Logging level
logging.basicConfig(format='-%(levelname)s- %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=general_defs['_logging_level'])

# just testing XML parsing Class
xml_parser = XmlParser()
xml_parser.set_xml_file("program.xml")
if not xml_parser.parse_xml():
    print "sdf"
    sys.exit(1)
err_msgs_inst = ErrorMsgs(xml_parser.get_error_element())

# Load Authentication Form
logging.info("Loading authentication form")
app = QApplication(sys.argv)

auth_form = AuthFormCtrl(err_msgs_inst)
auth_form.setWindowTitle(auth_defs['en_identification_window'].decode(general_defs['_decoding']))
auth_form.setWindowIcon(get_qicon(general_defs['icon']))
auth_form.setFixedSize(500, 150)
auth_form.show()
app.exec_()


if auth_form.get_u_name_index() == "NA":  # this is basically the same as userID that i defined in sql Class
    app.exit(1)
    sys.exit(1)
# load Registration Form with the user name we got
logging.info("Loading registration form")
reg_form = RegisterForm(auth_form.get_u_name_index())
# reg_form.setFixedSize(650,300)
reg_form.setWindowTitle(regsiter_defs['h_initial_register'].decode(general_defs['_decoding']))
reg_form.show()
app.exec_()
logging.info("Exit app")
