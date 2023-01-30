from Utils.print_log import print_log_box, print_log_status
from Utils.create_sym_link import create_sym_link
from Utils.run_command import run_command

def configure(CONSTANTS: dict, args: dict):
  """
  This script will do some system configurations.
  Some of them are on the Arch Installation Guide from the Time zone:
    * https://wiki.archlinux.org/title/installation_guide#Time_zone
  """

  print_log_box("Arch")

  print_log_status(0, "This script will do some system configurations", 0)
  print_log_status(0, "Some of them are on the Arch Installation Guide after the Time zone chapter\n", 0)

  print_log_status(3)

  print_log_status(3, "Setting Timezone and running hwclock (Arch Guide 3.3)")
  create_sym_link("/usr/share/zoneinfo/Portugal", "/etc/localtime", sudo=True)
  run_command("sudo hwclock --systohc")

  print_log_status(3, "Setting locale.gen, locale.conf & vconsole.conf (Arch Guide 3.4)")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/arch/locale.gen", "/etc/locale.gen", sudo=True)
  run_command("sudo locale-gen")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/arch/locale.conf", "/etc/locale.conf", sudo=True)
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/arch/vconsole.conf", "/etc/vconsole.conf", sudo=True)

  print_log_status(3, f"Setting {args['environment']}@hostname & {args['environment']}@hosts (Arch Guide 3.5)")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/arch/{args['environment']}@hostname", "/etc/hostname", sudo=True)
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/arch/{args['environment']}@hosts", "/etc/hosts", sudo=True)
  
  print_log_box()
