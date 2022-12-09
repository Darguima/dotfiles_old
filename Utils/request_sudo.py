from Utils.run_command import run_command

def request_sudo():
  """
  Ask to the user the root password in order to, in the next 15 minutes,
    don't be needed to enter the password.

  This is made with the command `sudo true`, that just checks if 
    everything is fine with the `sudo` package, but is sufficient to
    the shell stores the root's password.
  """
  
  run_command("/usr/bin/sudo true", capture_std_out=False)
