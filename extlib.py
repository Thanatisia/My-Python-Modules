"""
Program Name: External Library
- A universal, portable, reusable, versatile library containing various useful everyday functions, classes and variables

:: How to use?
	- Copy this into your project's module folder
	- Import this library/module
	- extlib.{class|function|variable}(<parameters>)
"""

# Import modules
import os
import sys
from importlib import import_module
from pathlib import Path
import sqlite3 as db


def importlib(self, mod_name=None):
	"""
	Import Module only when needed

	:: Params
		mod_name
			Type: String
			Description: Module Name
	"""
	module = None
	if not (mod_name == ""):
		module = import_module(mod_name)
	return module

def get_currentfile_dir():
	""" Get the parent directory of the current source file
	__file__ : Path of your source file
	
	:: Syntax
		Path({path-to-file}).parent
	"""
	parent_dir = Path(__file__).parent
	return parent_dir

def get_parent_dir(file_path=__file__, jumps=1):
	""" Get the parent directory of a file/folder
	:: Params
		file_path
			Description: The path of the file/folder you want to get the parent directory of
			Type: String
			Default: __file__ = Your current source file

		jumps
			Description: Number of parent directories you want to go backwards
			Type: Integer
			Default: 1

	:: Syntax
		Path({path-to-file}).parent
	"""
	curr_dir = file_path
	for i in range(jumps):
		curr_dir = Path(curr_dir).parent
	return curr_dir

def init():
	"""
	Initialize on startup
	- Variables
	- Import modules
	"""
	print("Starting debug function...")

def setup():
	init()

def main():
	"""
	Debug function
	"""
	print("Initialized")

	
if __name__ == "__main__":
	# Run functions
	setup()
	main()