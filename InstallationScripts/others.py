from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package

"""
  Templates:

  * Installing packages without dependencies:
  
  print_log_status(1, f"Installing xxx")
  install_package("xxx", print_status=False)
  
  * Installing packages with dependencies:
  
  print_log_status(1, f"Installing xxx")
  print_log_status(1, f"Installing dependency xxx", indentation=2)
  install_package("xxx", ["xxx"], print_status=False)
"""

def installAndConfigure(CONSTANTS: dict, args: dict):
  """
  This packages don't need to be configured, just to be installed
  """

  print_log_box("Others")

  print_log_status(0, "This packages don't need to be configured, just to be installed\n", 0)

  print_log_status(1)

  # ========== Installation Area ==========

  # Arch Essentials:
  print_log_status(1, f"Installing grub")
  install_package("grub", print_status=False)

  print_log_status(1, f"Installing efibootmgr")
  install_package("efibootmgr", print_status=False)

  print_log_status(1, f"Installing sudo")
  install_package("sudo", print_status=False)

  print_log_status(1, f"Installing git")
  install_package("git", print_status=False)

  print_log_status(1, f"Installing base-devel")
  install_package("base-devel", print_status=False)

  print_log_status(1, f"Installing networkmanager")
  install_package("networkmanager", print_status=False)

  # Video and Sound:
  print_log_status(1, f"Installing alsa-utils")
  install_package("alsa-utils", print_status=False)

  print_log_status(1, f"Installing pavucontrol")
  install_package("pavucontrol", print_status=False)

  print_log_status(1, f"Installing pulseaudio-bluetooth")
  install_package("pulseaudio-bluetooth", print_status=False)

  print_log_status(1, f"Installing vlc")
  install_package("vlc", print_status=False)

  # Internet
  print_log_status(1, f"Installing realvnc-vnc-server")
  install_package("realvnc-vnc-server", print_status=False)

  print_log_status(1, f"Installing realvnc-vnc-viewer")
  install_package("realvnc-vnc-viewer", print_status=False)

  print_log_status(1, f"Installing kdeconnect")
  install_package("kdeconnect", print_status=False)

  print_log_status(1, f"Installing ufw")
  install_package("ufw", print_status=False)

  # Coding:
  print_log_status(1, f"Installing vim")
  install_package("vim", print_status=False)

  print_log_status(1, f"Installing visual-studio-code-bin")
  install_package("visual-studio-code-bin", print_status=False)

  # print_log_status(1, f"Installing nvm")
  # install_package("nvm", print_status=False)

  # print_log_status(1, f"Installing android-studio")
  # install_package("android-studio", print_status=False)

  # Utilities:

  print_log_status(1, f"Installing wget")
  install_package("wget", print_status=False)

  # Apps:
  print_log_status(1, f"Installing firefox")
  install_package("firefox", print_status=False)

  print_log_status(1, f"Installing spotify")
  install_package("spotify", print_status=False)

  print_log_status(1, f"Installing gimp")
  install_package("gimp", print_status=False)

  print_log_status(1, f"Installing discord")
  install_package("discord", print_status=False)

  print_log_status(1, f"Installing figma-linux")
  install_package("figma-linux", print_status=False)

  print_log_status(1, f"Installing obs-studio")
  install_package("obs-studio", print_status=False)

  # Others:
  print_log_status(1, f"Installing deja-dup")
  install_package("deja-dup", print_status=False)

  print_log_status(1, f"Installing seahorse")
  install_package("seahorse", print_status=False)

  print_log_status(1, f"Installing gnome-keyring")
  install_package("gnome-keyring", print_status=False)

  # =======================================

  print_log_status(2)

  print_log_box()