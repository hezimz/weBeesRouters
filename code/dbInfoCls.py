from paramsCls import ParamsLoader


class DbInfo(ParamsLoader):

    def __init__(self):
        super(DbInfo, self).__init__()
        # ParamsLoader.__init__(self)
        # paramsInst = ParamsLoader()
        # self._db_params = params["db"]
        # self.db_params = paramsInst.db_params

        self.sqlName = self.getSqlName()
        self.server_ip = self.getServerIp()
        self.dbname = self.getDbName()
        self.user_id = self.getUserID()
        self.password = self.getPassword()
        self.paramsDict = {
            "NAME": self.sqlName,
            "SERVER_IP": self.server_ip,
            "DATABASE": self.dbname,
            "UID": self.user_id,
            "PWD": self.password
        }

    def getSqlName(self):
        return self.db_params["NAME"]

    def getServerIp(self):
        return self.db_params["SERVER_IP"]

    def getDbName(self):
        return self.db_params["DATABASE"]

    def getUserID(self):
        return self.db_params["UID"]

    def getPassword(self):
        return self.db_params["PWD"]

    #def getDbParamsDict(self):
    #    return self.paramsDict
