from Utils.run_command import run_command

def mkdir(path: str, sudo: bool = False, parents: bool = True):
  """
  Create a directory on the given path

  Parameters
  ----------
  path : str
      The new folder path
  
  sudo : bool, optional
      Needs run the `mkdir`command as root?

  parents : bool, optional
        If True, will not raise an error if the folder already exists
            and will make parent directories as needed.
  """

  run_command(f"{'sudo' if sudo else ''} mkdir {'-p' if parents else ''} {path}")
