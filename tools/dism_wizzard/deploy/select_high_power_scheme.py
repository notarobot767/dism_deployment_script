from ..system_functions import SysFun

def selectHighPowerScheme():
  SysFun().cls()
  return SysFun().confirm(r"set power scheme to high? [y\n]: ")