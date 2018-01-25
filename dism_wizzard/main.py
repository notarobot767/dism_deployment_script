#from default_settings import DefaultSettings
from .system_functions import SysFun
from .menu_arrys import Menu

def main():
  while True:
    SysFun().cls()
    Menu.main_switch[SysFun().selectOptionArry(Menu.main)]()