
""" usercustomize.py

Simple series of command that can be included every time a Python interpeter is launched.

To execute this automatically every time you start an interpreter, place this file in your USER_SITE directory, which you can find as 
	import site; site._script() 

Otherwise, execute when launching a Python shell through 
	python -i usercustomize.py
"""

# Standard imports
import os
import sys
import time

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

import numpy as np

