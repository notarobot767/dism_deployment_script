from .system_functions import SysFun
import subprocess

class Wpeutil:
  def restart(self):
    SysFun().cls()
    print("restarting...")
    var = subprocess.call("wpeutil reboot", shell=True)

  def shutdown(self):
    SysFun().cls()
    print("shutting down...")
    var = subprocess.call("wpeutil shutdown", shell=True)
    