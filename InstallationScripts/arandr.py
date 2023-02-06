from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("arandr")

  install_package("arandr", ["xorg-xrandr"])

  print_log_status(3)

  print_log_status(3, "Linking .screenlayouts folder's files")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/arandr/*", f"{CONSTANTS['HOME']}/.screenlayout", dest_is_directory=True)
  
  print_log_status(4)

  print_log_box()
