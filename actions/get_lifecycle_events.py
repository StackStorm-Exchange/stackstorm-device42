from lib.base_action import BaseAction 
import time, requests, json, sys 

class GetLifecycleEvents(BaseAction):
    
    def get(self, url, user, pw, payload):
        try:
            res = requests.get(
                url,
                params=payload,
                auth=(user, pw),
                headers={'Accept': 'application/json'},
                verify=False # https call to localhost requires skipping verification
            )
        except requests.exceptions.RequestsException as e: 
            self.logger.error( e ) 
            sys.exit(1) 
        self.logger.info("HTTP GET %s - status: %s " % (url, res.status_code) )   
        return res

    def run(self, device, lc_type, asset, enduser, date_gt, date_lt):
        
        
        url = 'lifecycle_event/?' 
        
        params= {
            'device': device, 
            'type': lc_type, 
            'asset': asset, 
            'enduser': enduser, 
            'date_gt': date_gt, 
            'date_lt': date_lt
        }

        response = self.getAPI(url, d42_user, d42_pass, params=params) 
        
        full_device = json.loads(response.text) 
        
        print full_device 
        
        return full_device 

