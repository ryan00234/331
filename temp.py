#!/usr/bin/env python
import os, time


def adb_shell():
    os.popen("adb wait-for-device")
    print "start uninstall..."
    for i in range(100000):
        for cpuinfo in os.popen("adb shell dumpsys cpuinfo |grep bf.cloud.bfclouddemowithui").readlines():
            str = cpuinfo.split(" ")
            user = str[4]
            kernel = str[7]
            # os.popen("adb uninstall " + packageName)
            print user
            print kernel
        time.sleep(1)

if __name__ == "__main__":
    adb_shell()
