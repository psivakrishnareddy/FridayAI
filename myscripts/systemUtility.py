from __future__ import print_function
import pyautogui
import sys
import subprocess
import time
from timeloop import Timeloop
from datetime import timedelta
import psutil  # for system details checking - processes, batery ,temp , cpu
batt = None
tl = Timeloop()
tl.logger.disabled = True


def checkCompatibilty():
    global batt
    if not hasattr(psutil, "sensors_battery"):
        return sys.exit("platform not supported")
    batt = psutil.sensors_battery()
    if batt is None:
        return sys.exit("no battery is installed")


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%02d:%02d:%02d" % (hh, mm, ss)


# @tl.job(interval=timedelta(seconds=600))
def battery_check():
    stat = None
    if not batt.power_plugged and int(batt.percent) < 15:
        stat = "Battery Levels Critical!! Please Connect charger Immediately !!"

    elif not batt.power_plugged and int(batt.percent) < 60:
        stat = "Sir! Your Battery levels are low You have  %s time of battery Charge! Connect Your Adaptor" % secs2hours(
            batt.secsleft)
    return stat


def battery_status():
    status = []

    status.append("charge:     %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        status.append("status:     %s" % (
            "charging" if batt.percent < 100 else "fully charged"))
        status.append("plugged in: yes")
    else:
        status.append("left:       %s" % secs2hours(batt.secsleft))
        status.append("status:     %s" % "discharging")
        status.append("plugged in: no")
    return status


# Returns The name of processes running.
def processes_running_status():
    l = []
    for p in psutil.process_iter():
        l.append(p.name())
    return l


checkCompatibilty()
# print(processes_running_status())
