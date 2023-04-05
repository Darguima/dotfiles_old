from Utils.run_command import run_command

def remove(path: str, sudo: bool = False):
  """
  Remove the file or folder (and respective childs) on path.

  Parameters
  ----------
  path : str
      The file/folder
  
  sudo : bool, optional
      Needs run the `rm`command as root?
  """

  run_command(f"{'sudo' if sudo else ''} rm -rf {path}")
