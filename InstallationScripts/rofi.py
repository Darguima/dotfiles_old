from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("rofi")

  install_package("rofi")

  print_log_status(3)

  print_log_status(3, "Linking `config.rasi`")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/rofi/config.rasi", f"{CONSTANTS['HOME']}/.config/rofi", "config.rasi")
  
  print_log_status(4)

  print_log_box()
