# Oh My Zshell

<p align="center">
  <img src="./logo.png" width="150"/>
</p>

Great framework for managing zsh, which is the shell I use more frequently. \
To know more visit their [website](https://ohmyz.sh/).

## Install

### Install Zshell

    sudo apt install zsh

To set up zsh as default shell

    chsh -s $(which zsh)

### Install Oh My Zshell

    $ sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

#### Agnoster theme

To set the agnoster theme, set the `ZSH_THEME` variable in `.zshrc`

    ZSH_THEME="agnoster"

To use the agnoster theme make sure o have the powerline fonts installed.

    sudo apt-get install fonts-powerline


## Configuration

TODO

## Requirements

Clone the repositories for autocompeltion and syntax highlighting plugins

    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

The `chuck` plugin requires the fortuna and cowsay packages installed:

      sudo apt-get install fortune cowsay