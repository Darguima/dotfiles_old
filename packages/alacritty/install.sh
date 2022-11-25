# /usr/bin/bash

currentPackage="alacritty"

install_package $currentPackage

symlink "$DOTFILES_FOLDER/packages/alacritty/alacritty.yml" ~/.config/alacritty/alacritty.yml

reprint_last_line "\t-> ${bold}${currentPackage}${normal} installed and configured"