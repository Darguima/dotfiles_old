from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.print_log import print_log_status, print_log_box
from Utils.colors import colors

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("alacritty")

  install_package("alacritty")

  print_log_status(3)

  print_log_status(3, f"Linking {args['environment']}@{colors.UNDERLINE}alacritty.yml{colors.ENDC}")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/alacritty/{args['environment']}@alacritty.yml", f"{CONSTANTS['HOME']}/.config/alacritty", "alacritty.yml")
  
  print_log_status(4)

  print_log_box()


