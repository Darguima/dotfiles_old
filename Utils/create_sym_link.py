from Utils.run_command import run_command
from os.path import dirname

def create_sym_link(source_file: str, dest_file: str, sudo: bool = False, dest_is_directory: bool = False):
  """
  Create a symbolic link file. Can be used to link the dotfiles.

  Parameters
  ----------
  source_file : str
    The source file to be linked on the destination folder.

  dest_file : str
    The destination file where will be created a link to the source file.
  
  sudo : bool , optional
    To run the command as root, set to True
    Default: False

  dest_is_directory : bool , optional
    If the `dest_file` is actually a directory, and not the file name to the link.
    This will create a link file with the same name of `source_file` on the target directory.
    Default: False
  """
  
  parent_dir = dirname(dest_file) if not dest_is_directory else dest_file
  run_command(f"{'sudo' if sudo else ''} mkdir -p {parent_dir}")
  run_command(f"{'sudo' if sudo else ''} ln -sf {source_file} {'-T' if not dest_is_directory else '-t'} {dest_file}")
