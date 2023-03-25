from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.systemctl import systemctl

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("lightdm")

  install_package("lightdm", ["lightdm-gtk-greeter"])

  systemctl.enable("lightdm")

  print_log_status(3)

  print_log_status(3, "Linking `lightdm.conf`")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/lightdm/lightdm.conf", f"/etc/lightdm/lightdm.conf", sudo=True)
  
  print_log_status(4)

  print_log_box()
