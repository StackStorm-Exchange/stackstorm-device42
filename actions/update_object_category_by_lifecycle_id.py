from lib.base_action import BaseAction
from st2client.client import Client


class Update_Object_Category_By_Lifecycle_ID(BaseAction):

    def run(
        self,
        identifier,
        identifier_type,
        lc_type_id,
        additional_changes=None
    ):

        st2client = Client(base_url='http://localhost')

        # search st2 datastore for value stored under the lifecycle event id
        # in the datastore, the IDs are stored under the format
        #   lc_{lc event id} so prepend 'lc_'
        key = "lc_%s" % lc_type_id
        lc_type_name = st2client.keys.get_by_name(name=key)

        # add device identifier to payload
        payload = {identifier_type: identifier}

        # change obj cat with the LC name (as a basic example)
        changes = {
            "new_object_category": "%s" % (lc_type_name.value),
        }

        payload.update(changes)

        # if additional_changes:
        #    payload.update(additional_changes)

        url = 'device/'
        response = self.putAPI(url, payload=payload)

        return response
