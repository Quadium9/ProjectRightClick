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


def check_white_space(file):
    for line in fileinput.input(file, inplace=2, encoding="UTF8"):
        counter = 0
        for char in line:
            if char == '\x00':
                counter += 1
                continue
            print(char, end='')
    fileinput.close()
    print("Number of abandoned characters " + str(counter) + R' \x00')


def start():
    # save_file_name()
    global_file_name.append('GEALAN_INVOICE_20220207_916101122.xml')
    global_file_name.append('GEALAN_INVOICE_20220204_916101123.xml')
    for g_l_n in global_file_name:
        if os.path.isdir(g_l_n):
            list_files(g_l_n)
            continue
        check_white_space(g_l_n)
    input('Operation complete...')


start()
