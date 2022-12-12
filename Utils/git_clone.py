from Utils.run_command import run_command
from Utils.errorExit import exit_with_error
from os.path import exists
from shutil import rmtree

def git_clone(path: str, dst_folder: str, host="https://github.com", overwrite: bool = False):
  """
  Clone a git repository.

  Parameters
  ----------
  path : str
    The path inside the git host.
    For example, to clone this dotfiles, use 'Darguima/dotfiles.git' from 'https://github.com/Darguima/dotfiles.git' 

  dst_folder : str
    The destination where clone the repository
  
  host : str, optional
    The url of the repository host.
      Default: 'https://github.com'
  
  overwrite : bool, optional
    In case the destination folder already exists, it will be overwritten if True, or ignored if False.
    Default: False

  Returns
  -------
  int
      0 = cloned (clean)
      1 = not cloned (ignored)
      2 = cloned (overwritten)
  """

  if not exists(dst_folder):
    run_command(f"git clone {host}/{path} {dst_folder}")
    return 0

  elif not overwrite:
    return 1

  else: # if overwrite:
    rmtree(dst_folder, onerror=(lambda _, __, err: exit_with_error("Error trying to delete the existent destination folder.", err[1])))
    run_command(f"git clone {host}/{path} {dst_folder}")
    return 2
