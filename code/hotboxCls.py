from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from recognizeCls import Recognize


class HotboxFast3184(Recognize):

    def __init__(self):
        super(HotboxFast3184, self).__init__()

    def login(self):

        self.driver.get(self.preUrl)
        elem = self.driver.find_element_by_name('loginUsername')
        elem.send_keys(self.r_dict['auth']['loginUsername'])
        elem = self.driver.find_element_by_name('loginPassword')
        elem.send_keys(self.r_dict['auth']['loginPassword'])
        elem.send_keys(Keys.RETURN)

    def backup(self):

        self.login()
        self.driver.get(self.preUrl+"/RgBackup.asp")
        elem = self.driver.find_element_by_name('ExportFile')
        elem.click()
        wait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to_alert()
        alert.accept()
        return 0

    def restore(self):

        self.login()
        self.driver.get(self.preUrl+"/RgBackup.asp")
        elem = self.driver.find_element_by_name('ImportFile')
        fullCfgPath = self.r_dict['cfgFile']['location']+self.r_dict['cfgFile']['name']
        elem.send_keys(fullCfgPath)
        elem = self.driver.find_element_by_xpath("//input[@value='Restore'][@type='submit']")
        elem.send_keys(Keys.RETURN)
        wait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to_alert()
        alert.accept()
        return 0

    def reset(self):

        self.login()
        self.driver.get(self.preUrl + "/RgSetup.asp")
        elem = self.driver.find_element_by_xpath("//input[@value='Reboot'][@type='submit']")
        elem.send_keys(Keys.RETURN)
        wait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to_alert()
        alert.accept()
        return 0

    def get_ext_ip(self):

        self.login()
        self.driver.get(self.preUrl + "/RgSetup.asp")
        return 0

    Funcs = {
        'reset': reset,
        'restore': restore,
        'backup': backup,
        'getExtIP': get_ext_ip
    }

