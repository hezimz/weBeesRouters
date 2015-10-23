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
        # business details Header
        bd_label = self.create_qlabel(reg_defs['h_buss_det'], 'header')
        # customer choosing ( Beecomm, Retalix)
        self.cu_group = self.create_label_combo_group(reg_defs['h_choose_cust'])
        # franchise name ( rami levy ,...)
        self.fr_group = self.create_label_combo_group(reg_defs['h_choose_fr'])
        # branch choosing ( natanya ,rosh ha-ayn..)
        self.br_group = self.create_label_combo_group(reg_defs['h_choose_br'])
        self.br_label = self.br_group['label']
        self.br_combobox = self.br_group['combo']

        # network card info header ( label )
        nc_label = self.create_qlabel(reg_defs['h_network_card_info'], 'header')

        # External IP Group creator
        self.ext_ip_group = self.create_ip_style_group(reg_defs['h_choose_ip_grp'])
        # local IP group creator
        self.local_ip_group = self.create_ip_style_group(reg_defs['h_local_ip_grp'])
        # local Subnet Mask group creator
        self.subnet_mask_group = self.create_ip_style_group(reg_defs['h_subnet_mask_grp'])
        # default gateway group creator
        self.default_gateway_group = self.create_ip_style_group(reg_defs['h_default_gateway_grp'])
        # preferred DNS Server group creator
        self.pref_dns_group = self.create_ip_style_group(reg_defs['h_pref_dns_grp'])
        # Alternate DNS Server group creator
        self.alt_dns_group = self.create_ip_style_group(reg_defs['h_alt_dns_grp'])
        # Geographic location (north ,south, center)
        self.geo_group = self.create_label_combo_group(reg_defs['h_geo_label'])
        # Register Button
        self.regBtn = self.create_button(reg_defs['h_register_btn'])
        # Exit Button
        self.exitBtn = self.create_button(reg_defs['h_exit_btn'] )
        ################################
        # set the widgets on the layout
        ################################
        self.grid = QGridLayout()
        local_ip_vbox = QVBoxLayout()
        dns_vbox = QVBoxLayout()

        self.grid.addLayout(self.router_type_group['grid'], 0, 0, 1, 2)
        self.grid.addWidget(self.img_label,0, 6)  # webees logo
        self.grid.addWidget(bd_label, 1, 0)  # business info header
        self.grid.addLayout(self.cu_group['grid'], 2, 0, 1, 2)  # customer group
        self.grid.addLayout(self.fr_group['grid'], 3, 0, 1, 2)  # frenchise group
        self.grid.addLayout(self.br_group['grid'], 4, 0, 1, 2)  # branch group
        # add external ip group to grid
        self.grid.addLayout(self.ext_ip_group['grid'], 5, 0, 1, 2)  # xternal ip
        # add geographic group to grid
        self.grid.addLayout(self.geo_group['grid'], 6, 0, 1, 2)
        # add Network Card Data
        self.grid.addWidget(nc_label,7,0)
        local_ip_vbox.addLayout(self.local_ip_group['grid'], 0)
        local_ip_vbox.addLayout(self.subnet_mask_group['grid'], 1)
        local_ip_vbox.addLayout(self.default_gateway_group['grid'], 2)
        dns_vbox.addLayout(self.pref_dns_group['grid'], 3)
        dns_vbox.addLayout(self.alt_dns_group['grid'], 4)

        self.grid.addLayout(local_ip_vbox, 8, 0, 1, 2)
        self.grid.addLayout(dns_vbox, 9, 0, 1, 2)

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
        group['grid'] = QGridLayout()
        h_box = QHBoxLayout()
        group['grid'].addLayout(h_box, 0, 0)
        group['label1'] = self.create_qlabel(groupName)
        group['label2'] = self.create_qlabel("")
        group['label2'].setMaximumHeight(30)
        group['label2'].setFrameShape(QFrame.Panel)
        group['label2'].setFrameShadow(QFrame.Sunken)
        h_box.addWidget(group['label1'])
        h_box.addWidget(group['label2'])

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
        self.cu_group['combo'].addItems(sorted(self.customersDict.keys()))
        # set franchise combo data
        self.franchiseDict = self.getFranchisesList(self.customersDict[
                                                        unicode(self.cu_group['combo'].currentText())])
        self.fr_group['combo'].addItems(sorted(self.franchiseDict.keys()))
        # set branch combo data
        self.branchDict = self.getBranchList(self.franchiseDict[unicode(self.fr_group['combo'].currentText())])
        self.br_group['combo'].addItems(sorted(self.branchDict.keys()))
        # set default placeholder for external ip first two octets
        self.ext_ip_group['octet4'].setPlaceholderText('192')
        self.ext_ip_group['octet3'].setPlaceholderText('168')
        # set Geo location data
        self.zoneDict = self.getZoneList()
        self.geo_group['combo'].addItems(sorted(self.zoneDict.keys()))
        self.alighCombobox(self.geo_group['combo'])
        # setting IPV4 infomation into octets
        self.set_ipv4_data_into_octets()

        # Signals Binding
        self.connect(self.fr_group['combo'],
                     SIGNAL("currentIndexChanged(const QString&)"), self.updateBr)
        self.connect(self.cu_group['combo'],
                     SIGNAL("currentIndexChanged(const QString&)"), self.updateFr)
        self.connect(self.regBtn, SIGNAL("clicked ()"), self.FinishRegistration)
        self.connect(self.exitBtn, SIGNAL("clicked ()"), quit)

    def get_r_name(self):
        recognizeInst = Recognize()
        r_name = recognizeInst.r_name
        return QString(r_name)

    def set_ipv4_data_into_octets(self):
        """
        for each ipv4 data we get from the network card (WMI package)
        we insert it to the right ip address line (local ip, dns, DG, subnet mask)
        :return:
        """
        oLst = ['octet4', 'octet3', 'octet2', 'octet1']
        pairs = {
            self.ipv4Dict["IPv4Address"]: self.local_ip_group,
            self.ipv4Dict["DefaultIPGateway"]: self.default_gateway_group,
            self.ipv4Dict["Subnet Mask"]: self.subnet_mask_group,
            self.ipv4Dict["pref DNS"]: self.pref_dns_group,
            self.ipv4Dict["alt DNS"]: self.alt_dns_group
        }
        for ipv4Key in pairs:
            l = ipv4Key.split(".")
            for o in oLst:
                pairs[ipv4Key][o].setText(QString(l[oLst.index(o)]))



    def updateBr(self):
        self.branchDict = self.getBranchList(self.franchiseDict[unicode(self.fr_group['combo'].currentText())])
        self.br_group['combo'].clear()
        self.br_group['combo'].addItems(sorted(self.branchDict.keys()))
        self.alighCombobox(self.br_group['combo'])

    def updateFr(self):
        self.franchiseDict = self.getFranchisesList(self.customersDict[unicode(self.cu_group['combo'].currentText())])
        self.fr_group['combo'].clear()
        self.fr_group['combo'].addItems(sorted(self.franchiseDict.keys()))
        self.alighCombobox(self.fr_group['combo'])

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


