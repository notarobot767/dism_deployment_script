from ..system_functions import SysFun

def selectInstallDrivers():
  SysFun().cls()
  return SysFun().confirm(r"check if driver folder is present and attempt to install drivers after deployment? [y\n]: ")