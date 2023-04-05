from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.systemctl import systemctl

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("syncthing")

  # install_package("syncthing", ["c++utilities", "qtforkawesome", "syncthingtray"])
  install_package("syncthing")
  print_log_status(3, "syncthingtray was not installed")

  print_log_status(3)

  print_log_status(3, "Linking syncthing.service")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/syncthing/syncthing.service", "/usr/lib/systemd/system", "syncthing.service", sudo=True)
  
  systemctl.enable("syncthing")
  systemctl.start("syncthing")

  
  
  print_log_status(4)

  print_log_box()
