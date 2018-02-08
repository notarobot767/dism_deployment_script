from ..system_functions import SysFun

#write dynamic disk script and return path
def _writeDiskScript(default):
  file = open(default.dynamic_diskscript, "w")
  file.write("select disk {0}\n".format(default.disk))
  if default.is_UEFI:
    script = default.createUEFI_script
  else:
    script = default.createMBR_script
  file.write(SysFun().cat(script))
  file.close()
  return default.dynamic_diskscript

def applyPartitioning(default):
  #SysFun().cls()
  print("partitioning drive...\n")
  SysFun().run("diskpart /s {0}".format(_writeDiskScript(default)))

def applyHighPowerScheme(default):
  if default.use_high_power_scheme:
    #SysFun().cls()
    print("applying high power scheme...\n")
    SysFun().run("powercfg /s {0}".format(default.power_scheme))

def applyImage(default):
  #SysFun().cls()
  print("applying image...\n")
  SysFun().run("dism /apply-image /imagefile:{0} /index:{1} /applydir:{2}:\\".format(
    default.getWim(),
    default.wim_index,
    default.windows_vol
    )
  )

def applyDrivers(default):
  if default.install_drivers_if_any and default.isDriverFolderPresent():
    #SysFun().cls()
    print("applying drivers...\n")
    SysFun().run("dism /Image:{0} /Add-Driver /Driver:{1} /Recurse".format(
      default.getWim(),
      default.getDriverFolder()
      )
    )

def applyBCDBoot(default):
  #SysFun().cls()
  print("applying Windows boot manager...\n")
  if default.is_UEFI:
    mode = "UEFI"
  else:
    mode = "BIOS"
  SysFun().run("bcdboot {0}:\\Windows /s {1}: /f {2}".format(
    default.windows_vol,
    default.system_vol,
    mode
    )
  )

def deployImage(default):
  applyPartitioning(default)
  applyHighPowerScheme(default)
  applyImage(default)
  applyDrivers(default)
  applyBCDBoot(default)