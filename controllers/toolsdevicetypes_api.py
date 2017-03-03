""" Tools Device Types Api Calls """

from ..phpipam import PhpIpamApi

class ToolsDeviceTypesApi(object):
    """ Tools Devices Api Class """
    def __init__(self, phpipam=None):
        if phpipam:
            self.phpipam = phpipam
        else:
            self.phpipam = PhpIpamApi()


    def list_devicetypes(self):
        """ get device type list """
        uri = 'tools/devicetypes/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result


    def list_devicetype_devices(self, devicetype_id=''):
        """ get device type devices """
        uri = 'tools/devicetypes/' + str(devicetype_id) + '/devices/'
        result = self.phpipam.api_send_request(path=uri, method='get')
        return result
    