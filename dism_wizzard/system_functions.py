import subprocess
import sys

class SysFun:
  def _pound_text(self, word):
    return "{0}\n# {1} #\n{0}".format("#"*(len(word) + 4), word)

  def _returnOptionArryStr(self, arry):
    ans_str = self._pound_text(arry[0]) + "\n"
    for i, val in enumerate(arry[1:]):
      ans_str += "{0}. {1}\n".format(i+1, val)
    return ans_str

  def _verifyOptionArryResponse(self, arry, response):
    return response.isnumeric() and int(response) > 0 and int(response) < len(arry)

  def selectOptionArry(self, arry, msg="select option"):
    while True:
      print(self._returnOptionArryStr(arry))
      response = input("{0}: ".format(msg)).strip()
      if(self._verifyOptionArryResponse(arry, response)):
        return int(response)
      self.cls()

  def cat(self, file_name):
    return open(file_name, "r").read()

  def cls(self):
    var = subprocess.call("cls", shell=True)

  def pause(self):
    var = subprocess.call("pause", shell=True)

  def cd(self, directory):
    var = subprocess.call("cd {0}".format(directory), shell=True)

  def confirm(self, msg="continue? [y/n]: "):
    while True:
      choice = input(msg).strip().lower()
      if choice == "y":
        return True
      if choice == "n":
        return False

  def connectNetshare(self, default):
    cmd = "net use {0}: {1}".format(default.netshare_vol, default.netshare)
    var = subprocess.call(cmd, shell=True)

  def disconnectNetshare(self):
    cmd = "net use {0}: /delete".format(default.netshare_vol)
    var = subprocess.call(cmd, shell=True)

  def return_disk_list(self):
    path = r"powershell dism_wizzard\ps\list_disks.ps1"
    disks = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE).stdout.read().decode().strip()
    def fix(data):
      ans_arry = []
      for d in data.split("\r\n"):
        ans_arry.append(d.split(":")[1].strip())
      num, model = ans_arry
      return "Disk {0}: {1}".format(num, model)
    disks = list(map(fix, disks.split("\r\n\r")))
    return disks

  def return_vol_list(self):
    path = r"powershell dism_wizzard\ps\list_volumes.ps1"
    vols = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE).stdout.read().decode().strip()
    def fix(data):
      return data.split(" : ")[1].split()
    vols = list(map(fix, vols.split("\r\n\r")))
    return [item for sublist in vols for item in sublist]

  def exit(self, error):
    print(error)
    self.pause()
    sys.exit()