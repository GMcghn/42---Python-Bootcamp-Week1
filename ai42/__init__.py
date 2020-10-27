# The __init__.py file is necessary because with this file, Python will know that 
# this directory is a Python package directory other than an ordinary directory 
# (or folder – whatever you want to call it). Anyway, it is in this file where 
# we'll write some import statements to import classes from our brand new package.

#VS me met un problem mais ça marche quand même
    #https://stackoverflow.com/questions/55643859/pylint-import-error-while-import-a-module-in-the-same-folder-with-vscode

from loading import *
from logger import *

