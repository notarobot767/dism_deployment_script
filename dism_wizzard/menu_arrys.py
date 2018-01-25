from . import deploy
from . import pwedit
from .wpeutil import Wpeutil
import sys

class Menu:
  main = [
    "Main Menu",
    "Deploy Image",    #1
    "Password Editor", #2
    "Powershell",      #3
    "Restart",         #4
    "Shutdown"         #5
  ]
  main_switch = {
    1 : deploy.main,
    2 : pwedit.main,
    3 : sys.exit,
    4 : Wpeutil().restart,
    5 : Wpeutil().shutdown
  }