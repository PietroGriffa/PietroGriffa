# Python

<p align="center">
  <img src="./logo.png" width="150"/>
</p>

Custom configuration for Python coding.

## Usercustomize

To launch a python interactive shell with the customize template defined in `usercustomize.py` automatically every time you start an interpreter, place this file in your USER_SITE directory, which you can find as:

    import site; site._script()

Otherwise, execute when launching a Python shell through:

    python -i usercustomize.py