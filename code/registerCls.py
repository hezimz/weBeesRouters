# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from sqlCls import SqlFunctions
from recognizeCls import Recognize
from userCls import User

from viewCls import View
from view_defs import reg_defs, general_defs
from generalFunctions import get_scaled_pixmap

class ViewRegisterForm(View):
    def __init__(self):
        super(ViewRegisterForm, self).__init__()
        View.__init__(self)
        # router type
        r_label = self.create_qlabel(reg_defs['h_r_type'])
        #r_name = self.rName()
        self.r_value_label = self.create_qlabel("") # self.r_name comes from Recognize -> Router
        self.r_value_label.setMaximumHeight(30)
        self.r_value_label.setFrameShape(QFrame.Panel)
        self.r_value_label.setFrameShadow(QFrame.Sunken)

        # business details Header
        bd_label = self.create_qlabel(reg_defs['h_buss_det'], 'header')
        # bd_label = QLabel(reg_defs['h_buss_det'])
        # bd_label.setFont(self.header_font)
        # bd_label.setFrameStyle(QFrame.Sunken)
        # bd_label.setPalette(self.palette)

        # webees image
        img_label = QLabel()
        img_label.setPixmap(get_scaled_pixmap(general_defs['_logo_small']))

        # customer choosing ( Beecomm, Retalix)
        cu_label = self.create_qlabel(reg_defs['h_choose_cust'])
        self.cu_combobox = self.create_combobox()
        ####################
        # move to controller
        ####################
        # self.customersDict = self.getCustomerList()
        # self.cu_combobox.addItems(sorted(self.customersDict.keys()))

        # franchise name ( rami levy ,...)
        fr_label = self.create_qlabel(reg_defs['h_choose_fr'])
        self.fr_combobox = self.create_combobox()
        ####################
        # move to controller
        ####################
        #self.franchiseDict = self.getFranchisesList(self.customersDict[unicode(self.cu_combobox.currentText())])
        #self.fr_combobox.addItems(sorted(self.franchiseDict.keys()))
        #self.alighCombobox(self.fr_combobox)

        # branch choosing ( natanya ,rosh ha-ayn..)
        br_label = self.create_qlabel(reg_defs['h_choose_br'])
        self.br_combobox = self.create_combobox()
        ####################
        # move to controller
        ####################
        #self.branchDict = self.getBranchList(self.franchiseDict[unicode(self.fr_combobox.currentText())])
        #self.br_combobox.addItems(sorted(self.branchDict.keys()))
        #self.alighCombobox(self.br_combobox)

        # Background label to lay under the network details
        # i use two labels do defer between dns data and the rest
        bg_ip_label = self.create_label_as_bg()
        bg_dns_label = self.create_label_as_bg()

        # network card info header
        nc_label = self.create_qlabel(reg_defs['h_network_card_info'], 'header')

        # External IP Group creator
        self.ext_ip_group = self.create_ip_style_group(reg_defs['h_choose_ip_grp'])
        self.ext_ip_grid = self.ext_ip_group['grid']
        self.ext_ip_group['octet3'].setPlaceholderText('192')
        self.ext_ip_group['octet4'].setPlaceholderText('168')
        # local IP group creator
        self.local_ip_group = self.create_ip_style_group(reg_defs['h_local_ip_grp'])
        self.local_ip_grid = self.local_ip_group['grid']
        # local Subnet Mask group creator
        self.subnet_mask_group = self.create_ip_style_group(reg_defs['h_subnet_mask_grp'])
        self.subnet_mask_grid = self.subnet_mask_group['grid']
        # default gateway group creator
        self.default_gateway_group = self.create_ip_style_group(reg_defs['h_default_gateway_grp'])
        self.default_gateway_grid = self.default_gateway_group['grid']
        # preferred DNS Server group creator
        self.pref_dns_group = self.create_ip_style_group(reg_defs['h_pref_dns_grp'])
        self.pref_dns_grid = self.pref_dns_group['grid']
        # Alternate DNS Server group creator
        self.alt_dns_group = self.create_ip_style_group(reg_defs['h_alt_dns_grp'])
        self.alt_dns_grid = self.alt_dns_group['grid']

        # Geographic location (north ,south, center)
        geo_label = self.create_qlabel(reg_defs['h_geo_label'])
        self.geo_combobox = self.create_combobox()
        ####################
        # move to controller
        ####################
        #self.zoneDict = self.getZoneList()
        #self.geo_combobox.addItems(sorted(self.zoneDict.keys()))
        #self.alighCombobox(self.geo_combobox)

        # Registr Button
        self.regBtn = self.create_button(reg_defs['h_register_btn'])

        # Exit Button
        self.exitBtn = self.create_button(reg_defs['h_exit_btn'] )

        ################################
        # set the widgets on the layout
        ################################
        self.grid = QGridLayout()
        local_ip_vbox = QVBoxLayout()
        dns_vbox = QVBoxLayout()

        self.grid.addWidget(r_label, 0, 0)
        self.grid.addWidget(self.r_value_label, 0, 1)

        self.grid.addWidget(img_label,0, 6)

        self.grid.addWidget(bd_label, 1, 0)

        self.grid.addWidget(cu_label, 2, 0)
        self.grid.addWidget(self.cu_combobox, 2, 1)

        self.grid.addWidget(fr_label, 3, 0)
        self.grid.addWidget(self.fr_combobox, 3, 1)

        self.grid.addWidget(br_label, 4, 0)
        self.grid.addWidget(self.br_combobox, 4, 1)

        # add external ip group to grid
        self.grid.addLayout(self.ext_ip_grid, 5, 0,1,2 )

        self.grid.addWidget(geo_label, 6, 0)
        self.grid.addWidget(self.geo_combobox, 6, 1)


        # add Network Card Data
        self.grid.addWidget(nc_label,7,0)
        local_ip_vbox.addLayout(self.local_ip_grid, 0 )
        local_ip_vbox.addLayout(self.subnet_mask_grid,1)
        local_ip_vbox.addLayout(self.default_gateway_grid,2)
        dns_vbox.addLayout(self.pref_dns_grid,3)
        dns_vbox.addLayout(self.alt_dns_grid,4)

        # grid.addWidget(bg_ip_label,8,0, 2, 3)
        self.grid.addLayout(local_ip_vbox,8,0, 1, 2)
        # grid.addWidget(bg_dns_label,9,0, 1, 2)
        self.grid.addLayout(dns_vbox,9,0, 1, 2)

        self.grid.addWidget(self.support_label, 10, 6)

        self.grid.addWidget(self.regBtn, 5, 6)
        self.grid.addWidget(self.exitBtn, 6, 6)
        self.setLayout(self.grid)


