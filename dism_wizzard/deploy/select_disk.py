from ..system_functions import SysFun

def selectDisk():
  SysFun().cls()
  disks = SysFun().return_disk_list()
  if disks:
    disks.insert(0, "Local Disks")
    choice = SysFun().selectOptionArry(disks)
    return choice - 1
  
  SysFun().exit("no disks found!")