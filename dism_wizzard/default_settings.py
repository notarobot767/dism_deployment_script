class DefaultSettings:
  def __init__(self):
    #script dirs
    ###########
    self.tools_dir = r"X:\tools"
      #python should cd to this dir once script has loaded
      #to avoid breaking relative path lookups

    #arbitrary drive letters for volumes
    ###################################################
    self.netshare_vol = "N"
      #if source is a netshare, it will be mounted as this drive letter
    self.windows_vol = "W"
      #the partition Windows will be applied to will be assigned this drive letter
    self.system_vol = "S"
      #the associated partition adjacent to Windows partition will be assigned
      #this drive letter

    #wim source
    ###########
    self.wim_image = "OG.wim"
      #name of wim file itself
    self.wim_source = "N:"
      #where the wim is located
    self.is_wim_source_netshare = True
    self.wim_index = 1
      #assumes wim has a index of the this value
    self.netshare = r"\\dropzone\anonymous\wim /user:user pass"
      #even if the netshare is not password protected, Windows
      #may require a bogus user and pw in order to connect
    self.local_wim_dir = r"_images"
      #findLocalWimSource will attempt to find this dir amoung
      #the available volumes
      #store your wim files in this folder in the root dir of your drive
    self.install_drivers_if_any = True
      #within the source folder where wim is located, check if within same folder,
      #that another folder drivers/[folder with name of wim image] exists
      #if present recurisvely install drivers after applying

    #partitioning
    #############
    self.disk = 0
      #default disk to format
    self.is_UEFI = True
      #is the partitioning going to be UEFI
      #false indicates MBR style
    self.createUEFI_script = r"dism_wizzard\diskpart\createUEFI.bat"
    self.createMBR_script = r"dism_wizzard\diskpart\createMBR.bat"
    self.dynamic_diskscript = r"dism_wizzard\diskpart\dynamic_diskscript.bat"
     #diskscript is the dynamic diskpart script built using the
     #default_disk and either the default create UEFI or MBR by writing
     #the line "select disk ?" followed by appending one of the above scripts

    #prompted user for the following or use the defaults?
    #####################################################
    self.prompt_select_disk = True
    self.prompt_select_partitioning = True
    self.prompt_select_wim_source = True
    self.prompt_select_wim_image = True
    self.prompt_pause_after_connecting_netshare = True
    self.prompt_install_drivers_if_any = True
    self.prompt_use_high_power_scheme = True
    self.prompt_confirm_before_applying_image = True

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