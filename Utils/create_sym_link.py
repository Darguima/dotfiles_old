from Utils.run_command import run_command
from os import makedirs
from os.path import dirname

def create_sym_link(source_file: str, dest_file: str, sudo: bool = False):
  """
  Create a symbolic link file. Can be used to link the dotfiles.

  Parameters
  ----------
  source_file : str
    The source file to be linked on the destination folder.

  dest_file : str
    The destination file where will be created a link to the source file.
  
  sudo : bool , optional
    Tu run the command as root, set to True
    Default: False
  """
  
  makedirs(dirname(dest_file), exist_ok=True)
  run_command(f"{'sudo' if sudo else ''} ln -sfT {source_file} {dest_file}")
