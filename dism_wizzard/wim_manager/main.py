from .wim_manager import WimManager
from ..system_functions import SysFun

def main():
  manager = WimManager()

  main_menu = [
    ["Wim Manager Menu"],
    ["Mount Image", manager.mountImage],
    ["Unmount & Commit Changes", manager.unmountImageCommit],
    ["Unmount & Discard Changes", manager.unmountImageDiscard],
    ["Write ISO", manager.writeISO],
    ["Write to Bootable USB (WIP)", SysFun().wip],
    ["Create PE", manager.copype],
    ["back..."]
  ]
  
  def fix(data):
    return data[0]
  
  fun_pos = 1

  while True:
    SysFun().cls()
    choice = SysFun().selectOptionArry(list(map(fix, main_menu)))
    if choice == len(main_menu) - 1:
      break
    else:
      main_menu[choice][fun_pos]()
