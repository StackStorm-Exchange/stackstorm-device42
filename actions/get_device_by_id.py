from lib.base_action import BaseAction


class GetDeviceById(BaseAction):

    def run(self, device_id):

        url = 'devices/id/' + str(device_id) + '/'
        response = self.getAPI(url, {})
        print("response: ", response)
        if type(response) is dict:
            return response
        else:
            return response.text
