from Utils.colors import colors

logfile = open("log.txt", "w")

def prepare_command_log(msg: str, command: str):
  """
  Log a string on the logfile.
  Will be used a blue text to differentiate from normal text

  Parameters
  ----------
  msg : str
      The output of the command

  command : str
    The command used to get the output (msg)
  """

  if msg.strip() != "":
    msg += "\n"
    
  pre_msg = \
f"""{colors.OKBLUE}===
> {command}
==={colors.OKCYAN}
"""

  msg = msg.replace(colors.ENDC, colors.ENDC + colors.OKCYAN)

  if msg.strip() != "":
    pos_msg = f"{colors.OKBLUE}==={colors.ENDC}\n"
  else:
    pos_msg =  colors.ENDC

  msg = pre_msg + msg + pos_msg

  return msg

def log(msg: str, command=""):
  """
  Log a string on the logfile.

  Parameters
  ----------
  msg : str
      The string to log on the file

  command : str, optional
    The command used to get the output (msg)
    If passed, will be used a blue text to differentiate from normal text
  """

  if command:
    msg = prepare_command_log(msg, command)
  
  if msg.strip() != "":
    msg += "\n"

  logfile.write(msg)
