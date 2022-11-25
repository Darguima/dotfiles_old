# /usr/bin/bash

currentPackage="awesome"

install_package $currentPackage

mkdir -p ~/.config/awesome/
symlink "$DOTFILES_FOLDER/packages/awesome/dotfiles/rc.lua" ~/.config/awesome/

reprint_last_line "\t-> ${bold}${currentPackage}${normal} installed and configured"