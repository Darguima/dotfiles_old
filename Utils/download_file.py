from Utils.errorExit import exit_with_error
from os.path import exists, dirname
from os import makedirs

import urllib.request

def download_file(url: str, dst_file: str, overwrite: bool = False):
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

  Returns
  -------
  int
      0 = downloaded (with no problems)
      1 = not downloaded (ignored)
      2 = downloaded (overwritten)
  """

  parent_folder = dirname(dst_file)
  if not exists(parent_folder): makedirs(parent_folder)

  if not exists(dst_file):
    try:
      urllib.request.urlretrieve(url, dst_file)
    except Exception as err:
      exit_with_error("Error trying to download the file.", err)
    return 0

  elif not overwrite:
    return 1

  else: # if overwrite:

    try:
      urllib.request.urlretrieve(url, dst_file)
    except Exception as err:
      exit_with_error("Error trying to overwrite the existent destination file.", err)

    return 2
