import os.path

class DefaultSettings:
  def __init__(self):
    self.dev_mode = True

    #script dirs
    ###########
    self.tools_dir = r"C:\Users\god\git\dism_deployment_script\tools"
    #self.tools_dir = r"X:\tools"
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
    self.wim_image = "ghost_snakes.wim"
      #name of wim file itself
    self.wim_source = r"C:\_images"
      #where the wim is located
    self.is_wim_source_netshare = False
    self.wim_index = 1
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
      #default disk to format
    self.is_UEFI = True
      #is the partitioning going to be UEFI
      #false indicates MBR style
    self._diskpart_dir = "\\dism_wizzard\\diskpart\\"
    self.createUEFI_script = "{0}createUEFI.bat".format(self.tools_dir)
    self.createMBR_script = "{0}createMBR.bat".format(self.tools_dir)
    self.dynamic_diskscript = "{0}dynamic_diskscript.bat".format(self.tools_dir)
     #diskscript is the dynamic diskpart script built using the
     #default_disk and either the default create UEFI or MBR by writing
     #the line "select disk ?" followed by appending one of the above scripts

    #prompted user for the following or use the defaults?
    #####################################################
    self.prompt_select_disk = False
    self.prompt_select_partitioning = False
    self.prompt_select_wim_source = False
    self.prompt_select_wim_image = True
    self.prompt_select_drivers = True
    self.prompt_pause_after_connecting_netshare = True
    self.prompt_use_high_power_scheme = False
    self.prompt_confirm_before_applying_image = True

    #power scheme
    #############
    self.use_high_power_scheme = True
    self.power_scheme = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
      #the high performance power scheme recommended by Microsoft to
      #use when depoying a WIM using DISM (optional speedup)
      #https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/winpe-mount-and-customize#highperformance

    #driver directory
    self.driver_dir = None

    #PE
    self.pe_image_dir = r"C:\WinPE_amd64_PS"
      #in Wim manager where working direcotry for the WinPE image will live
    self.adk_dir = r"C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit"
      #default location of ADK
      
    #misc
    #####
    self.encoding = r"utf8"
      #the default encoding in PS is unicode which does not play
      #nice with some applications when reading script files such as
      #when using the diskpart command

  def getWim(self):
    return "{0}\\{1}".format(self.wim_source, self.wim_image)
  def getDriverFolder(self):
    return "{0}\\_drivers".format(self.wim_source)
