output = ""

def print_log(msg: str):

  """
  Print a string and log it on the logfile.
  Using this function also allows you to reprint this line when using
    `reprint_log` function.

  Parameters
  ----------
  msg : str
      The string to be printed and logged.

  """

  global output

  print("\n" + msg, end="\r")
  output = msg

def reprint_log(msg: str):

  """
  Print a string over the last one and log it on the logfile.
  In order to work properly you should use `print_log` function to print
    the outputs
  This just overwrite on terminal output, on logfile a newline is appended.

  Parameters
  ----------
  msg : str
      The string to be printed and logged.

  """

  global output

  cleanSpaces = " " * (len(output) - len(msg))
  print(msg + cleanSpaces, end="\r")
  output = msg
