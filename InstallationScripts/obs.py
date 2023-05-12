from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.copy import copy

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("obs")

  install_package("obs")

  print_log_status(3)

  print_log_status(3, "Linking `~/.config/obs-studio/basic/scenes`")
  copy(f"{CONSTANTS['DOTFILES']}/dotfiles/obs/scenes", f"{CONSTANTS['HOME']}/.config/obs-studio/basic/scenes")
  
  print_log_status(4)

  print_log_box()
