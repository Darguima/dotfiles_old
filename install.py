#! /usr/bin/python3

from Utils.request_sudo import request_sudo

from InstallationScripts import yay, alacritty

bold = "\033[1m"
normal = "\033[0m"

request_sudo()

print(f"""
Welcome to my {bold}.dotfiles{normal}.
  by {bold}Darguima{normal} 
""")

yay.install()
yay.update()

alacritty.installAndConfigure()

print("\nBye\n")
