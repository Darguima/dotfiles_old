from Utils.run_command import run_command

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

  run_command(f"{'sudo' if sudo else ''} cp -r {src} {dst}")
