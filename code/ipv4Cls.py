import wmi


class Ipv4(object):

    def __init__(self):

        self.ipv4Dict = dict()
        self.wmi_obj = wmi.WMI()
        self.wmi_sql = "select IPAddress,DefaultIPGateway,IPSubnet," \
                       "DNSServerSearchOrder from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
        self.wmi_out = self.wmi_obj.query(self.wmi_sql)
        self.preUrl = ""
        self.get_ipv4_dict()

    def get_ipv4_dict(self):

        for dev in self.wmi_out:
            self.ipv4Dict["IPv4Address"] = dev.IPAddress[0]
            self.ipv4Dict["DefaultIPGateway"] = dev.DefaultIPGateway[0]
            self.preUrl = "http://" + self.ipv4Dict["DefaultIPGateway"]
            self.ipv4Dict["Subnet Mask"] = dev.IPSubnet[0]
            self.ipv4Dict["DNS Servers"] = dev.DNSServerSearchOrder

