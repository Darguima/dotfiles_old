from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.copy import copy

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("gimp")

  install_package("gimp")

  print_log_status(3)

  print_log_status(3, "Linking `~/.config/GIMP` folder")
  copy(f"{CONSTANTS['DOTFILES']}/dotfiles/gimp", f"{CONSTANTS['HOME']}/.config/GIMP")
  
  print_log_status(4)

  print_log_box()
