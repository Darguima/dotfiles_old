from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.git_clone import git_clone
from Utils.run_command import run_command

def installAndConfigure(CONSTANTS: dict):
  print_log_box("awesome")

  install_package(
    "awesome",
    ["network-manager-applet", "pa-applet-git", "acpid", "acpilight", "xorg-xrandr", "arandr", "imagemagick", "i3lock", "rofi"]
  )

  print_log_status(3)

  print_log_status(3, "Enabling `acpid`")
  run_command("sudo systemctl enable acpid")

  print_log_status(3, "Cloning awesome widgets")
  git_clone("deficient/battery-widget", f"{CONSTANTS['HOME']}/.config/awesome/battery-widget")
  git_clone("deficient/brightness", f"{CONSTANTS['HOME']}/.config/awesome/brightness")

  print_log_status(3, "Linking `rc.lua` & `lockscreen`")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/awesome/rc.lua", f"{CONSTANTS['HOME']}/.config/awesome/rc.lua")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/awesome/lockscreen", "/usr/bin/lockscreen", sudo=True)
  
  print_log_status(4)

  print_log_box()


