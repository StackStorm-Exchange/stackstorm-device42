from lib.base_action import BaseAction
import datetime


class Add_Device_Lifecycle(BaseAction):

    def run(self, identifier, identifier_type,
            lc, device_name_prefix, additional_changes=False):

        # name / serial / asset / device_id ->  actual identifier of given type
        payload = {identifier_type: identifier}

        d = datetime.datetime
        timestamp = d.now().strftime("%Y-%m-%d %H:%M")

        # add lifecycle to device
        changes = {
            "type": "%s" % (lc),
            "date": "%s" % (timestamp),
        }

        payload.update(changes)

        if additional_changes:
            payload.update(additional_changes)

        url = 'lifecycle_event/'
        response = self.putAPI(url, payload=payload)
        print("response: %s" % response)
        return response
