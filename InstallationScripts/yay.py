from os import chdir

from Utils.run_command import run_command
from Utils.print_log import print_log
from Utils.colors import colors

def install(CONSTANTS: dict):
  yayIsInstalled = not run_command("command -v yay", exit_on_error=False)[0]

  if not yayIsInstalled:
    print_log(f"\t-> Installing {colors.BOLD}yay{colors.ENDC}")
    
    print_log("\t\t-> Installing dependencies:")

    print_log("\t\t\t-> git")
    run_command("sudo pacman -S --needed --noconfirm git")
    
    print_log("\t\t\t-> base-devel")
    run_command("sudo pacman -S --needed --noconfirm base-devel")

    print_log("\t\t-> Cloning GitHub repository")
    run_command(f"git clone https://aur.archlinux.org/yay.git \"{CONSTANTS['TEMP_PATH']}/yay\"")

    print_log("\t\t-> Making package")
    chdir(f"{CONSTANTS['TEMP_PATH']}/yay")
    run_command("makepkg -si --noconfirm")
    chdir(CONSTANTS['ROOT_PATH'])

  else:
    print_log(f"\t-> {colors.BOLD}yay{colors.ENDC} already installed")

def update(CONSTANTS: dict):
  print_log(f"\t-> Updating {colors.BOLD}yay{colors.ENDC}")
