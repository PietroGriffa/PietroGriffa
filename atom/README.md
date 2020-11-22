# Atom configuration

<p align="center">
  <img src="../media/atom.png" width="150"/>
</p>

## Restore saved settings
Copy packages list ```package.list```, and configuration files ```config.cson``` and ```linter-config.json```  in the ```~/.atom/``` directory. Then synch installed packages through:

    apm install --packages-file ~/.atom/package.list

## Track installed packages
To track installed packages:

    apm list --installed --bare > ~/.atom/package.list
