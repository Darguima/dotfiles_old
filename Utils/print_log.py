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

def print_log_box(package_name: str = "", box_size = 30):

  """
  Print box to visual division between packages installation.

  Parameters
  ----------
  package_name : str
      The package being installed/configured.
  
  box_size: int , optional
      How many characters will have de box. For example, 30, will print 30 chars.
  """

  if package_name != "":
    print_log(f"\n=== {colors.BOLD}{package_name}{colors.ENDC} " + "=" * (box_size - 5 - len(package_name)))
  else:
    print_log("=" * box_size)

def print_log_status(status: int, message = "", indentation: int = 1):

  """
  Print standard status messages for installation and configuration process.

  Parameters
  ----------
  status: int
      The current status:

        1 - installing
        2 - installed
        3 - installed and configuring
        4 - installed and configured

        5 - updating
        6 - updated

        12 - already installed
  
  message: int , optional
      A status message. This message will be shown as a subtitle of the status,
        indented, to give more information.

  indentation: int , optional
      How many tabs need be printed before the message
      Default 1 (+ 1 when message != "")

  """

  indent = "\t" * (indentation + (1 if message != "" else 0) )

  if message != "":
    print_log(f"{indent}-> {message}")


  elif status == 1:
    print_log(f"{indent}-> Installing")
  elif status == 2:
    print_log(f"{indent}-> Installed")
  elif status == 3:
    print_log(f"{indent}-> Configuring")
  elif status == 4:
    print_log(f"{indent}-> Installed and Configured")

  elif status == 5:
    print_log(f"{indent}-> Updating")
  elif status == 6:
    print_log(f"{indent}-> Updated")

  elif status == 12:
    print_log(f"{indent}-> Already Installed")
