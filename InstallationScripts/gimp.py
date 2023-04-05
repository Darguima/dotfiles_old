from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_folder_link

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("gimp")

  install_package("gimp")

  print_log_status(3)

  print_log_status(3, "Linking `~/.config/GIMP` folder")
  create_folder_link(f"{CONSTANTS['DOTFILES']}/dotfiles/gimp", f"{CONSTANTS['HOME']}/.config/GIMP")
  
  print_log_status(4)

  print_log_box()
