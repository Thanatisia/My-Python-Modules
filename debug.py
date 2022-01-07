import os
import sys

def unittest(fnc, res, error_msg="Error", success_msg="Success"):
	"""
	personal_unittest
	:: Params
		fnc :
			Description: Function to test
			Type: Function

		res : 
			Description: Expected assert result
			Type: Object

		error_msg :
			Description: Error message to display if failed
			Type: String

		success_msg : 
			Description: Message if successful
			Type: String

	:: Usage
		unittest(function(args), result, "error message", "success message")
	"""
	assert fnc == res, print(error_msg)
	print(success_msg)

def main():
	print("Starting debugger...")

if __name__ == "__main__":
	main()

