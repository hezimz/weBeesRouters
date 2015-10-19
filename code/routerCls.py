
from recognizeCls import Recognize
from hotboxCls import HotboxFast3184


class Router(Recognize):

    def __init__(self):
        super(Router, self).__init__()
        self.backup = ""
        self.reset = ""
        self.restore = ""
        self.ready = False


    def instantiate_specific_router_cls(self):
        if self.r_name == "hotbox f@st3184":
            inst = HotboxFast3184()
            return inst

    def get_methods_from_inst(self, inst):
        self.backup = inst.backup
        self.reset = inst.reset
        self.restore = inst.restore

    def prepare_for_use(self):
        specific_router_instance = self.instantiate_specific_router_cls()
        self.ready = True
        return specific_router_instance


