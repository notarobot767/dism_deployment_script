#from default_settings import DefaultSettings
from .system_functions import SysFun
from . import deploy
from . import pwedit
from .wpeutil import Wpeutil
from .system_functions import SysFun
import sys

def main():
  #menu name followed by assocaited function
  #position 0 is name of menu
  #the functions need to be stripped out in order for list
  #to be passed into selectOptionArry
  main_menu = [
    ["Main Menu"],
    ["Deploy Image", deploy.main],
    ["Express Image Deployment", SysFun().wip],
    ["Password Editor", pwedit.main],
    ["Powershell", sys.exit],
    ["Restart", Wpeutil().restart],
    ["Shutdown", Wpeutil().shutdown]
  ]

  def fix(data):
    return data[0]

  fun_pos = 1

  while True:
    SysFun().cls()
    main_menu[SysFun().selectOptionArry(list(map(fix, main_menu)))][fun_pos]()