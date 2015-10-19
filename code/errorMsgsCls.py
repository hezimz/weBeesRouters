# this class is initiated by receiving
# the xml_error_element (=error tag from program.xml)
# and it can return the error message according to a tag (error type)
# we give it
import logging


class ErrorMsgs(object):

    def __init__(self, xml_error_element):
        # the xml error element is valid after we
        # parse the program xml and extract the error "ErrorMsg"
        # specific tag

        # i only decalre the error dictionary variable
        # if the xml element has contents
        if len(xml_error_element) > 0:
            self._err_dict = {}
            for err_type_child in xml_error_element:
                self._err_dict[err_type_child.tag] = err_type_child.text

    def get_error_msg(self, err_type):
        return self._err_dict[err_type]
