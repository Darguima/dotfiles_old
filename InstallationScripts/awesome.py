from Utils.print_log import reprint_log, print_log_status
from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.git_clone import git_clone
from Utils.run_command import run_command

def installAndConfigure(CONSTANTS: dict):
  package_name = "awesome"

  install_package(
    package_name,
    ["network-manager-applet", "pa-applet-git", "acpid", "xorg-xbacklight", "xorg-xrandr", "arandr", "imagemagick", "i3lock"]
  )

  print_log_status(package_name, 3, reprint_log)

  run_command("sudo systemctl enable acpid")

  git_clone("deficient/battery-widget", f"{CONSTANTS['HOME']}/.config/awesome/battery-widget")
  git_clone("deficient/brightness", f"{CONSTANTS['HOME']}/.config/awesome/brightness")

  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/awesome/rc.lua", f"{CONSTANTS['HOME']}/.config/awesome/rc.lua")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/awesome/lockscreen", "/usr/bin/lockscreen", sudo=True)
  
  print_log_status(package_name, 4, reprint_log)

