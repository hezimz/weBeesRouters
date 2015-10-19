# from login import login
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from requests import Session, Request

from paramsCls import ParamsLoader
from ipv4Cls import Ipv4


class Recognize(Ipv4, ParamsLoader):

    def __init__(self):
        ParamsLoader.__init__(self)
        Ipv4.__init__(self)

        self.routerRecognizeFuncMapping = {
            'hotbox f@st3184': self._hotbox,
            'dlink DSL-2500U': self._dlink2500,
            'dlink DSL-6740U': self._dlink6740,
            'dlink DSL-6850U': self._dlink6850,
            'edimax br6214k': self._edimax6214k,
            'edimax br6428ns': self._edimax6428ns,
            'edimax br6226n': self._edimax6226n,
            'netgear dgn2200v2': self._netgeardgn2200v2,
            'netgear vegn2610': self._netgearvegb2610,
            'tplink WR740N': self._tplinkwr740n
        }
        self.r_name = self.recognize()
        self.r_dict = self.routers_params = self.params["routers"][self.r_name]

    ## Main recognize method, uses the below specific recognize methods
    def recognize(self):

        for router in self.routerRecognizeFuncMapping.keys():
            response = self.loginRequests(router, True)
            if response and response.status_code == 200:
                s = BeautifulSoup(response.content, "html.parser")
                if self.routerRecognizeFuncMapping[router](s, response):
                    return router

        return 0

    def set_selenium_driver(self):

        print "Setting Selemium Driver"
        chrome_options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": self.r_dict['cfgFile']['location']}
        chrome_options.add_experimental_option("prefs", prefs)
        chromedriver = "C:\Python27\Scripts\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
        self.driver.set_window_position(0, 0)

    def loginRequests(self, routerName, forRecognition):

        r_dict = self.routers_params[routerName]
        data = r_dict['login']['data']
        auth = (r_dict['auth']['loginUsername'], r_dict['auth']['loginPassword'])
        url = self.preUrl + r_dict['login']['url']
        s = Session()
        req = Request(r_dict['login']['method'], url=url, auth=auth, data=data)
        prepped = req.prepare()
        try:
            res = s.send(prepped)
            if res.status_code == 200:
                if forRecognition:
                    return res
                else:
                    #return "-I- Logged in to: ", router
                    return True
            else:
                #return "-E- Problems Logging into", router
                return False
        except:
            #print "-E- Problems Logging into..", router
            return False

    def _hotbox(self, s, r):
        pat = re.compile('product="HOTBOX"')
        if s.head and s.head.script and pat.match(s.head.script.text):
            return 1
        return 0


    def _netgearvegb2610(self, s, r):
        if s.head and s.head.title:
            titleText = s.head.title.text
            if titleText.find('VEGN2610') > 0:
                return 1
        return 0

    def _netgeardgn2200v2(self, s, r):
        if s.head and s.head.title:
            titleText = s.head.title.text
            if titleText.find('DGN2200V2'):
                return 1
        return 0


    def _dlink2500(self, s, r):
        pat = re.compile("^DSL Router")
        if s.head:
            if pat.match(s.head.title.text):
                return 1
        return 0


    def _dlink6740(self, s, r):
        pat = re.compile("^D-Link ADSL Router")
        if s.head:
            if pat.match(s.head.title.text):
                return 1
        return 0


    def _dlink6850(self, s, r):
        pat = re.compile("^D-Link VDSL Router")
        if s.head:
            if pat.match(s.head.title.text):
                return 1
        return 0


    def _edimax6214k(self, s, r):
        if 'server' in r.headers and r.headers['server'] == 'Boa/0.93.15':
            return 1

        return 0


    def _edimax6428ns(self, s, r):
        if 'server' in r.headers and r.headers['server'] == 'GoAhead-Webs':
            return 1

        return 0


    def _edimax6226n(self, s, r):
        # recognition mechanism is the same as edimax 6428ns.
        # so in case its a 6226 ,i will first attempt to work as if i recognized 6428 ,
        # see that the script made a mistake and then return and go back with 6226 "manual" recognition
        if 'server' in r.headers and r.headers['server'] == 'GoAhead-Webs':
            return 1

        return 0


    def _tplinkwr740n(self, s, r):
        pat = re.compile("^TL-WR740N")
        if s.head:
            if pat.match(s.head.title.text):
                return 1
        return 0
