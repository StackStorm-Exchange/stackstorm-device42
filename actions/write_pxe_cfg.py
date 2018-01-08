from lib.base_action import BaseAction
from shutil import copyfile 

class Write_PXE_CFG(BaseAction):
    def run(self,  mac_addr, os ):
        
        pxe_cfg_path = "/opt/tftpboot/pxelinux.cfg"
        ubuntu_default_pxe = "/ubuntu_default"
         
        try:
            print("os: %s   mac: %s" % (os, mac_addr))

            mac_dashes = mac_addr.replace(':', '-')
            mac_file_name = "01-%s" % mac_dashes 

            # pxe config will be distributed to machines matching a mac address or IP address in HEX
            # see http://www.syslinux.org/wiki/index.php?title=PXELINUX#Configuration_filename 
            if os.lower() == 'ubuntu':
                copyfile(
                    pxe_cfg_path + ubuntu_default_pxe, 
                    "%s/%s" % (pxe_cfg_path, mac_file_name)
                )
            print("created pxe cfg file for mac: %s and os: %s  " % (mac_addr, os))

            return 0              
        except:
            print("error copying pxe cfg base file for os: %s  and  mac: %s" % (os, mac_addr))  
            return "1" 

