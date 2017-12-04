from lib.base_action import BaseAction


class Add_Device_Lifecycle(BaseAction):

    def run(self, identifier, identifier_type,
            lc, device_name_prefix, additional_changes):

        # name / serial / asset / device_id ->  actual identifier of given type
        payload = {identifier_type: identifier}

        # add lifecycle to device
        changes = {
            "type": "%s" % (lc),
        }

        payload.update(changes)

        payload.update(additional_changes)

        url = 'lifecycle_event/'
        response = self.putAPI(url, payload=payload)

        return response
