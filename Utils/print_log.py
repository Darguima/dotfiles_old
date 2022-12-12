from Utils.colors import colors

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

def print_log_status(package_name: str, status: int, print_function = print_log, indentation: int = 1):

  """
  Print standard status messages for installation and configuration process.

  Parameters
  ----------
  package_name : str
      The package being installed/configured.
  
  status: int
      The current status:

        1 - installing
        2 - installed
        3 - installed and configuring
        3 - installed and configured

  print_function: (msg: str, ...) -> Any , optional
      The print function used to output the message.
      Can be the default 'print', 'print_log', 'reprint_log', between others that respect the signature.
      Default: print_log
  
  indentation: int , optional
      How many tabs need be printed before the message

  """

  indent = "\t" * indentation

  if status == 1:
    print_function(f"{indent}-> Installing {colors.BOLD}{package_name}{colors.ENDC}")
  elif status == 2:
    print_function(f"{indent}-> {colors.BOLD}{package_name}{colors.ENDC} installed")
  elif status == 3:
    print_function(f"{indent}-> Configuring {colors.BOLD}{package_name}{colors.ENDC}")
  elif status == 4:
    print_function(f"{indent}-> {colors.BOLD}{package_name}{colors.ENDC} installed and configured")
