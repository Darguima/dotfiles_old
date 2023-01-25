from subprocess import call, getstatusoutput
from Utils.errorExit import exit_with_error
from Utils.logger import log
from Utils.colors import colors

def run_command(command: str, capture_std_out=True, exit_on_error=True):
  """
  Run a shell command

  Parameters
  ----------
  command : str
      The bash command to be executed

  capture_std_out : bool, optional
    It can capture (True) or not (False) the command's output, in order to hide or show
      it. If you capture, the output will not be printed and will be returned.

  exit_on_error : bool, optional
    If the command is crucial to the script you can stop it when some one runs 
      into an error. If you want that the script stops when a command return an
      error code use `True`, otherwise, use `False`.

  Returns
  -------
  tuple
      (return_code, stdout)
  """

  stdout = ""
  return_code = 0
  
  if capture_std_out:
    [return_code, stdout] = getstatusoutput(command)
    log(stdout, command)
  else:
    try:
      return_code = call(command.split(" "))
    except:
      return_code = 1

  if exit_on_error and return_code != 0:
    exit_with_error(f"Error running command - {colors.UNDERLINE}{command}{colors.ENDC}", stdout)
  else:
    return (return_code, stdout)
