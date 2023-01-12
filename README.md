# .dotfiles

Finally after 3 years of Linux and many Linux distros I created my `.dotfiles`.

## Installing

### Clone the repo

###### Only install it if you've cloned it inside `~/.dotfiles`, otherwise you'll run into problems.

```
# Por HTTPS
$ git clone https://github.com/Darguima/dotfiles ~/.dotfiles

# Por SSH
$ git clone git@github.com:Darguima/dotfiles.git ~/.dotfiles
```

### Install

Run the install script:

```
$ ~/.dotfiles/install.py
```

#### Arguments

Run the helper to learn more about the arguments:

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

Examples of commands:

> ~/.dotfiles/install.py
> ~/.dotfiles/install.py --environment laptop -o True
> ~/.dotfiles/install.py --overwrite None
```

## Packages

At this moment, this are the installed and configured packages:

1) yay
2) zsh
3) awesome
3) alacritty
