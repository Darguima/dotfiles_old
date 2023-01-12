from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.print_log import reprint_log, print_log_status, print_log_box

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("alacritty")

  install_package("alacritty")

  print_log_status(3)

  print_log_status(3, "Linking `alacritty.yml`")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/alacritty/alacritty.yml", f"{CONSTANTS['HOME']}/.config/alacritty/alacritty.yml")
  
  print_log_status(4)

  print_log_box()


