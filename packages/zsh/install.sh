# /usr/bin/bash

currentPackage="zsh"

install_package $currentPackage

symlink "$ROOT_DIR"/packages/zsh/zshrc ~/.zshrc

reprint_last_line "\t-> ${bold}${currentPackage}${normal} installed and configured"