from lib.base_action import BaseAction 
import time, requests, json, sys 

class GetDeviceById(BaseAction):
    
    def run(self, device_id):
        
        url = 'devices/id/' + str(device_id) + '/'
        response = self.getAPI(url, {}) 
         
        
        full_device = json.loads(response.text)        
        
        print full_device 
        
        return full_device 

