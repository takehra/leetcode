import os
import sys

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
root_directory = os.path.abspath(os.path.join(script_directory, ".."))
sys.path.append(root_directory)
