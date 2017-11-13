from lib.base_action import BaseAction
import time, requests, json, random, string 

class Update_Device(BaseAction):

    def run(self, identifier, identifier_type, changes): 
        full_device = {} 
        
        # random_tag = [random.choice(string.letters) for i in range(10) ] # potentially useful for testing... 
        # random_tag = ''.join(random_tag) 
        
        payload = {identifier_type: identifier} # designate which device to update, based on any id_type:id pair 
        payload.update(changes) # include the KVP changes meant to change the device 
        
        url = 'device/'
         
        response = self.putAPI(url, payload=payload) 
        
        return response 

