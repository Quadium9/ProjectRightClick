import sys
import fileinput
import os

# Zmienna przechowujaca scieki do plikow
global_file_name = []


# Funkcja pobierajaca pliki i tworzaca zmienna globalna
def save_file_name():
    for s in sys.argv[1:]:
        global_file_name.append(s)


# Funkcja do wypisywania struktury drzewa
# Input: startpath = sciezka do folderu
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print("Folder: " + '{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


# Funkcja znajdujaca ciag znakow i zamieniajaca go na inny
# Input: char_for_change = string, char_for_find = string
# Return = number of change
def change_char():
    char_for_change = input("Znajdź znaki: ")
    char_for_find = input("Zamien na: ")
    for g_l_n in global_file_name:
        if os.path.isdir(g_l_n):
            list_files(g_l_n)
            continue
        for line in fileinput.input(g_l_n, inplace=2):
            print(line.replace(char_for_change, char_for_find), end='')
        fileinput.close()


save_file_name()
change_char()

input("\n Press Enter to close")
