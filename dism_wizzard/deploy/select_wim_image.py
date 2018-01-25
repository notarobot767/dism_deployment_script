from ..system_functions import SysFun
import os

def selectWimImage(default):
  SysFun().cls()
  wims = [file for file in os.listdir(default.wim_source) if file.endswith(".wim")]
  if len(wims) == 0:
    SysFun().exit("no wims found in source folder!")
  else:
    wims.insert(0, "Wim Files")
    choice = SysFun().selectOptionArry(wims)
    print(choice)
    return wims[choice]
