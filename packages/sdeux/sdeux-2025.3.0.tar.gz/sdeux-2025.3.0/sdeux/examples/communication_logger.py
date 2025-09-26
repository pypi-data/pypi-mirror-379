# -*- coding: utf-8 -*-
"""
Created by chiesa

Copyright Alpes Lasers SA, Switzerland
"""
__author__ = 'chiesa'
__copyright__ = "Copyright Alpes Lasers SA"

from datetime import datetime
import os

from sdeux.auto_detect import init_driver
from sdeux.communication import RETRY_NO, RETRY_SOME
from sdeux.serial_handler import S2SerialHandler

th = None

port = '/dev/ttyUSB0'

retry_policy = RETRY_NO   # on communications errors, raise an exception directly


def print_status(s2_instance):
    print_status = 'Bit Status: {}\n'.format(s2_instance.bit_stats) + \
                   'Uptime: {}\n'.format(s2_instance.get_uptime())
    print(print_status)

try:
    th = S2SerialHandler(port)
    th.open()
    s2 = init_driver(th)
    s2.set_up()
    s2.retry_policy = retry_policy
    print_status(s2)
    while True:
        try:
            uptime = s2.get_uptime()
        except Exception as e:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Communication error at")
            print(now)
            with open("communication_errors.log", "a") as log_file:
                log_file.write(f"[{now}] S2-m Communication error: {str(e)}\n")
            pass
        else:
            pass

finally:
    try:
        if th:
            th.close()
    except NameError:
        pass
