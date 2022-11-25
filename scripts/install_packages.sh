# /usr/bin/bash

function install_yay() {
  if ! command -v yay &> /dev/null
  then
    print "\t-> Installing ${bold}yay${normal}"

    reprint_last_line "\t-> Installing ${bold}yay${normal} (pacman -S git base-devel)"
    sudo pacman -S --needed --noconfirm git base-devel &>> $LOGFILE

    reprint_last_line "\t-> Installing ${bold}yay${normal} (git clone)"
    git clone https://aur.archlinux.org/yay.git "$TEMPPATH/yay" &>> $LOGFILE

    reprint_last_line "\t-> Installing ${bold}yay${normal} (makepkg)"
    cd "$TEMPPATH/yay" &>> $LOGFILE
    makepkg -si --noconfirm &>> $LOGFILE

  else
    print "\t-> ${bold}yay${normal} already installed"
  fi
}

function update_yay() {
  print "\t-> ${bold}yay${normal} updating"

  yay -Suy --noconfirm &>> $LOGFILE

  reprint_last_line "\t-> ${bold}yay${normal} updated"
}

function install_package() {
  local PKG="$1"

  print "\t-> Installing ${bold}${PKG}${normal}"

  yay -S ${PKG} --needed --noconfirm &>> $LOGFILE

  reprint_last_line "\t-> ${bold}${PKG}${normal} installed"
}

function install_packages () {
  print "Starting Packages Instalation:"
  
  install_yay
  update_yay

  # Run all sub folders with file `install.sh`
  local subDirs=$(find ./packages -maxdepth 1 -mindepth 1 -type d -print | sed -e 's/.\///')

  for dir in $subDirs; do
    if [ -f "$dir/install.sh" ]; then
      . "${dir}"/install.sh
      # will call `install_package` function
    fi
  done
}

packages=(
  grub
  efibootmgr
  xorg-server
  base-devel
  sudo
  git
  wget
  zsh
  networkmanager
  alsa-utils
  pavucontrol
  pulseaudio-bluetooth
  vim
  visual-studio-code-bin
  firefox
  vlc
  deja-dup
  ufw
  kdeconnect
  seahorse
  gnome-keyring
  realvnc-vnc-server
  realvnc-vnc-viewer
  spotify
  gimp
  discord
  figma-linux
  obs-studio
  # nvm
  # android-studio
)

KDE=(
  packagekit-qt5
)

LAPTOP=()

DESKTOP=(
  nvidia
)