class CtrlRegisterForm(ViewRegisterForm, SqlFunctions, User):
    def __init__(self, user_id):
        super(CtrlRegisterForm, self).__init__()
        SqlFunctions.__init__(self)
        User.__init__(self)
        self.setUserId(user_id) # user_id is received from the auth form
        # self.r_value_label.setText(self.get_r_name())

    def get_r_name(self):
        recognizeInst = Recognize()
        r_name = recognizeInst.r_name
        return QString(r_name)


class RegisterForm(QDialog, SqlFunctions, User):
    def __init__(self, user_id):
        super(RegisterForm, self).__init__()
        SqlFunctions.__init__(self)
        User.__init__(self)
        self.setUserId(user_id) # user_id is received from the auth form
        self.get_r_name()
        # Gui layout
        self.setLayoutDirection(Qt.RightToLeft)
        #self.client = client
        #self.userID = userID
        # self.sqlInst = sqlInst


        label_font = QFont("David", 18)
        header_font = QFont("David", 20, QFont.Bold)
        register_btn_font = QFont("David", 20, QFont.Bold)
        alignR = Qt.AlignRight
        alignL = Qt.AlignLeft
        self.comboboxMinWidth = 180
        palette = QPalette()
        palette.setColor(QPalette.Foreground, Qt.darkBlue)
        #self.logoW = 400
        #self.logoH = 200
        # router type
        r_label = QLabel('סוג ראוטר '.decode('utf-8'))
        r_label.setFont(label_font)
        #r_name = self.rName()
        r_value = QLabel(self.r_name.upper()) # self.r_name comes from Recognize -> Router
        r_value.setMaximumHeight(30)
        r_value.setFrameShape(QFrame.Panel)
        r_value.setFrameShadow(QFrame.Sunken)

        # business details
        bd_label = QLabel('פרטי העסק: '.decode('utf-8'))
        bd_label.setFrameStyle(QFrame.Sunken)
        bd_label.setFont(header_font)
        bd_label.setPalette(palette)

        # webees image
        img_label = QLabel()
        #my_pixmap = QPixmap('WeBees Logo - small.png')
        #my_scaled_pixmap = my_pixmap.scaled(auth_defs['logoH'], auth_defs['logoW'], Qt.KeepAspectRatio)
        img_label.setPixmap(get_scaled_pixmap(general_defs['_logo_small']))

        # customer choosing ( Beecomm, Retalix)
        cu_label = QLabel('בחירת לקוח:'.decode('utf-8'))
        cu_label.setFont(label_font)
        self.cu_combobox = QComboBox()
        self.cu_combobox.setMinimumWidth(self.comboboxMinWidth)
        self.customersDict = self.getCustomerList()
        self.cu_combobox.addItems(sorted(self.customersDict.keys()))

        # franchise name ( rami levy ,...)
        fr_label = QLabel('בחירת רשת:'.decode('utf-8'))
        fr_label.setFont(label_font)
        self.fr_combobox = QComboBox()
        self.fr_combobox.setMinimumWidth(self.comboboxMinWidth)
        self.franchiseDict = self.getFranchisesList(self.customersDict[unicode(self.cu_combobox.currentText())])
        self.fr_combobox.addItems(sorted(self.franchiseDict.keys()))
        self.alighCombobox(self.fr_combobox)

        # branch choosing ( natanya ,rosh ha-ayn..)
        br_label = QLabel('בחירת סניף:'.decode('utf-8'))
        br_label.setFont(label_font)
        self.br_combobox = QComboBox()
        self.br_combobox.setMinimumWidth(self.comboboxMinWidth)
        self.branchDict = self.getBranchList(self.franchiseDict[unicode(self.fr_combobox.currentText())])
        self.br_combobox.addItems(sorted(self.branchDict.keys()))
        self.alighCombobox(self.br_combobox)

        # External IP
        eip_label = QLabel('בחירת IP:'.decode('utf-8'))
        eip_label.setFont(label_font)
        self.eip_1_octet = QLineEdit()
        self.eip_1_octet.setMaxLength(3)
        self.eip_1_octet.setMaximumWidth(30)
        self.eip_2_octet = QLineEdit()
        self.eip_2_octet.setMaxLength(3)
        self.eip_2_octet.setMaximumWidth(30)
        self.eip_3_octet = QLineEdit()
        self.eip_3_octet.setMaxLength(3)
        self.eip_3_octet.setMaximumWidth(30)
        self.eip_4_octet = QLineEdit()
        self.eip_4_octet.setMaxLength(3)
        self.eip_4_octet.setMaximumWidth(30)
        eip_dot_label_1 = QLabel('.'.decode('utf-8'))
        eip_dot_label_2 = QLabel('.'.decode('utf-8'))
        eip_dot_label_3 = QLabel('.'.decode('utf-8'))
        eip_dot_label_4 = QLabel('.'.decode('utf-8'))
        eip_dot_label_1.setFont(label_font)
        eip_dot_label_2.setFont(label_font)
        eip_dot_label_3.setFont(label_font)
        eip_dot_label_4.setFont(label_font)

        # Geographic location (north ,south, center)
        geo_label = QLabel('אזור גאוגרפי:'.decode('utf-8'))
        geo_label.setFont(label_font)
        self.geo_combobox = QComboBox()
        self.geo_combobox.setMinimumWidth(self.comboboxMinWidth)
        self.zoneDict = self.getZoneList()
        self.geo_combobox.addItems(sorted(self.zoneDict.keys()))
        self.alighCombobox(self.geo_combobox)

        # Registr Button
        self.regBtn = QPushButton(' לחץ להרשמה '.decode('utf-8'))
        self.regBtn.setFont(register_btn_font)

        # Exit Button
        self.exitBtn = QPushButton('לחץ ליציאה'.decode('utf-8'))
        self.exitBtn.setFont(register_btn_font)

        # set the widgets on the layout
        grid = QGridLayout()
        grid.addWidget(r_label, 0, 0)
        grid.addWidget(r_value, 0, 1)

        grid.addWidget(img_label,0, 6)

        grid.addWidget(bd_label, 1, 0)

        grid.addWidget(cu_label, 2, 0)
        grid.addWidget(self.cu_combobox, 2, 1)

        grid.addWidget(fr_label, 3, 0)
        grid.addWidget(self.fr_combobox, 3, 1)

        grid.addWidget(br_label, 4, 0)
        grid.addWidget(self.br_combobox, 4, 1)

        h_box = QHBoxLayout()
        grid.addLayout(h_box, 5, 1)
        grid.addWidget(eip_label, 5, 0)
        h_box.addWidget(self.eip_1_octet,0)
        h_box.addWidget(eip_dot_label_4, 1)
        h_box.addWidget(self.eip_2_octet, 2)
        h_box.addWidget(eip_dot_label_3, 3)
        h_box.addWidget(self.eip_3_octet, 4)
        h_box.addWidget(eip_dot_label_2, 5)
        h_box.addWidget(self.eip_4_octet, 6)

        grid.addWidget(geo_label, 6, 0)
        grid.addWidget(self.geo_combobox, 6, 1)
        grid.addWidget(self.regBtn, 5, 6)
        grid.addWidget(self.exitBtn, 6, 6)
        self.setLayout(grid)

        self.connect(self.fr_combobox,
                     SIGNAL("currentIndexChanged(const QString&)"), self.updateBr)
        self.connect(self.cu_combobox,
                     SIGNAL("currentIndexChanged(const QString&)"), self.updateFr)
        self.connect(self.regBtn, SIGNAL("clicked ()"), self.FinishRegistration)
        self.connect(self.exitBtn, SIGNAL("clicked ()"), quit)


    def updateBr(self):
        self.branchDict = self.getBranchList(self.franchiseDict[unicode(self.fr_combobox.currentText())])
        self.br_combobox.clear()
        self.br_combobox.addItems(sorted(self.branchDict.keys()))
        self.alighCombobox(self.br_combobox)

    def updateFr(self):
        self.franchiseDict = self.getFranchisesList(self.customersDict[unicode(self.cu_combobox.currentText())])
        self.fr_combobox.clear()
        self.fr_combobox.addItems(sorted(self.franchiseDict.keys()))
        self.alighCombobox(self.fr_combobox)

    def FinishRegistration(self):
        # first update User Instances according to form data
        # octet 4 is the left most
        ext_ip = ".".join([unicode(self.eip_4_octet.text()), unicode(self.eip_3_octet.text()),
                           unicode(self.eip_2_octet.text()), unicode(self.eip_1_octet.text())])
        self.update_user_cls([self.r_name, self.cu_combobox.currentText(), self.fr_combobox.currentText(),
                              self.br_combobox.currentText(), ext_ip, self.geo_combobox.currentText()])
        self.create_str_to_file()
        print self.str2file
        self.set_file_handler()
        self.write_to_file()
        self.close_file_handler()
        # update sql with what ever is needed

        # pop up with a message that registration succeeded ?

        # exit app

    def get_r_name(self):
        recognizeInst = Recognize()
        self.r_name = recognizeInst.r_name

    def alighCombobox(self, comboboxWidget):
        comboboxWidget.setEditable(True)
        comboboxWidget.lineEdit().setReadOnly(True)
        comboboxWidget.lineEdit().setAlignment(Qt.AlignRight)
        for i in range(0,comboboxWidget.count()):
            comboboxWidget.setItemData(i, Qt.AlignRight, Qt.TextAlignmentRole)
        comboboxWidget.setEditable(False)
