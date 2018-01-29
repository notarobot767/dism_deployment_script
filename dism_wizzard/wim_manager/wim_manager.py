from ..system_functions import SysFun

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
  
  def copype(self):
    SysFun().cls()
    cmd = 'ECHO copype amd64 {0} | CALL cmd /k "{1}\Deployment Tools\DandISetEnv.bat"'.format(
      self.imagedir,
      self.getADKDir()
      )
    SysFun().pause()

  def writeISO(self):
    SysFun().cls()
    cmd = 'ECHO MakeWinPEMedia /ISO {0} {0}\WinPE_amd64_PS.iso | CALL cmd /k "{1}\Deployment Tools\DandISetEnv.bat"'.format(
      self.imagedir,
      self.getADKDir()
      )
    SysFun().run(cmd)
    SysFun().pause()
  
  def getImageFile(self):
    return self.imagedir + r"\media\sources\boot.wim"
  
  def getMountDir(self):
    return self.imagedir + r"\mount"

  def getADKDir(self):
    return r"C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit"
  
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
