from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link

def installAndConfigure(CONSTANTS: dict, args: dict):
  package_name = ""

  print_log_box(package_name)

  install_package(package_name)

  print_log_status(3)

  print_log_status(3, "Linking `file`")
  # create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/", f"{CONSTANTS['HOME']}/.config")
  
  print_log_status(4)

  print_log_box()
