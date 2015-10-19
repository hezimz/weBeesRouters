import xml.etree.ElementTree as ET
import os.path
import logging
from view_defs import general_defs
import sys

# set Logging level
logging.basicConfig(format='-%(levelname)s- %(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=general_defs['_logging_level'])


class XmlParser (object):

    def __init__(self):
        self._xml_file = ''  # private variable containing the xml file to parse
        self._root = ""
        self._tree = ""
        logging.debug("Initialized an XML parser")

    def set_xml_tree(self, _xml_file):
        try:
            self._tree = ET.parse(_xml_file)
        except ET.ParseError:
            logging.critical("Failed parsing XML file: %s", _xml_file)
            raise ET.ParseError

    def set_xml_file(self, xml_file_name):
        # this is a setter , for setting the xml_file private variable
        # before we can parse any xml data

        if os.path.isfile(xml_file_name):
            logging.debug('Setting current XML file to be: %s ', xml_file_name)
            self._xml_file = xml_file_name
        else:
            logging.warning('XML file given is not valid: %s ', xml_file_name)

    def parse_xml(self):
        # this method will check if there is an xml
        # file updated in self._xml_file
        # and then try to parse it using xml.etree...
        if self._xml_file == '':
            logging.critical("Found an empty xml file name while trying to parse xml, first set "
                             "the xml file source")
        else:
            try:
                self.set_xml_tree(self._xml_file)
                self._root = self._tree.getroot()
                return True
            except ET.ParseError:
                return False
            # ['__class__', '__delattr__', '__delitem__', '__dict__', '__doc__', '__format__',
            # '__getattribute__', '__getitem__', '__hash__', '__init__', '__len__', '__module__',
            # '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
            # '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
            # '_children', 'append', 'attrib', 'clear', 'copy', 'extend', 'find', 'findall',
            # 'findtext', 'get', 'getchildren', 'getiterator', 'insert', 'items', 'iter',
            # 'iterfind', 'itertext', 'keys', 'makeelement', 'remove', 'set', 'tag', 'tail', 'text']
            #for child in self._root:
                #print child.tag , child.attrib

    def get_error_element(self):
        # by element i mean an xml tree element
        for child in self._root:
                if child.tag == "ErrorMsg":
                    return child

    def get_server_element(self):
        # by element i mean an xml tree element
        for child in self._root:
                if child.tag == "Server":
                    return child
