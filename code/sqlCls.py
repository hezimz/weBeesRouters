# -*- coding: utf-8 -*-
import pyodbc

from dbInfoCls import DbInfo


class SqlFunctions(DbInfo):
    """
    perform all sql related functions

    """

    def __init__(self):
        """

        :return:
        testing123
        """

        super(SqlFunctions, self).__init__()
        # DbInfo.__init__(self)
        _db = self.paramsDict['DATABASE']
        _user_id = self.paramsDict['UID']
        _passwd = self.paramsDict['PWD']
        _host = self.paramsDict['SERVER_IP']
        self._connection_string = self.getConnString(_db, _user_id, _passwd, _host)
        self.cursor = self.getCursor()
        self.userID = "NA"
        self.userID = "NA"

    def getConnString(self,_db, _user_id, _passwd, _host):
        return 'DRIVER={SQL Server};' + \
               'SERVER=' + _host + \
               ';' 'DATABASE=' + _db + \
               ';' 'UID=' + _user_id + \
               ';' 'PWD=' + _passwd

    def getUserId(self, uName, pName):

        #upOptions = {
        #    userID: (uName, pName),
        #    '1':('webees', 'wb'),
        #    '2':('BeeComm', 'beecomm13'),
        #    '3':('Retalix', 'Retalix1')
        #}
        self.cursor.execute('{call [RouterBackup].[dbo].[Authentication](?,?)}', uName, pName)
        row = self.cursor.fetchone()
        if isinstance(row, pyodbc.Row):
            self.userID = row[0]
            return self.userID, uName
        else:
            # return ("NA","-E- DB didnt return any valid line")
            return ("err","Authentication")

    def setUserId(self, userId):
        self.userID = userId

    def getCustomerList(self):

        if self.userID == "NA":
            return 999
        self.cursor.execute('{call [RouterBackup].[dbo].[GetInfo_Cus](?)}', self.userID)
        row = self.cursor.fetchone()
        if isinstance(row, pyodbc.Row):
            d = dict()
            cus = row[1]
            self.customerIndex = row[0]
            self.cusID = str(self.customerIndex)
            d[cus] = self.cusID
            #return cusID + ";" + cus
            return d

        else:
            print " ; "
            return "999"

    def getFranchisesList(self, cusID):

        d = dict()
        frString = ''
        indexString = ''
        self.cursor.execute('{call [RouterBackup].[dbo].[GetInfo_FR](?)}', cusID)
        row = self.cursor.fetchall()
        if isinstance(row, list):
            for item in row:
                fr = item[1]
                ind = item[0]
                d[fr] = ind
                #print fr ," ", ind
                #d[ind] = fr
                #frString += fr + ","
                #indexString += str(ind) + ","
            #return frString + ";" + indexString
            return d

    def getBranchList(self,  frID):
        d = dict()
        #s = ''
        self.cursor.execute('{call [RouterBackup].[dbo].[GetInfo_BR](?)}', frID)
        row = self.cursor.fetchall()
        if isinstance(row, list):
            for item in row:
                br = item[1]
                ind = item[0]
                d[br] = ind
                #s += br + ","
            return d

    def getZoneList(self):
        zoneDict = dict()
        self.cursor.execute('{call [RouterBackup].[dbo].[GetZone]}')
        row = self.cursor.fetchall()
        #zoneString = ""
        if isinstance(row, list):
            for item in row:
                zone = item[1]
                #zoneString += zone.encode('cp1255') + ','
                #print type(zone)
                ind = item[0]
                zoneDict[zone] = ind
            return zoneDict

    def getCursor(self):
        """

        :return:

        A cursor for the sql connection
        using pyodbc.connect
        """

        try:
            cnxn = pyodbc.connect(self._connection_string)
            cursor = cnxn.cursor()
            return cursor
        except:
            return 0



