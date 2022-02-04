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
# Return = number of char if it's too long and number in line
def check_line_size():
    for g_l_n in global_file_name:
        row_count = 1
        column_count = 5
        for line in open(g_l_n, 'r'):
            row_count = row_count + 1
            split_line = line.split(';')
            if len(split_line[5]) >= 41:
                print(split_line[5])


# Function to find and switch phrase
# Input: char_for_change = string, char_for_find = string
# Return = number of change
def change_char():
    char_for_change = input("Find characters: ")
    char_for_find = input("Change to: ")
    for g_l_n in global_file_name:
        if os.path.isdir(g_l_n):
            list_files(g_l_n)
            continue
        for line in fileinput.input(g_l_n, inplace=2):
            print(line.replace(char_for_change, char_for_find), end='')
        fileinput.close()


save_file_name()
check_line_size()
switch_phrase = input("Do you want to switch phrase for this line? [Y/N]")
if switch_phrase == 'Y' or switch_phrase == 'y':
    change_char()
input("\n Process complete")
