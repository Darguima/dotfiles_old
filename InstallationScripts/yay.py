from os import chdir

from Utils.run_command import run_command
from Utils.print_log import print_log_box, print_log_status
from Utils.git_clone import git_clone

def installAndUpdate(CONSTANTS: dict):
  print_log_box("yay")

  yayIsInstalled = not run_command("command -v yay", exit_on_error=False)[0]

  if not yayIsInstalled:
    print_log_status(1)
    
    print_log_status(1, "Installing dependencies:")

    print_log_status(1, "git", indentation=2)
    run_command("sudo pacman -S --needed --noconfirm git")
    
    print_log_status(1, "base-devel", indentation=2)
    run_command("sudo pacman -S --needed --noconfirm base-devel")

    print_log_status(1, "Cloning GitHub repository")
    git_clone("yay.git", f"{CONSTANTS['TEMP_PATH']}/yay", "https://aur.archlinux.org", overwrite=True)

    print_log_status(1, "Making package")
    chdir(f"{CONSTANTS['TEMP_PATH']}/yay")
    run_command("makepkg -si --noconfirm")
    chdir(CONSTANTS['ROOT_PATH'])

  else:
    print_log_status(12)
  
  # Updating the system with yay
  print_log_status(5)
  run_command("yay -Suy --noconfirm")
  print_log_status(6)
  
  print_log_box()
