from Utils.run_command import run_command
from Utils.print_log import print_log_status

class systemctl():
  """
  Class with the 6 most useful commands from `systemctl`.

    1. status
    2. start
    3. restart
    4. stop
    5. enable
    5. disable

  #### Ex:

  ```python
    from Utils.systemctl import systemctl
    systemctl.enable("service name")
  ```

  """
  def status(service_name: str, print_action: bool = True):
    """
    Return the status from a Unit Service.

    Parameters
    ----------
    service_name : str

    print_action : bool , optional
        If True, the function will print a message with the action and the service name.

    Returns
    -------
    int
        0 = running / OK

        1 = dead - /var/run pid file exists

        2 = dead - /var/lock lock file exists

        3 = not running

        4 = unknown

    ###### https://www.freedesktop.org/software/systemd/man/systemctl.html#Exit%20status
    """

    if print_action:
      print_log_status(3, f"Requesting status from `{service_name}`")
    
    (err_code, _) = run_command(f"sudo systemctl status {service_name}", exit_on_error=False)

    return err_code
  
  def start(service_name: str, print_action: bool = True):
    """
    Starts a Unit Service.

    Parameters
    ----------
    service_name : str

    print_action : bool , optional
        If True, the function will print a message with the action and the service name.
    """

    if print_action:
      print_log_status(3, f"Starting `{service_name}`")
    
    run_command(f"sudo systemctl start {service_name}")
  
  def restart(service_name: str, print_action: bool = True):
    """
    Restarts a Unit Service.

    Parameters
    ----------
    service_name : str

    print_action : bool , optional
        If True, the function will print a message with the action and the service name.
    """

    if print_action:
      print_log_status(3, f"Restarting `{service_name}`")
    
    run_command(f"sudo systemctl restart {service_name}")
  
  def stop(service_name: str, print_action: bool = True):
    """
    Stops a Unit Service.

    Parameters
    ----------
    service_name : str

    print_action : bool , optional
        If True, the function will print a message with the action and the service name.
    """

    if print_action:
      print_log_status(3, f"Stopping `{service_name}`")
    
    run_command(f"sudo systemctl stop {service_name}")

  def enable(service_name: str, print_action: bool = True):
    """
    Enables a Unit Service.

    Parameters
    ----------
    service_name : str

    print_action : bool , optional
        If True, the function will print a message with the action and the service name.
    """
      
    if print_action:
      print_log_status(3, f"Enabling `{service_name}`")
    
    run_command(f"sudo systemctl enable {service_name}")
  
  def disable(service_name: str, print_action: bool = True):
    """
    Disables a Unit Service.

    Parameters
    ----------
    service_name : str

    print_action : bool , optional
        If True, the function will print a message with the action and the service name.
    """

    if print_action:
      print_log_status(3, f"Disabling `{service_name}`")
    
    run_command(f"sudo systemctl disable {service_name}")
