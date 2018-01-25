from ..system_functions import SysFun

def selectPartitioning():
  partitioning = [
  "Drive Partitioning", #menu title
  "GDP", #1
  "MBR"  #2
  ]

  SysFun().cls()
  choice = SysFun().selectOptionArry(partitioning)
  return choice == 1