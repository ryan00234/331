# -*- coding: utf-8 -*-
import os
pkg_name = 'bf.cloud.bfclouddemowithui'

def cpu():
    # os.popen('adb wait-for-device')
    cmd_cpu = os.popen('adb shell dumpsys cpuinfo |grep bf.cloud.bfclouddemowithui')
    for i in cmd_cpu.readlines():
        cpuinfo = i.split(' ')
        user = float(cpuinfo[4][:-1])
        kernel = float(cpuinfo[7][:-1])
    return (user, kernel)

def mem():
    cmd_mem = os.popen('adb shell dumpsys meminfo bf.cloud.bfclouddemowithui | grep TOTAL')
    for i in cmd_mem.readlines():
        meminfo = i.split(' ')
    list.sort(meminfo)
    return int(meminfo[-4])

