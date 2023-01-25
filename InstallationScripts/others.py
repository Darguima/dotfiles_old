from Utils.print_log import print_log_box, print_log_status
from Utils.install_package import install_package

"""
  Templates:

  * Installing packages without dependencies:
  
  print_log_status(1, f"Installing xxx")
  install_package("xxx", print_status=False)
  
  * Installing packages with dependencies:
  
  print_log_status(1, f"Installing xxx")
  print_log_status(1, f"Installing dependency xxx", indentation=2)
  install_package("xxx", ["xxx"], print_status=False)
"""

def installAndConfigure(CONSTANTS: dict, args: dict):
  """
  This packages don't need to be configured, just to be installed
  """

  print_log_box("Others")

  print_log_status(0, "This packages don't need to be configured, just to be installed\n", 0)

  print_log_status(1)

  # ========== Installation Area ==========

  print_log_status(1, f"Installing gimp")
  install_package("gimp", print_status=False)

  # =======================================

  print_log_status(2)

  print_log_box()
