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
  print("diskpart /s {0}".format(_writeDiskScript(default)))

def applyHighPowerScheme(default):
  if default.use_high_power_scheme:
    print("powercfg /s {0}".format(default.power_scheme))

def applyImage(default):
  print("dism /apply-image /imagefile:{0} /index:{1} /applydir:{2}".format(
    default.getWim(),
    default.wim_index,
    default.windows_vol
    )
  )

def applyBCDBoot(default):
  if default.is_UEFI:
    mode = "UEFI"
  else:
    mode = "BIOS"
  print("bcdboot {0}:\\Windows /s {1}".format(
    default.windows_vol,
    mode
    )
  )

def deployImage(default):
  SysFun().cls()
  print("deploying image...")
  applyPartitioning(default)
  applyHighPowerScheme(default)
  applyImage(default)
  applyBCDBoot(default)