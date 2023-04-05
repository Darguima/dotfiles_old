from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("qt")

  install_package("qt5ct")

  print_log_status(3)

  print_log_status(3, "Linking `qt5ct.conf`")
  # It's dependent from ~/.xprofile variables
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/qt/qt5ct.conf", f"{CONSTANTS['HOME']}/.config/qt5ct", "qt5ct.conf")
  
  print_log_status(4)

  print_log_box()
