from Utils.run_command import run_command
from Utils.remove import remove
from Utils.mkdir import mkdir
from os.path import exists, dirname

def create_sym_link(source_file: str, dest_folder: str, dest_file: str = "", sudo: bool = False):
    """
    Create a symbolic link from a file (or all files * ), on a file path.
    Will overwrite any existent file.

    Usage
    ----------
    create_sym_link("~/test/f1/1.txt", "~/test/f2")
    Links the file `~/test/f1/1.txt` on the file `~/test/f2/1.txt`

    create_sym_link("~/test/f1/1.txt", "~/test/f2", "2.txt")
    Links the file `~/test/f1/1.txt` on the file `~/test/f2/2.txt`

    create_sym_link("~/test/f1/*", "~/test/f2")
    Links all the files in `~/test/f1/` on the `~/test/f2` folder (the files will have te same name)

    Parameters
    ----------
    source_file : str
      The source file to be linked on the destination folder.

    dest_folder : str
      The destination folder where the links files gonna be created.

    dest_file : str , optional
      The destination file that gonna be create inside `dest_folder`.
      If not given will be used the source file name.
    
    sudo : bool , optional
      To run the command as root, set to True
      Default: False
    """

    if (not exists(dest_folder)): mkdir(dest_folder, sudo=sudo)

    run_command(f"{'sudo' if sudo else ''} ln -sf {source_file} {dest_folder}/{dest_file}")

def create_folder_link(source_folder: str, dst_folder: str, sudo: bool = False):
    """
    Create a symbolic link from a folder to other folder.
    Will delete any existent file and folder on the `dst_folder`.

    Parameters
    ----------
    source_folder : str
      The source folder to be linked on the destination folder.

    dst_folder : str
      The destination folder where the linked folder gonna be created.
      All files that are childs of this path gonna be removed.

    sudo : bool , optional
      To run the command as root, set to True
      Default: False
    """

    if (not exists(dirname(dst_folder))): mkdir(dirname(dst_folder), sudo=sudo)
    remove(dst_folder, sudo=sudo)
    
    run_command(f"{'sudo' if sudo else ''} ln -sf {source_folder} {dst_folder}")
