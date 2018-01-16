from lib.base_action import BaseAction
from st2client.client import Client 
from shutil import copyfile 


class Write_PXE_CFG(BaseAction):
    def run(self,  mac_addr, os, pxe_cfg_dir = None):
        
        if pxe_cfg_dir is None:
            pxe_cfg_path = "/opt/tftpboot/pxelinux.cfg"

        
        if os is None:
            print("No OS config item found, skipping custom PXE configuration template")
            return 0
                  
        try:
            print("os: %s   mac: %s" % (os, mac_addr))

            # check st2 data store for pxe cfg name for this OS 
            st2client = Client(base_url='http://localhost')
            key = "%s_pxe_cfg" % os.lower() 
            pxe_cfg = st2client.keys.get_by_name(name=key).value

            mac_dashes = mac_addr.replace(':', '-')
            
            # filename to store MAC specific pxe configuration under
            mac_file_name = "01-%s" % mac_dashes

            # full path to this OS's specific pxe configuration
            os_pxe_cfg = "%s/%s" % (pxe_cfg_path, pxe_cfg)
 
            print("os pxe cfg  %s" % os_pxe_cfg)
           
            # pxe config will be distributed to machines matching a mac address 
            #or IP address in HEX
            # see 
            # http://www.syslinux.org/wiki/index.php?title=PXELINUX#Configuration_filename 
            copyfile(
                os_pxe_cfg, 
                "%s/%s" % (pxe_cfg_path, mac_file_name)  
            )

            print("created pxe cfg file for mac: %s and os: %s  " % (mac_addr, os))

            return 0              
        except:
            print("error copying pxe cfg base file for os: %s mac: %s" % (os, mac_addr))  
            return "1" 

