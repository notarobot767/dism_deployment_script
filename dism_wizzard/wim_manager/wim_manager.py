import os.path
from ..system_functions import SysFun
from ..default_settings import DefaultSettings

class WimManager:
  def __init__(self, imagedir=r"C:\WinPE_amd64_PS"):
    self.imagedir = imagedir
    self.index = 1
    self.ps_packages = [
      "WinPE-WMI.cab",
      "en-us\WinPE-WMI_en-us.cab",
      "WinPE-NetFX.cab",
      "en-us\WinPE-NetFX_en-us.cab",
      "WinPE-Scripting.cab",
      "en-us\WinPE-Scripting_en-us.cab",
      "WinPE-PowerShell.cab",
      "en-us\WinPE-PowerShell_en-us.cab",
      "WinPE-StorageWMI.cab",
      "en-us\WinPE-StorageWMI_en-us.cab",
      "WinPE-DismCmdlets.cab",
      "en-us\WinPE-DismCmdlets_en-us.cab"
      ]
    self._autoCreate(self.imagedir)
  
  def _autoCreate(self, imagedir):
    if not os.path.exists(imagedir):
      SysFun().cls()
      print("PE image directory not found!")
      if SysFun().confirm("build one in using default directory ['{0}']? [y/n]: ".format(imagedir)):
        self.copype()

  #ceate new pe enviornment in imagedir
  def copype(self):
    #SysFun().cls()
    cmd = 'ECHO copype amd64 {0} | CALL cmd /k "{1}\Deployment Tools\DandISetEnv.bat"'.format(
      self.imagedir,
      self.getADKDir()
      )
    SysFun().run(cmd)
    SysFun().pause()

  #if exists, delete imagedir
  def removePE(self):
    SysFun().cls()
    if os.path.exists(self.imagedir):
      cmd = "powershell rm {0} -Recurse".format(self.imagedir)
      SysFun().run(cmd)
    else:
      print("image directory does not exist!")
      SysFun().pause()



  def writeISO(self):
    SysFun().cls()
    if os.path.exists(self.getISODir()):
      cmd = "powershell rm {0}".format(self.getISODir())
      SysFun().run(cmd)
    cmd = 'ECHO MakeWinPEMedia /iso {0} {1} | CALL cmd /k "{2}\Deployment Tools\DandISetEnv.bat"'.format(
      self.imagedir,
      self.getISODir(),
      self.getADKDir()
      )
    SysFun().run(cmd)
    SysFun().pause()
  
  def getImageFile(self):
    return self.imagedir + r"\media\sources\boot.wim"
  
  def getMountDir(self):
    return self.imagedir + r"\mount"

  def getADKDir(self):
    return DefaultSettings().adk_dir

  def getISODir(self):
    return self.imagedir + r"\WinPE_amd64_PS.iso"
  
  def showWorkingDir(self):
    if os.path.exists(self.imagedir):
      return self.imagedir
    return None

  def mountImage(self):
    SysFun().cls()
    SysFun().run('Dism /Mount-Image /ImageFile:"{0}" /index:{1} /MountDir:"{2}"'.format(
      self.getImageFile(),
      self.index,
      self.getMountDir()
      )
    )
    SysFun().pause()
  
  def unmountImageCommit(self):
    SysFun().cls()
    SysFun().run('Dism /Unmount-Image /MountDir:"{0}" /Commit'.format(
      self.getMountDir()
      )
    )

  def unmountImageDiscard(self):
    SysFun().cls()
    SysFun().run('Dism /Unmount-Image /MountDir:"{0}" /Discard'.format(
      self.getMountDir()
      )
    )
