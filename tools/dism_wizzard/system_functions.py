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

  #take in array of items and ennumerate them and ask user to select one
  #position 0 is the menu name and not an item
  #user is forced to select a vaild item
  #example ["Main Menu", "thing1", "think2"]
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
    self.run("cls")

  def pause(self):
    self.run("pause")

  def cd(self, directory):
    self.run("cd {0}".format(directory))

  #yes or no prompt
  #return true of false
  def confirm(self, msg="continue? [y/n]: "):
    while True:
      choice = input(msg).strip().lower()
      if choice == "y":
        return True
      if choice == "n":
        return False

  def run(self, cmd):
    var = subprocess.call(cmd, shell=True)

  #holder function for works in progress
  def wip(self):
    self.exit("work in progress!")

  #mount a netshare using the volume letter found in default.netshare_vol
  def connectNetshare(self, default):
    self.cls()
    print("connecting to '{0}'\nand mounting as '{1}:'".format(  
      default.netshare,
      default.netshare_vol
      )
    )
    cmd = "net use {0}: {1}".format(default.netshare_vol, default.netshare)
    self.run(cmd)
    if default.prompt_pause_after_connecting_netshare:
      if not self.confirm():
        sys.exit()

  #unmount the netshare volumed found in default.netshare_vol
  def disconnectNetshare(self, default):
    cmd = "net use {0}: /delete".format(default.netshare_vol)
    self.run(cmd)

  def startPS(self):
    self.cls()
    cmd = "CALL powershell"
    self.run(cmd)

  #return list of strings of disks and associated names in order assending
  #example ["Disk 0: generic disk", "Disk 1: samsung something 512GB"]
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

  #return list of volumes currently in use (drive letters)
  #example ["C", "D", "N"]
  def return_vol_list(self):
    path = r"powershell dism_wizzard\ps\list_volumes.ps1"
    vols = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE).stdout.read().decode().strip()
    def fix(data):
      return data.split(" : ")[1].split()
    vols = list(map(fix, vols.split("\r\n\r")))
    return [item for sublist in vols for item in sublist]

  #print message before exiting program
  def exit(self, error):
    print(error)
    self.pause()
    sys.exit()