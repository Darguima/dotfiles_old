# /usr/bin/bash

currentPackage="awesome"

install_package "network-manager-applet"
install_package "pa-applet-git"
install_package "acpid"
sudo systemctl enable acpid &>> $LOGFILE
install_package "network-manager-applet"
install_package "xorg-xrandr"
install_package "arandr"

git clone https://github.com/deficient/battery-widget.git $HOME/.config/awesome/battery-widget &>> $LOGFILE

install_package $currentPackage

mkdir -p ~/.config/awesome/
symlink "$DOTFILES_FOLDER/packages/awesome/dotfiles/rc.lua" $HOME/.config/awesome/rc.lua

reprint_last_line "\t-> ${bold}${currentPackage}${normal} installed and configured"