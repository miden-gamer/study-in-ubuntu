# MY SIDE PROGRAM - 7.3(II) : To show the use of isatty() method, example returning True.

# Python's "sys.stdout" represents standard output.
# If the program is being run directly in a terminal, you will commonly get: True, because "stdout" is connected to terminal.

import sys

if sys.stdout.isatty():
    print("Running in a terminal.")
else:
    print("Output is redirected.")