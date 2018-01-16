from lib.base_action import BaseAction
from st2client.client import Client
from shutil import copyfile


class Write_PXE_CFG(BaseAction):
    def run(
        self,
        mac_addr,
        os,
        pxe_cfg_dir=None
    ):

        if pxe_cfg_dir is None:
            pxe_cfg_path = "/opt/tftpboot/pxelinux.cfg"

        if os is None:
            print("No OS CI found, skipping custom PXE configuration template")
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
            # or IP address in HEX
            # for more info:
            # http://www.syslinux.org/wiki/index.php?title=PXELINUX#Configuration_filename
            copyfile(
                os_pxe_cfg,
                "%s/%s" % (pxe_cfg_path, mac_file_name)
            )

            print(
                "created pxe cfg file - mac: %s and os: %s  " % (mac_addr, os)
            )

            return 0
        except Exception as e:
            print("error: %s " % e)
            print("error copying pxe cfg base file for: ")
            print("os: %s mac: %s" % (os, mac_addr))
            return "1"
