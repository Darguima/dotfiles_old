from Utils.colors import colors
from Utils.print_log import print_log

def exit_with_error(msg: str, std_err: str = None):
  """
  Log an error and exit the script. 

  Parameters
  ----------
  msg : str
      A simple message to clarify the error

  std_err : str, optional
    A complex error message, or the std_err, in case you captured it from a shell program.
    If you don't have one, just ignore it.

  Example:

  >>> exit_with_error("Erro killing the process!")

  @
  === ERROR ===
  Erro killing the process!
  =============
  @

  >>> exit_with_error("Erro killing the process!", "The process that you try kill is being used.\nTry again later!")

  @
  === ERROR ===
  Erro killing the process!

  The process that you try kill is being used.
  Try again later!

  =============
  @
  """

  print_log(f"\n=== {colors.FAIL}ERROR{colors.ENDC} ===\n"
  + msg + "\n"
  + (f"\n{std_err}\n\n" if std_err else "")
  + "=============\n")
  exit()
