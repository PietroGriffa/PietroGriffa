# Vivaldi

<p align="center">
  <img src="../media/vivaldi.png" width="150"/>
</p>

Great browser. \
To know more visit their [website](https://vivaldi.com).

## Install Vivaldi

### Option 1: from website
Visit the website and download the DEB package.

### Option 2: command line

    wget -qO- https://repo.vivaldi.com/archive/linux_signing_key.pub | gpg --dearmor | sudo dd of=/usr/share/keyrings/vivaldi-browser.gpg

    echo "deb [signed-by=/usr/share/keyrings/vivaldi-browser.gpg arch=$(dpkg --print-architecture)] https://repo.vivaldi.com/archive/deb/ stable main" | sudo dd of=/etc/apt/sources.list.d/vivaldi-archive.list

    sudo apt update && sudo apt install vivaldi-stable

## Transfer profile

Find the `Profile Path` at `vivaldi://about`. \
It's probably something on the line of `$HOME/.config/vivaldi/Default`. \
Copy it to target pc in right location to import the profile.
