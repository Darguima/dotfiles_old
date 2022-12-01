from subprocess import call, getstatusoutput

def run_command(command: str, captureStdOut=True, exit_on_error=True):
  """
  This function will run a shell command. 
  
  * captureStdOut
  It can capture or not the command's output, in order to hide or show
    it. This can be done passing 'True' to `captureStdOut` to hide the output 
    or 'False' to show it.

  * captureStdOut
  If the command is crucial to the script you can stop it when some one runs 
    into an error. If you want that the script stops when a command return an
    error code use `True` on `exit_on_error`, otherwise, use `False`.
  """

  stdout = ""
  if captureStdOut:
    [return_code, stdout] = getstatusoutput(command)
  else:
    try:
      return_code = call(command.split(" "))
    except:
      return_code = 1

  if return_code == 0:
    return stdout
  elif exit_on_error:
    exit()
