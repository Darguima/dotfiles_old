from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.run_command import run_command

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("xorg")

  dependencies = []
  if "nvidia" in run_command("lspci | grep VGA")[1].lower():
    dependencies.append("nvidia")

  install_package("xorg-server", dependencies)

  print_log_status(3)

  print_log_status(3, "Linking 00-keyboard.conf & 70-touchpad-settings")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/xorg/00-keyboard.conf", "/etc/X11/xorg.conf.d/00-keyboard.conf", sudo=True)
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/xorg/70-touchpad-settings", "/etc/X11/xorg.conf.d/70-touchpad-settings", sudo=True)
  
  print_log_status(4)

  print_log_box()
