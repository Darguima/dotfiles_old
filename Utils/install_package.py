from Utils.print_log import print_log, reprint_log
from Utils.run_command import run_command
from Utils.colors import colors



def install_package(package_name: str, package_dependencies: list[str] = []):
  """
  Install a pacman/AUR package. 

  Parameters
  ----------
  package_name : str
    The package name to be installed.
    Should be a valid  package name, recognized by yay.

  package_dependencies : list[str], optional
    A string list of others packages that eventually are needed to everything
      work properly.
  """
  
  print_log(f"\t-> Installing {colors.BOLD}{package_name}{colors.ENDC}")
  run_command(f"yay -S {package_name} --needed --noconfirm")

  if len(package_dependencies) == 0:
    reprint_log(f"\t-> {colors.BOLD}{package_name}{colors.ENDC} installed")
  else:
    print_log(f"\t\t-> Installing {len(package_dependencies)} {'dependencies' if len(package_dependencies) != 1 else 'dependency'}:")

    for dependency in package_dependencies:
      print_log(f"\t\t\t-> {dependency}")
      run_command(f"yay -S {dependency} --needed --noconfirm")

    print_log(f"\t\t-> {colors.BOLD}{package_name}{colors.ENDC} installed")
    
