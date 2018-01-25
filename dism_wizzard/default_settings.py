class DefaultSettings:
  def __init__(self):
    #script dirs
    ###########
    self.tools_dir = r"X:\tools"

    #arbitrary drive letters for volumes
    ###################################################
    self.netshare_vol = "N"
    self.windows_vol = "W"
    self.system_vol = "S"

    #wim source
    ###########
    self.wim_image = "OG.wim"
    self.wim_source = "N:"
    self.is_wim_source_netshare = True
    self.index_index = 1
      #assumes wim has a index of the this value
    self.netshare = r"\\dropzone\anonymous\wim /user:user pass"
      #even if the netshare is not password protected, Windows
      #may require a bogus user and pw in order to connect
    self.local_wim_dir = r"_images"
      #findLocalWimSource will attempt to find this dir amoung
      #the available volumes
      #store your wim files in this folder in the root dir of your drive

    #partitioning
    #############
    self.disk = 0
    self.is_UEFI = True
    self.createUEFI_script = "diskpart\createUEFI.bat"
    self.createMBR_script = "diskpart\createMBR.bat"
    self.dynamic_diskscript = "diskpart\dynamic_diskscript.bat"
     #diskscript is the dynamic diskpart script built using the
     #default_disk and either the default create UEFI or MBR 

    #prompted user for the following or use the defaults?
    #####################################################
    self.prompt_select_disk = True
    self.prompt_select_partitioning = True
    self.prompt_select_wim_source = True
    self.prompt_select_wim_image = True
    self.prompt_pause_after_connecting_netshare = True
    self.prompt_confirm_before_applying_image = True
    self.prompt_use_high_power_scheme = True

    #power scheme
    #############
    self.use_high_power_scheme = True
    self.power_scheme = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
      #the high performance power scheme recommended by Microsoft to
      #use when depoying a WIM using DISM (optional speedup)
      #https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-mount-and-customize#highperformance

    #misc
    #####
    self.encoding = "utf8"
      #the default encoding in PS is unicode which does not play
      #nice with some applications when reading script files such as
      #when using the diskpart command

  def getWim(self):
    return "{0}\\{1}".format(self.wim_source, self.wim_image)