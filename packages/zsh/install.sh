# /usr/bin/bash

currentPackage="zsh"

install_package $currentPackage

ZSH_CUSTOM=${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}

reprint_last_line "\t-> ${bold}${currentPackage}${normal} (Installing Oh-My-ZSH)"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" &>> $LOGFILE

reprint_last_line "\t-> ${bold}${currentPackage}${normal} (Clonning zsh-autosuggestions)"
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions &>> $LOGFILE

reprint_last_line "\t-> ${bold}${currentPackage}${normal} (Clonning zsh-syntax-highlighting)"
git clone https://github.com/zsh-users/zsh-syntax-highlighting $ZSH_CUSTOM/plugins/zsh-syntax-highlighting &>> $LOGFILE

reprint_last_line "\t-> ${bold}${currentPackage}${normal} (Installing Meslo Nerd Font)"
sudo mkdir -p /usr/share/fonts/MesloLGS
sudo wget -P "/usr/share/fonts/MesloLGS" https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf &>> $LOGFILE
sudo wget -P "/usr/share/fonts/MesloLGS" https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf &>> $LOGFILE
sudo wget -P "/usr/share/fonts/MesloLGS" https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf &>> $LOGFILE
sudo wget -P "/usr/share/fonts/MesloLGS" https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf &>> $LOGFILE

reprint_last_line "\t-> ${bold}${currentPackage}${normal} (Clonning powerlevel10k)"
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM}/themes/powerlevel10k &>> $LOGFILE

symlink "$DOTFILES_FOLDER/packages/zsh/dotfiles/zshrc" ~/.zshrc
symlink "$DOTFILES_FOLDER/packages/zsh/dotfiles/p10k.zsh" ~/.p10k.zsh

reprint_last_line "\t-> ${bold}${currentPackage}${normal} (Changing default shell)"
sudo chsh --shell $(command -v zsh) $USER &>> $LOGFILE

reprint_last_line "\t-> ${bold}${currentPackage}${normal} installed and configured"