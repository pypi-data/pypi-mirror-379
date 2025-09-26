import logging


from sdeux.updater.writer import FirmwareUpdater




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    s2_port = '/dev/ttyUSB0'
    fu = FirmwareUpdater(port=s2_port,
                         stm32flash_path='/usr/local/bin/stm32flash',
                         new_firmware_version=3836,#s2_fw_version,
                         hw_version=2005,
                         configuration=dict(mode_auto_duty_limit_low=0.25,
                                            mode_auto_duty_limit_high=0.30)
                         )
    fu.upgrade()