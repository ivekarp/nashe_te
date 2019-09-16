#! /usr/bin/env python

from termcolor import colored

def print_logo():
	logo = """
_  _ ____ ____ _  _ ____    ____ ____ ___  _ ____ 
|\ | |__| [__  |__| |___    |__/ |__| |  \ | |  | 
| \| |  | ___] |  | |___    |  \ |  | |__/ | |__| 
___ ____ ____ _  _ _ _  _ ____ _       ____ ___  _ ___ _ ____ _  _ 
 |  |___ |__/ |\/| | |\ | |__| |       |___ |  \ |  |  | |  | |\ | 
 |  |___ |  \ |  | | | \| |  | |___    |___ |__/ |  |  | |__| | \| 
"""
	print(colored(logo,'green','on_red',attrs=['bold']))

def main():
	info = """
	Logo maded with art (python package).
	"""
	print(info)

if __name__ == '__main__':
	main()

