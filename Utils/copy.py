from Utils.run_command import run_command
from Utils.mkdir import mkdir
from os.path import exists, dirname

def copy(src: str, dst: str, sudo: bool = False):
  """
  Copy the source to the destination.
  Uses -r flag.

  Parameters
  ----------
  src : str
      The source file/folder

  dst : str
      The destination file/folder
        
  sudo : bool, optional
      Needs run the command as root?
  """

  if (not exists(dirname(dst))): mkdir(dirname(dst), sudo=sudo)
  run_command(f"{'sudo' if sudo else ''} cp -rT {src} {dst}")
