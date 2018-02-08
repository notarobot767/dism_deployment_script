from ..system_functions import SysFun
import os

def selectWimImage(default):
  SysFun().cls()
  try:
    path = os.listdir(default.wim_source)
  except FileNotFoundError:
    SysFun().exit("unable to find wim source dir!")

  wims = [file for file in path if file.endswith(".wim")]
  if len(wims) == 0:
    SysFun().exit("no wims found in source folder!")
  wims.insert(0, "Wim Files")
  return wims[SysFun().selectOptionArry(wims)]