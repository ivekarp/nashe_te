# -*- coding: utf-8 -*-
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

def print_help():
	info = '''
		_  _ ____ _    ___  
		|__| |___ |    |__] 
		|  | |___ |___ |    
		'''
	help = '''
		help),h),?) Помощь
		special) Дополнительные команды
		1) Включить радио
		2) Выключить радио
		3) Кто поёт?
		4) Новости
		5) Изменить громкость
		6) О программе
		7) Выйти из программы
		'''	
	print(colored(info,'grey','on_white',attrs=['bold']))
	print(help)

def print_special():
	info = '''
						____ ___  ____ ____ _ ____ _    
						[__  |__] |___ |    | |__| |    
						___] |    |___ |___ | |  | |___ 
                                

	'''
	special = '''
~~~~~~~~Специальные команды~~~~~~~~
			clear), cls) Очистить терминал
			exit) , quit) Выйти из программы 
			news) Новости 
			play) Включить радио
			stop) Выключить радио
			who) Кто поёт?
			volume) Изменить громкость
			about) О программе
		
		'''

	print(colored(info,'green','on_grey',attrs=['bold']))
	print(special)

def main():
	info = """
	Logo maded with art (python package).
	"""
	print(info)

if __name__ == '__main__':
	main()

