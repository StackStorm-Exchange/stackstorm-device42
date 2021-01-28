from lib.base_action import BaseAction


class GetLifecycleEventObjects(BaseAction):
    def run(self):

        d42_headers = {'Accept': 'application/json'}
        payload = {"query": "SELECT * FROM view_assetaction_v1"}
        response = self.post(
            endpoint="services/data/v1.0/query/",
            payload=payload,
            headers=d42_headers,
            doql_query=True
        )
        # d42 api agent returns response.json(0) if response.ok...:
        if type(response) is dict:
            return response
        else:
            return response.text
