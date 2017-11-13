from lib.base_action import BaseAction

class GetDeviceById(BaseAction):

    def run(self, device_id):

        url = 'devices/id/' + str(device_id) + '/'
        response = self.getAPI(url, {})

        return response
