from ..system_functions import SysFun
import os

def findDriverFolder(default):
  if os.path.isdir(default.getDriverFolder()):
    drivers = [d for d in os.listdir(default.getDriverFolder()) if os.path.isdir(os.path.join(default.getDriverFolder(), d))]
    drivers.insert(0, "Drivers")
    if len(drivers) > 1:
      return os.path.join(default.getDriverFolder(), drivers[SysFun().selectOptionArry(drivers)])
  return None

def selectInstallDrivers(default):
  SysFun().cls()
  if SysFun().confirm(r"install drivers? [y\n]: "):
    return findDriverFolder(default)
  return None