from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.print_log import print_log_status, reprint_log

def installAndConfigure(CONSTANTS: dict):
  package_name = ""

  install_package(package_name, [])

  print_log_status(package_name, 3, reprint_log)

  # create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/", f"{CONSTANTS['HOME']}/.config/")
  
  print_log_status(package_name, 4, reprint_log)

