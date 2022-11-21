# /usr/bin/bash

function clear_log () {
  echo "" > $LOGFILE
}

function print () {
  echo -e "$1" | tee -a $LOGFILE
}

function reprint_last_line () {
  echo -en "\e[1A\e[K"
  echo -e "$1" | tee -a $LOGFILE
}

function symlink() {
  local SRC="$1"
  local DST="$2"

  mkdir -p $(dirname ${DST})
  ln -sfT ${SRC} ${DST}
}
