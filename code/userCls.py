# -*- coding: Windows-1255 -*-
# this class will get the data from the register form and save whats needed
# in a file
from datetime import datetime

from paramsCls import ParamsLoader


class User(ParamsLoader):

    def __init__(self):
        super(User, self).__init__()
        # ParamsLoader.__init__(self)
        self.str2file = ""
        self.router_name = ""
        self.customer = ""
        self.franchise = ""
        self.branch = ""
        self.zone = ""
        self.ext_ip = ""
        self.updateDate = unicode(datetime.now()).split(" ")[0]


    def set_file_handler(self):
        file_name = self.local_file_location + self.local_file_name
        self.fh = open(file_name,'w')

    def close_file_handler(self):
        self.fh.close()

    def write_to_file(self):
        self.fh.write(self.str2file.encode('Windows-1255'))

    def update_user_cls(self, infoLst):
        self.set_router_name(infoLst[0])
        self.set_customer(unicode(infoLst[1]))
        self.set_franchise(unicode(infoLst[2]))
        self.set_branch(unicode(infoLst[3]))
        self.set_ext_ip(unicode(infoLst[4]))
        self.set_zone(unicode(infoLst[5]))

    def set_router_name(self, rName):
        #print "setting router name  %s",rName
        self.router_name = rName

    def set_customer(self, cus):
        #print "setting customer name  %s", cus
        self.customer = cus

    def set_franchise(self, fr):
        #print "setting franchise name  %s", fr
        self.franchise = fr

    def set_branch(self, br):
        #print "setting branch name  %s", br
        self.branch = br

    def set_zone(self, zone):
        #print "setting zone name  %s", zone
        self.zone = zone

    def set_ext_ip(self, ip):
        #print "setting external ip %s", ip
        self.ext_ip = ip

    def create_str_to_file(self):
        self.str2file = ",".join(["Date","Router Name", "Customer", "Franchise", "Branch", "External IP", "Zone", "\n"])
        self.str2file += ",".join([self.updateDate, self.router_name, self.customer, self.franchise, self.branch, self.ext_ip, self.zone])

    def get_str_to_file(self):
        return self.str2file