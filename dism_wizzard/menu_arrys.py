from . import deploy
from . import pwedit
from .wpeutil import Wpeutil
from .system_functions import SysFun
import sys

class Menu:
  main = [
    "Main Menu",
    "Deploy Image",             #1
    "Express Image Deployment", #2
    "Password Editor",          #3
    "Powershell",               #4
    "Restart",                  #5
    "Shutdown"                  #6
  ]
  main_switch = {
    1 : deploy.main,
    2 : SysFun().wip,
    3 : pwedit.main,
    4 : sys.exit,
    5 : Wpeutil().restart,
    6 : Wpeutil().shutdown
  }