from lib.base_action import BaseAction


class Update_Device(BaseAction):

    def run(self, identifier, identifier_type, changes):

        # potentially useful for testing...
        # random_tag = [random.choice(string.letters) for i in range(10) ]
        # random_tag = ''.join(random_tag)

        # designate which device to update, based on any id_type:id pair
        payload = {identifier_type: identifier}
        # include the KVP changes meant to change the device
        payload.update(changes)

        url = 'device/'

        response = self.putAPI(url, payload=payload)

        return response
