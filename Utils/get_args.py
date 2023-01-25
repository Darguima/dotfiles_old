from sys import argv, exit
from getopt import getopt, GetoptError

from Utils.print_log import print_log, print_log_box, print_log_status
from Utils.colors import colors

"""
Places where updated when added/changed some arg:

  -> README.md
  -> function `get_args` documentation on this file
  -> function `get_args`:
    1. add the new argument possible values
    2. add an if clause
    3. convert the value
    4. export it
"""

def print_param_info(param_flag: str, default_option: str, other_options: list[str], description: str = ""):
  params_info = f" = {colors.UNDERLINE}{default_option}{colors.ENDC}" if default_option else ""

  for param in other_options:
    params_info += f" | {param}"

  print_log(
    f"\n\t{colors.BOLD}{param_flag}{colors.ENDC}{params_info}" \
    + (f"\n{description}".replace("\n", "\n\t\t") if description else "")
  )

def print_params_error_message():
  print_log("\nInvalid parameters. Read documentation or help.")
  print_log("\n> ~/.dotfiles/install.py -h\n")
  exit()

def get_args():
  """
  Get the args passed to the script.

  -> environment = "desktop" | "laptop"
      Some dotfiles need different values from each computer to computer.
      This will create a bash variable variable `$DOTFILES_ENVIRONMENT`;
      When needed `{environment}@{filename}` dotfiles are used.
      (ex: desktop@alacritty.yml)

  -> overwrite = None | True | False
      When downloading files, repositories ... you want:
        * a fresh download? (True)
        * ignore a new download to be quick? (False)
        * let the default option for each case? (None)
  
  -> show_commands = False | True
      When downloading running commands ... you want:
        * Hide the command output and just show a summary info (False)
        * Show the original command output + summary info (True)

  Returns
  -------
  dict
      {
        environment: ...
        overwrite: ...
        show_commands: ...
      }
  """

  environment_params = ["desktop", "laptop"]
  environment = environment_params[0]

  overwrite_params = ["none", "true", "false"]
  overwrite = overwrite_params[0]

  show_commands_params = ["false", "true"]
  show_commands = show_commands_params[0]

  try:
    opts, _ = getopt(argv[1:], "he:o:s:", ["help", "environment=", "overwrite=", "show_commands="])
  except GetoptError:
    print_params_error_message()
  
  for opt, arg in opts:
    arg = arg.lower().strip()
    
    if opt in ["-h", "--help"]:
      print_log("These are the parameters that you can use:")

      print_param_info(
        "-e --environment",
        environment_params[0],
        environment_params[1:],
"""Some dotfiles need different values from each computer to computer.
This will create a bash variable variable `$DOTFILES_ENVIRONMENT`;
When needed `{environment}@{filename}` dotfiles are used.
(ex: desktop@alacritty.yml)"""
      )

      print_param_info(
        "-o --overwrite",
        overwrite_params[0],
        overwrite_params[1:],
"""When downloading files, repositories, etc. you want:
  * a fresh download? (True)
  * ignore a new download to be quick? (False)
  * let the default option for each case? (None)"""
      )

      print_param_info(
        "-s --show_commands",
        show_commands_params[0],
        show_commands_params[1:],
"""When downloading running commands ... you want:
  * Hide the command output and just show a summary info (False)
  * Show the original command output + summary info (True)"""
      )

      print_log("""
Examples of commands:

> ~/.dotfiles/install.py
> ~/.dotfiles/install.py --environment laptop -o True
> ~/.dotfiles/install.py --overwrite None -s False
""")
      exit()

    elif opt in ("-e", "--environment") and arg in environment_params:
      environment = arg
    
    elif opt in ("-o", "--overwrite") and arg in overwrite_params:
      overwrite = arg
    
    elif opt in ("-s", "--show_commands") and arg in show_commands_params:
      show_commands = arg

    else:
      print_params_error_message()
    
  # Converting params string to values
  
  if overwrite == "none":
    overwrite = None 
  elif overwrite == "true":
    overwrite = True
  elif overwrite == "false":
    overwrite = False 

  if show_commands == "true":
    show_commands = True
  elif show_commands == "false":
    show_commands = False 

  params = {
    "environment": environment,
    "overwrite": overwrite,
    "show_commands": show_commands
  }

  # Logging params
  
  print_log_box("Arguments selected")
  for key, value in params.items(): print_log_status(0, f"{key} = {value}", 0)
  print_log_box()
  
  return params

def convert_overwrite_to_bool(arg_value, default_value):
  if arg_value == True or arg_value == False:
    return arg_value
    
  elif arg_value == None:
    return default_value
