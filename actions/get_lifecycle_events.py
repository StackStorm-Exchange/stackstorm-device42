from lib.base_action import BaseAction


class GetLifecycleEvents(BaseAction):

    def run(
        self,
        device_name,
        lc_type,
        asset,
        enduser,
        date_gt,
        date_lt
    ):

        url = 'lifecycle_event/?'

        params = {
            'device': device_name,
            'type': lc_type,
            'asset': asset,
            'enduser': enduser,
            'date_gt': date_gt,
            'date_lt': date_lt
        }

        response = self.getAPI(url, params=params)

        return response
