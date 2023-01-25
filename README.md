# .dotfiles

Finally after 3 years of Linux and many Linux distros I created my `.dotfiles`.

Here you will find a Python Environment, with a set of utils, to create your dotfiles, or you can just clone and install mine.

## Installing 🐧

### Clone the repo 📥

###### ⚠️ Only install it if you've cloned it inside `~/.dotfiles`, otherwise you'll run into problems. ⚠️

```
# With HTTPS
$ git clone https://github.com/Darguima/dotfiles ~/.dotfiles

# With SSH
$ git clone git@github.com:Darguima/dotfiles.git ~/.dotfiles
```

### Install 🚀

Run the install script:

```
$ ~/.dotfiles/install.py
```

#### Arguments

Run the helper to learn more about the possible arguments:

```
$ ~/.dotfiles/install.py -h
```

```
These are the parameters that you can use:

	-e --environment = desktop | laptop
		Some dotfiles need different values from each computer to computer.
		This will create a bash variable variable `$DOTFILES_ENVIRONMENT`;
		When needed `{environment}@{filename}` dotfiles are used.
		(ex: desktop@alacritty.yml)

	-o --overwrite = none | true | false
		When downloading files, repositories, etc. you want:
		  * a fresh download? (True)
		  * ignore a new download to be quick? (False)
		  * let the default option for each case? (None)

	-s --show_commands = false | true
		When downloading running commands ... you want:
		  * Hide the command output and just show a summary info (False)
		  * Show the original command output + summary info (True)

Examples of commands:

> ~/.dotfiles/install.py
> ~/.dotfiles/install.py --environment laptop -o True
> ~/.dotfiles/install.py --overwrite None -s False
```

### Packages 📦

At this moment, this are the installed and configured packages:

1) yay
2) zsh
3) awesome
3) alacritty

But you can add/edit your favorite packages. Learn below how this project is structured and feel free to modify it.

## How it works? ⚙⚙

Now if you are interested to know how are this dotfiles organized, or want to modify something here is a summary:

### Project Structure 📂

To start this is the file tree of this project:

* __InstallationScripts__ - here each package have it's own script. Is where we install the packages and dependencies and configure everything. 

* __dotfiles__ - here, each package have it's own folder, with the needed dotfiles. The installation scripts will link the apps dotfiles to their correspondent here

* __Utils__ - here, you can find a set of Python Modules that will help you writing yours Installation Scripts. Every function is documented and well named, so just check the files for more information. You can find for example: `create_sym_link`, `install_package`, `print_log`, `run_command`, ...

* __install.py__ - and finally the center of everything, the main script file. This file prepare everything and call each installation script

### Creating a new package installation script ➕

#### The script

First of all start by copying the template file from `InstallationScripts/template/template.py` to `InstallationScripts/example.py`

Edit the `install_package` with the package name and add the needed dependencies.

Edit and uncomment the `create_sym_link`, if needed, to the respective file. Don't forget to save it under the __dotfiles__ folder, on its respective folder.

Now if you need download some extra files or Github repositories, start/enable some services, etc. you can use, the Utils scripts. If you don't find the perfect one for your case, just run the shell command, with `Utils/run_command` to finish the configuration. Try respect the logs/prints areas (read more below).

#### The logs/prints

One of my goals was try have a good text return of the installation status, not only command outputs or a void terminal.

When writing yours installation script you should use `print_log_status(x, "msg")` functions to return the status of the installation. If you check ths function documentation you will find more about how use it. Try use it every time you do something different, creating groups of similar commands and "documenting" it with this function. This will be helpful when running the script to now the current status and to know what are you editing.

##### Logs

The terminal output, and the commands output, are stored inside the log file (usually stored at ~/.dotfiles/log.txt). If something goes wrong and you want to know why, you can read it any time. Just do it with `cat` command for a better experience.
