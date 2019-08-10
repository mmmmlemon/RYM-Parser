#! /usr/bin/env python
# -*- coding: utf-8 -*-
#импорт библиотеки для чтения с кодировками
import io
import os
#импорт бибилиотеки для рисования таблиц
from tabulate import tabulate
#бибилотека для чтения конфигов
import configparser

#импортируем свои файлы
from base_functions import *
from stat_functions import *

clear = lambda: os.system('cls')
config = configparser.ConfigParser()
config.read("conf.ini")


#главная ф-ция
def main_func():
    print("Rate Your Music Parser v {}".format(config['BASIC']['dev_version']))
    print("Пишите комнады внизу")
    command = ""
    global global_album_list
    global global_filename
    while command != "exit":
        print("cmd: ")
        command = input()
        #basic stats
        if command == "bs":
            if(global_album_list != 0):
                clear()
                basic_stats(global_album_list)
        #albums spreadsheet
        elif command == "as":
            if(global_album_list != 0):
                clear()
                show_album_spreadsheet(global_album_list, "default")
        elif command == "as-top":
            if(global_album_list != 0):
                clear()
                show_album_spreadsheet(global_album_list, "top")
        elif command == "as-bottom":
            if(global_album_list != 0):
                clear()
                show_album_spreadsheet(global_album_list, "bottom")
        elif command == "as-year":
            year = input("Введите год: ")
            if(global_album_list != 0):
                clear()
                show_album_spreadsheet_by_year(global_album_list, year, "default")
        elif command == "as-year-top":
            year = input("Введите год: ")
            if(global_album_list != 0):
                clear()
                show_album_spreadsheet_by_year(global_album_list, year, "top")
        #artist stats
        elif command == "ars":
            artist_name = input("Введите имя исполнителя: ")
            clear()
            artist_basic_stat(global_album_list, artist_name, "default")
        elif command == "ars-top":
            artist_name = input("Введите имя исполнителя: ")
            clear()
            artist_basic_stat(global_album_list, artist_name, "top")
        #top artists
        elif command == "top-art":
            clear()
            top_artists(global_album_list)
        #top artists by count
        elif command == "top-art-count":
            clear()
            top_artists_by_count(global_album_list)
        #top artists by count
        elif command == "top-years":
            clear()
            top_years(global_album_list)
        #change filename
        elif command == "chf":
            clear()
            print("New file name: ")
            filename = input()
            if(change_filename(filename) != 0):
                global_filename = change_filename(filename)
                global_album_list = load_file(global_filename)
                print ("Файл был изменен!")
        #help
        elif command == "help":
            clear()
            help()
        #exit the program
        elif command == "exit":
            break
        elif command == "g":
            clear()

        else:
            print("Нет такой команды")

global_filename = config['BASIC']['file']

global_album_list = load_file(global_filename)

#clear()

#запускаем главную ф-цию
main_func()


    



                









