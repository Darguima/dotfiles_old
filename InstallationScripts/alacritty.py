from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.print_log import reprint_log, print_log_status

def installAndConfigure(CONSTANTS: dict):
  install_package("alacritty")

  print_log_status("alacritty", 3, reprint_log)

  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/alacritty/alacritty.yml", f"{CONSTANTS['HOME']}/.config/alacritty/alacritty.yml")
  
  print_log_status("alacritty", 4, reprint_log)

