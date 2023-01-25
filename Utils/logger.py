from Utils.colors import colors

logfile = open("log.txt", "w")

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

  if msg.strip() != "":
    msg += "\n"
    
  if command:
    pre_msg = \
f"""{colors.OKBLUE}===
> {command}
==={colors.OKCYAN}
"""

    msg = msg.replace(colors.ENDC, colors.ENDC + colors.OKCYAN)

    pos_msg = f"{colors.OKBLUE}==={colors.ENDC}\n" if msg.strip() != "" else colors.ENDC

    msg = pre_msg + msg + pos_msg + "\n"

  logfile.write(msg)
