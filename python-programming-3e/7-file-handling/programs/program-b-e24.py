# EXAMPLE 7.24 : Program to demonstrate use of dirname(path) and basename(path) methods

import os

print(f"os.path.dirname({__file__}) = {os.path.dirname(__file__)}")
print(f"os.path.basename({__file__}) = {os.path.basename(__file__)}")