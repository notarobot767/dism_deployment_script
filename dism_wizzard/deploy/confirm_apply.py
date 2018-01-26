from ..system_functions import SysFun
import sys

def confirmApply(default):
  SysFun().cls()
  print("loading...")

  my_str = "About to:\n\n"
  
  #disk
  my_str += "clean {0}\n".format(SysFun().return_disk_list()[int(default.disk)])
  
  #partitioning
  if default.is_UEFI:
    part = "GDP"
  else:
    part = "MBR"
  my_str += "format disk to {0}\n".format(part)

  #powerscheme
  if default.use_high_power_scheme:
    my_str += "apply high power scheme\n"

  #wim
  my_str += "apply wim {0}\n".format(default.getWim())

  SysFun().cls()
  print(my_str)
  return SysFun().confirm()
  
