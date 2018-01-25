from ..system_functions import SysFun
import os.path

def findLocalWimSource(default):
  for vol in SysFun().return_vol_list():
    path = "{0}:\\{1}".format(vol, default.local_wim_dir)
    if os.path.exists(path):
      return path
  SysFun().exit("could not find any local wim sources!")

def enterNetshare(default):
  while True:
    SysFun().cls()
    netshare = input("enter SMB netshare\n[{0}]: ".format(default.netshare)).strip()
    if netshare == "":
      netshare = default.netshare
    if SysFun().confirm():
      if os.path.exists(netshare.strip().split()[0]):
        return netshare
      print("unable to find netshare!")
      SysFun().pause()
      print("nope")

def selectWimSource(default):
  SysFun().cls()

  wim_source = [
    "Wim Source",       #menu title
    "Local Drive",      #1
    "SMB network share" #2
  ]

  choice = SysFun().selectOptionArry(wim_source)
  if choice == 1:
    default.is_wim_source_netshare = False
    return findLocalWimSource(default)

  else:
    default.is_wim_source_netshare = True
    default.netshare = enterNetshare(default)
    return default.netshare_vol + ":"