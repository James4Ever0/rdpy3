import os
import sys

python = sys.executable

files = os.listdir(".")
for filename in files:
    if filename.startswith("test_") and filename.endswith(".py"):
        error_no = os.system(" ".join([python, "-m unittest --failfast", filename]))
        if error_no:
            print("failed at unittest: %s" % filename)
            break
