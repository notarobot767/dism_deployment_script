from ..system_functions import SysFun
import subprocess
import os.path

def lookForSAM():
  path = r"\Windows\System32\config\SAM"
  ans_lst = []
  for vol in SysFun().return_vol_list():
    if os.path.isfile("{0}:{1}".format(vol, path)):
      ans_lst.append(vol)
  if len(ans_lst) == 0:
    return ""
  return ", ".join(ans_lst)

def main():
  path = r"dism_wizzard\pwedit\ntpwedit64.exe"
  SysFun().cls()
  print("Found Windows SAMs in: " + lookForSAM())
  var = subprocess.call(path, shell=True)