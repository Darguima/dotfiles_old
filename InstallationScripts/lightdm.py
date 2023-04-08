from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.copy import copy
from Utils.systemctl import systemctl

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("lightdm")

  install_package("lightdm", ["lightdm-webkit2-greeter"])

  systemctl.enable("lightdm")

  print_log_status(3)

  print_log_status(3, "Linking `lightdm.conf`")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/lightdm/lightdm.conf", f"/etc/lightdm", "lightdm.conf", sudo=True)
  
  # In this case is not possible to link the files, it's needed to copy them
  print_log_status(3, "Copying `lightdm-webkit2-greeter.conf` and `rui_theme` folder")
  copy(f"{CONSTANTS['DOTFILES']}/dotfiles/lightdm/lightdm-webkit2-greeter.conf", f"/etc/lightdm/lightdm-webkit2-greeter.conf", sudo=True)
  copy(f"{CONSTANTS['DOTFILES']}/dotfiles/lightdm/rui_theme", f"/usr/share/lightdm-webkit/themes/rui_theme", sudo=True)
  
  print_log_status(4)

  print_log_box()
