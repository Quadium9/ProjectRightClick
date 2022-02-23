import sys
import os
import fileinput

# Variable for save file name in list
global_file_name = []


# Function for get file and created list of it
def save_file_name():
    for s in sys.argv[1:]:
        global_file_name.append(s)


# Function to write tree structure of entered folder
# Input: startpath = sciezka do folderu
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print("Folder: " + '{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


# Function to check line length in file
# Input: g_l_n = file_name
# Return = number of char if it's too long and number in line
def check_line_size(g_l_n):
    file = open(g_l_n, 'r')
    for line in file:
        split_line = line.split(';')
        if len(split_line[4]) >= 45:
            print(split_line[4])

    file.close()


# Function for checking if remain line to switch
# Return True or False according to search result
def the_check():
    for g_l_n in global_file_name:
        last_line = ""
        file = open(g_l_n, 'r')
        for line in file:
            split_line = line.split(';')
            if len(split_line[4]) >= 45:
                last_line = split_line[4]
        file.close()
        if last_line == "":
            return False
        else:
            return True


# Function to find and switch phrase
# Input: char_for_change = string, char_for_find = string, g_l_n = file name
# Return = number of change
def change_char(g_l_n):
    char_for_change = input("Find characters: ")
    char_for_find = input("Change to: ")
    for line in fileinput.input(g_l_n, inplace=2):
        print(line.replace(char_for_change, char_for_find), end='')
    fileinput.close()


# Function start
def start():
    save_file_name()
    for g_l_n in global_file_name:
        if os.path.isdir(g_l_n):
            list_files(g_l_n)
            continue
        check_line_size(g_l_n)
        switch_phrase = input("Do you want to switch phrase? [Y/N]")
        if switch_phrase == 'Y' or switch_phrase == 'y':
            change_char(g_l_n)
        if the_check():
            start()


start()

input("\n Process complete")
