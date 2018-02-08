from ..system_functions import SysFun

class DeployImage:
  def __init__(self, default):
    self.default = default
    self.deployImage()

  #write dynamic disk script and return path
  def _writeDiskScript(self):
    file = open(self.default.dynamic_diskscript, "w")
    file.write("select disk {0}\n".format(self.default.disk))
    if self.default.is_UEFI:
      script = self.default.createUEFI_script
    else:
      script = self.default.createMBR_script
    file.write(SysFun().cat(script))
    file.close()
    return self.default.dynamic_diskscript

  def applyPartitioning(self):
    SysFun().cls()
    print("partitioning drive...\n")
    SysFun().run("diskpart /s {0}".format(self._writeDiskScript()))

  def applyHighPowerScheme(self):
    if self.default.use_high_power_scheme:
      SysFun().cls()
      print("applying high power scheme...\n")
      SysFun().run("powercfg /s {0}".format(self.default.power_scheme))

  def applyImage(self):
    SysFun().cls()
    print("applying image...\n")
    SysFun().run("dism /apply-image /imagefile:{0} /index:{1} /applydir:{2}:\\".format(
      self.default.getWim(),
      self.default.wim_index,
      self.default.windows_vol
      )
    )

  def applyDrivers(self):
    if self.default.install_drivers_if_any and self.default.isDriverFolderPresent():
      SysFun().cls()
      print("applying drivers...\n")
      SysFun().run("dism /Image:{0} /Add-Driver /Driver:{1} /Recurse".format(
        self.default.getWim(),
        self.default.getDriverFolder()
        )
      )

  def applyBCDBoot(self):
    #SysFun().cls()
    print("applying Windows boot manager...\n")
    if self.default.is_UEFI:
      mode = "UEFI"
    else:
      mode = "BIOS"
    SysFun().run("bcdboot {0}:\\Windows /s {1}: /f {2}".format(
      self.default.windows_vol,
      self.default.system_vol,
      mode
      )
    )

  def deployImage(self):
    self.applyPartitioning()
    self.applyHighPowerScheme()
    self.applyImage()
    self.applyDrivers()
    self.applyBCDBoot()
    