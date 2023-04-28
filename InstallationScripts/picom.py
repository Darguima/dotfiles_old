from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("picom")

  install_package("picom")

  print_log_status(3)

  print_log_status(3, "Linking `picom.conf`")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/picom/picom.conf", f"{CONSTANTS['HOME']}/.config", "picom.conf")
  
  print_log_status(4)

  print_log_box()
