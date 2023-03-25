from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.git_clone import git_clone
from Utils.get_args import convert_overwrite_to_bool
from Utils.systemctl import systemctl

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("awesome")

  install_package(
    "awesome",
    ["network-manager-applet", "pa-applet-git", "acpid", "acpilight", "imagemagick", "i3lock", "rofi"]
  )

  print_log_status(3)

  systemctl.enable("acpid")

  print_log_status(3, "Cloning awesome widgets")
  git_clone(
    "deficient/battery-widget",
    f"{CONSTANTS['HOME']}/.config/awesome/battery-widget",
    overwrite=convert_overwrite_to_bool(args["overwrite"], True)
  )
  git_clone(
    "deficient/brightness",
    f"{CONSTANTS['HOME']}/.config/awesome/brightness",
    overwrite=convert_overwrite_to_bool(args["overwrite"], True)
  )

  print_log_status(3, "Linking `rc.lua`, `lockscreen` and my awesome modules")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/awesome/rc.lua", f"{CONSTANTS['HOME']}/.config/awesome/rc.lua")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/awesome/get-dotfiles-environment", f"{CONSTANTS['HOME']}/.config/awesome/get-dotfiles-environment")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/awesome/lockscreen", "/usr/bin/lockscreen", sudo=True)
  
  print_log_status(4)

  print_log_box()


