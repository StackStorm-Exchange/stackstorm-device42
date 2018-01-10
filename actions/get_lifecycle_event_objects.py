from lib.base_action import BaseAction


class GetLifecycleEventObjects(BaseAction):
    def run(self) 

        d42_headers = {'Accept': 'application/json'}
        payload = {query: "SELECT * FROM view_assetaction_v1"} 
        response = self.post( endpoint="/", payload=payload, headers=d42_headers)
        
        if type(response) is dict:  # d42 api agent returns response.json(0) if response.ok...:
            return response
        else:
            return response.text 
