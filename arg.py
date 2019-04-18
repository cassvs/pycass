# arg.py
# Various utilities for dealing with command-line arguments

import sys

# Return the argument at a specified index, or a default value
def getarg(index, default):
    if len(sys.argv) >= index + 1:
        return sys.argv[index]
    else:
        return default
# End of getarg function
