from lib.base_action import BaseAction
import time, requests, json, random, string 

class Update_Device(BaseAction):

    def get(self, url, user, pw):
        try:
            res = requests.get(
                url,
                auth=(user, pw),
                headers={'Accept': 'application/json'},
                verify=False # https call to localhost requires skipping verification
            )
        except requests.exceptions.RequestsException as e: 
            self.logger.error( e ) 
            sys.exit(1) 
        self.logger.info("HTTP GET %s - status: %s " % (url, res.status_code) )   
        
        return res


    def put(self, url, payload, user, pw):
        
        try:  
            res = requests.put(
                url,
                auth=(user, pw),
                headers={'Accept': 'application/json'}, 
                data=payload,
                verify=False # https call to localhost requires skipping verification
            )
        except requests.exceptions.RequestsException as e:
            self.logger.error( e )
            sys.exit(1)
        self.logger.info("HTTP GET %s - status: %s " % (url, res.status_code) ) 
        
        return res 
        
         
    def run(self, identifier, identifier_type, changes): 
        full_device = {} 
        
        # random_tag = [random.choice(string.letters) for i in range(10) ] # potentially useful for testing... 
        # random_tag = ''.join(random_tag) 
        
        payload = {identifier_type: identifier} # designate which device to update, based on any id_type:id pair 
        payload.update(changes) # include the KVP changes meant to change the device 
        
        url = 'device/'
         
        response = self.putAPI(url, payload=payload) 
        
        return response 

