# -*- coding: utf-8 -*-
#! /usr/bin/env python

import vlc
import json
import requests
from bs4 import BeautifulSoup as bs
from termcolor import colored
from sys import exit
from logo import print_logo, print_help, print_special

#Variables
radio_url = 'http://nashe1.hostingradio.ru:80/nashe-128.mp3'

#Version
VERSION = '1.0'

#define vlc instance
instance = vlc.Instance('--input-repeat=-1','--fullscreen')

#define vlc player
player = instance.media_player_new()

#define vlc media
media = instance.media_new(radio_url)

#set player media
player.set_media(media)

#Functions
def play(player):
	#clear()
	player.play()
	print('Вы слушаете "НАШЕ Радио"')

def stop(player):
	#clear()
	player.stop()
	print('Радио остановлено')

def choosing():
	while True:
		choose = raw_input('Выберите действие: ')
		if str(choose) == '1':
			#play radio
			play(player)
		#special commands
		elif str(choose) == 'h':
			clear()
			print_help()
		elif str(choose) == 'help':
			clear()
			print_help()
		elif str(choose) == '?':
			clear()
			print_help()
		elif str(choose) == 'special':
			print_special()
		elif str(choose) == 'clear':
			clear()
		elif str(choose) == 'cls':
			clear()
		elif str(choose) == 'exit':
			exit()
		elif str(choose) == 'quit':
			exit()
		elif str(choose) == 'news':
			show_news()
		elif str(choose) == 'who':
			who_sings()
		elif str(choose) == 'volume':
			volume_change(player)
		elif str(choose) == 'about':
			about()
		elif str(choose) == 'play':
			play(player)
		elif str(choose) == 'stop':
			stop(player)
		#------------------
		elif str(choose) == '2':
			#stop radio
			stop(player)
		elif str(choose) == '3':
			#singer and song info
			who_sings()
		elif str(choose) == '4':
			#show news
			show_news()
		elif str(choose) == '5':
			#volume
			volume_change(player)
		elif str(choose) == '6':
			#about
			about()
		elif str(choose) == '7':
			#exit
			exit()
		else:
			print('Неверная команда! (Введите h или help для показа помощи)')
			choosing()

def who_sings():
	#singer and name of song
	singer_url = 'http://metanashe.hostingradio.ru/current.json'
	response = requests.get(singer_url)
	data = json.loads(response.text)
	try:
		singer = data["artist"]
		song = data["title"]
		print(colored("В эфире: ",'green'))
		print(colored(u'{} - {}','white','on_green',attrs=['bold']).format(singer,song))
	except KeyError:
		pass

def clear():
	print('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n''')

def show_news():
	print(colored('Новости с nashe.ru :','white','on_red',attrs=['bold']))
	url = 'https://www.nashe.ru/news/'
	html = requests.get(url).text
	soup = bs(html,'lxml')
	news = soup.find_all('a',{'class':'news__item'})
	for n in news:
		news_title = n.find('span',{'class':'news__name'})
		news_link = n
		print(colored(news_title.text,'grey','on_white',attrs=['bold']))
		print(colored(news_link.get('href'),'white','on_green',attrs=['bold']))

def volume_change(player):
	try:
		volume = input('Введите значение громкости (0-100): ')
		if int(volume)>=0 and int(volume)<=100:
			player.audio_set_volume(int(volume))
			print(u'Установлена громкость: {}'.format(volume))
		else:
			print('Введите значение в диапазоне 0-100 ')
		if int(volume) == 0:
			print('Звук отключен')
	except ValueError:
		print('Введено некорректное значение!')

def about():
	text = '''
			____ ___  ____ _  _ ___ 
			|__| |__] |  | |  |  |  
			|  | |__] |__| |__|  |  
	'''
	info = '''
	Онлайн-радио радиостанции "НАШЕ Радио" (версия для терминала).
		Разработчик - Иван Карпов
		vanhelsing66677@gmail.com
	'''

	print(colored(text,'white','on_green',attrs=['bold']))
	print(colored(info,'green',attrs=['bold']))

#Code
try:
	print_logo()
	print('								'+colored(VERSION,'green',attrs=['bold']))
	player.audio_set_volume(100)
	print_help()
	choosing()
except KeyboardInterrupt:
	print(colored('\nАварийное завершение программы','red',attrs=['bold']))
	exit()
