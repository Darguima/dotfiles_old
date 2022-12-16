from Utils.install_package import install_package
from Utils.create_sym_link import create_sym_link
from Utils.git_clone import git_clone
from Utils.run_command import run_command
from Utils.print_log import print_log_box, print_log_status
from Utils.download_file import download_file

from os.path import exists
from shutil import rmtree

from urllib.parse import quote as uri_converter

def installAndConfigure(CONSTANTS: dict):
  print_log_box("zsh")

  install_package("zsh")

  print_log_status(3)

  rm_tree_if_exists(CONSTANTS["ZSH_PATH"])

  print_log_status(3, "Installing Oh-My-ZSH")
  run_command('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
  #   CHSH       - 'no' means the installer will not change the default shell (default: yes)
  #   RUNZSH     - 'no' means the installer will not run zsh after the install (default: yes)
  #   --unattended: sets both CHSH and RUNZSH to 'no'

  print_log_status(3, "Cloning zsh-autosuggestions")
  git_clone("zsh-users/zsh-autosuggestions", f"{CONSTANTS['ZSH_CUSTOM']}/plugins/zsh-autosuggestions")

  print_log_status(3, "Cloning zsh-syntax-highlighting")
  git_clone("zsh-users/zsh-syntax-highlighting", f"{CONSTANTS['ZSH_CUSTOM']}/plugins/zsh-syntax-highlighting")

  print_log_status(3, "Installing Meslo Nerd Font")

  fonts_names = ["MesloLGS NF Regular.ttf", "MesloLGS NF Bold.ttf", "MesloLGS NF Italic.ttf", "MesloLGS NF Bold Italic.ttf"]
  for font_name in fonts_names:
    download_file(
      f"https://github.com/romkatv/powerlevel10k-media/raw/master/{uri_converter(font_name)}",
      f"/usr/share/fonts/MesloLGS/{font_name}",
      sudo=True
    )

  print_log_status(3, "Cloning powerlevel10k")
  git_clone("romkatv/powerlevel10k", f"{CONSTANTS['ZSH_CUSTOM']}/themes/powerlevel10k")

  print_log_status(3, "Changing default shell")
  run_command('sudo chsh --shell $(command -v zsh) $USER')
  
  print_log_status(3, "Linking dotfiles (zshrc & p10k.zsh)")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/zsh/zshrc", f"{CONSTANTS['HOME']}/.zshrc")
  create_sym_link(f"{CONSTANTS['DOTFILES']}/dotfiles/zsh/p10k.zsh", f"{CONSTANTS['HOME']}/.p10k.zsh")
  
  print_log_status(4)

def rm_tree_if_exists(zsh_path: str):
  if exists(zsh_path):
    print_log_status(3, f"Deleting old zsh path - {zsh_path}")
    rmtree(zsh_path)