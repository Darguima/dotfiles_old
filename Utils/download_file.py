from Utils.errorExit import exit_with_error
from Utils.run_command import run_command
from os.path import exists, dirname
from os import makedirs

import urllib.request

def download_file(url: str, dst_file: str, overwrite: bool = False, sudo = False):
  """
  Download a file from web.

  Parameters
  ----------
  url : str
    The url for the file

  dst_file : str
    The path of the downloaded file.
  
  overwrite : bool, optional
    In case the destination file already exists, it will be overwritten if True, or ignored if False.
    Default: False
  
  sudo : bool , optional
    Tu run the command as root, set to True
    Default: False

  Returns
  -------
  int
      0 = downloaded (with no problems)
      1 = not downloaded (ignored)
      2 = downloaded (overwritten)
  """

  parent_folder = dirname(dst_file)
  try:
    # makedirs(parent_folder, exist_ok=True)
    run_command(f"{'sudo' if sudo else ''} mkdir -p {parent_folder}")
  except Exception as err:
    exit_with_error("Error creating the parent path.", err)
  

  if not exists(dst_file):
    try:
      # urllib.request.urlretrieve(url, dst_file)
      run_command(f"{'sudo' if sudo else ''} wget -O '{dst_file}' '{url}'")
    except Exception as err:
      exit_with_error("Error trying to download the file.", err)
    return 0

  elif not overwrite:
    return 1

  else: # if overwrite:

    try:
      # urllib.request.urlretrieve(url, dst_file)
      run_command(f"{'sudo' if sudo else ''} wget -O '{dst_file}' '{url}'")
    except Exception as err:
      exit_with_error("Error trying to overwrite the existent destination file.", err)

    return 2
