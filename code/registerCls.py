# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from sqlCls import SqlFunctions
from recognizeCls import Recognize
from userCls import User

from viewCls import View
from ipv4Cls import Ipv4
from view_defs import reg_defs, general_defs
from generalFunctions import get_scaled_pixmap

class ViewRegisterForm(View):
    def __init__(self):
        super(ViewRegisterForm, self).__init__()
        View.__init__(self)
        # router type
        self.router_type_group = self.create_label_label_group(reg_defs['h_r_type'])
        self.r_label = self.router_type_group['label1']
        self.r_value_label = self.router_type_group['label2']

        # business details Header
        bd_label = self.create_qlabel(reg_defs['h_buss_det'], 'header')

        # webees image
        img_label = QLabel()
        img_label.setPixmap(get_scaled_pixmap(general_defs['_logo_small']))

        # customer choosing ( Beecomm, Retalix)
        self.cu_group = self.create_label_combo_group(reg_defs['h_choose_cust'])
        self.cu_label = self.cu_group['label']
        self.cu_combobox = self.cu_group['combo']

        # franchise name ( rami levy ,...)
        self.fr_group = self.create_label_combo_group(reg_defs['h_choose_fr'])
        self.fr_label = self.fr_group['label']
        self.fr_combobox = self.fr_group['combo']

        # branch choosing ( natanya ,rosh ha-ayn..)
        self.br_group = self.create_label_combo_group(reg_defs['h_choose_br'])
        self.br_label = self.br_group['label']
        self.br_combobox = self.br_group['combo']

        # network card info header ( label )
        nc_label = self.create_qlabel(reg_defs['h_network_card_info'], 'header')

        # External IP Group creator
        self.ext_ip_group = self.create_ip_style_group(reg_defs['h_choose_ip_grp'])
        self.ext_ip_grid = self.ext_ip_group['grid']
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
        self.geo_group = self.create_label_combo_group(reg_defs['h_geo_label'])
        self.geo_label = self.geo_group['label']
        self.geo_combobox = self.geo_group['combo']

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

        self.grid.addWidget(self.r_label, 0, 0)
        self.grid.addWidget(self.r_value_label, 0, 1)

        self.grid.addWidget(img_label,0, 6)

        self.grid.addWidget(bd_label, 1, 0)

        self.grid.addWidget(self.cu_label, 2, 0)
        self.grid.addWidget(self.cu_combobox, 2, 1)

        self.grid.addWidget(self.fr_label, 3, 0)
        self.grid.addWidget(self.fr_combobox, 3, 1)

        self.grid.addWidget(self.br_label, 4, 0)
        self.grid.addWidget(self.br_combobox, 4, 1)

        # add external ip group to grid
        self.grid.addLayout(self.ext_ip_grid, 5, 0,1,2 )

        self.grid.addWidget(self.geo_label, 6, 0)
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

    def create_label_combo_group(self, groupName):
        group = dict()
        group['label'] = self.create_qlabel(groupName)
        group['combo'] = self.create_combobox()

        group['grid'] = QGridLayout()
        h_box = QHBoxLayout()
        group['grid'].addLayout(h_box, 0, 0)
        h_box.addWidget(group['label'])
        h_box.addWidget(group['combo'])

        return group

    def create_label_label_group(self, groupName):
        """
        This method is for creating a group like the one showing the router name
        Recognized automatically
        :param groupName: the
        :return: two horizontal labels and the second is styled
        """
        group = dict()
        group['label1'] = self.create_qlabel(groupName)
        group['label2'] = self.create_qlabel("")
        group['label2'].setMaximumHeight(30)
        group['label2'].setFrameShape(QFrame.Panel)
        group['label2'].setFrameShadow(QFrame.Sunken)

        return group

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

        return group

class CtrlRegisterForm(ViewRegisterForm, SqlFunctions, Ipv4, User):
    def __init__(self, user_id):
        super(CtrlRegisterForm, self).__init__()
        SqlFunctions.__init__(self)
        Ipv4.__init__(self)
        User.__init__(self)
        self.setUserId(user_id) # user_id is received from the auth form
        self.router_type_group['label2'].setText(QString(self.get_r_name()))
        # set customers Combo data
        self.customersDict = self.getCustomerList()
        self.cu_combobox.addItems(sorted(self.customersDict.keys()))
        # set franchise combo data
        self.franchiseDict = self.getFranchisesList(self.customersDict[unicode(self.cu_combobox.currentText())])
        self.fr_combobox.addItems(sorted(self.franchiseDict.keys()))
        # set branch combo data
        self.branchDict = self.getBranchList(self.franchiseDict[unicode(self.fr_combobox.currentText())])
        self.br_combobox.addItems(sorted(self.branchDict.keys()))
        # set default placeholder for external ip first two octets
        self.ext_ip_group['octet4'].setPlaceholderText('192')
        self.ext_ip_group['octet3'].setPlaceholderText('168')
        # set Geo location data
        self.zoneDict = self.getZoneList()
        self.geo_combobox.addItems(sorted(self.zoneDict.keys()))
        self.alighCombobox(self.geo_combobox)

        self.set_local_ip_octets()


        # Signals Binding
        self.connect(self.fr_combobox,
                     SIGNAL("currentIndexChanged(const QString&)"), self.updateBr)
        self.connect(self.cu_combobox,
                     SIGNAL("currentIndexChanged(const QString&)"), self.updateFr)
        self.connect(self.regBtn, SIGNAL("clicked ()"), self.FinishRegistration)
        self.connect(self.exitBtn, SIGNAL("clicked ()"), quit)

    def get_r_name(self):
        recognizeInst = Recognize()
        r_name = recognizeInst.r_name
        return QString(r_name)

    def set_local_ip_octets(self):
        l = self.ipv4Dict["IPv4Address"].split(".")
        for o in ['octet1', 'octet2', 'octet3', 'octet4']:
            self.local_ip_group[o].setText(QString(l[1]))



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


