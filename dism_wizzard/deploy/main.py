import subprocess
from ..system_functions import SysFun
from .default_settings import DefaultSettings
from .select_disk import selectDisk
from .select_partitioning import selectPartitioning
from .select_wim_source import selectWimSource
from .select_wim_image import selectWimImage
from .select_high_power_scheme import selectHighPowerScheme

def main():
  default = DefaultSettings()
  if default.prompt_select_disk:
    default.disk = selectDisk()
  if default.prompt_select_partitioning:
    default.is_UEFI = selectPartitioning()
  if default.prompt_select_wim_source:
    selectWimSource(default)
  if default.is_wim_source_netshare:
    SysFun().connectNetshare(default)
  if default.prompt_select_wim_image:
    selectWimImage(default)


  if default.prompt_use_high_power_scheme:
    default.use_high_power_scheme = selectHighPowerScheme()


  if default.prompt_confirm_before_applying_image:
    print("confirm apply")
  var = subprocess.call("pause", shell=True)