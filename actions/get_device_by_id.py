from lib.base_action import BaseAction 
import time, requests, json, sys 

class GetDeviceById(BaseAction):
    
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

    def run(self, device_id):
        
        with open('/home/stanley/update_device.out', 'a') as out:
            out.write("get device ran at: %s" % time.strftime("%Y-%m-%d %H:%M") ) 
        
        print "hey we're running at: %s " % time.strftime("%Y-%m-%d %H:%M")  
        
        url = 'devices/id/' + str(device_id) + '/'
        response = self.getAPI(url, {}) 
         
        # response = self.get(url, d42_user, d42_pass) 
        
        full_device = json.loads(response.text)        
        
        print full_device 
        
        return full_device 

