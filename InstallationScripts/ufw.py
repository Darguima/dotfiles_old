from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package
from Utils.run_command import run_command

def installAndConfigure(CONSTANTS: dict, args: dict):
  print_log_box("ufw")

  install_package("ufw")

  print_log_status(3)

  print_log_status(3, "Activating ufw")
  run_command("sudo ufw enable")

  print_log_status(3, "Allowing doors at ufw")
  run_command("sudo ufw allow 22") #ssh
  run_command("sudo ufw allow 1714:1764/udp") # KDE Connect
  run_command("sudo ufw allow 1714:1764/tcp") # KDE Connect
  run_command("sudo ufw allow 8081") # React Native

  print_log_status(4)

  print_log_box()
