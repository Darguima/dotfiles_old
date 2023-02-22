from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.run_command import run_command

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("lightdm")

  install_package("lightdm", ["lightdm-gtk-greeter"])

  print_log_status(3, "Enabling `lightdm`")
  run_command("sudo systemctl enable lightdm")

  print_log_status(3)

  print_log_status(3, "Linking `lightdm.conf`")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/lightdm/lightdm.conf", f"/etc/lightdm/lightdm.conf", sudo=True)
  
  print_log_status(4)

  print_log_box()
