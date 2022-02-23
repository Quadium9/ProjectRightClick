import os
import shutil
from distutils.dir_util import copy_tree
import sys
import time
import ctypes


# Function create register file that add too context menu programs
def registry():
    if not os.path.isfile("AddToRegistry.reg"):
        file = open("AddToRegistry.reg", "w")
        file.close()
    file = open("AddToRegistry.reg", 'r+')
    file.write(R"Windows Registry Editor Version 5.00" + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script] ' + '\n'
               + R'"MUIVerb" = "My Tool" ' + '\n'
               + R'"subcommands"=""' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell]' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\SwitchChar]' + '\n'
               + R'@="Switch Char"' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\SwitchChar\command]' + '\n'
               + R'@=' + '''"''' + R"\"" + R'''C:\\Program Files (x86)\\ProjectRightClick\\SwitchChar\\SwitchChar.exe\" \"%1\""''' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\RemoveSpace]' + '\n'
               + R'@="XML Gealan"' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\RemoveSpace\command]' + '\n'
               + R'@=' + '''"''' + R"\"" + R'''C:\\Program Files (x86)\\ProjectRightClick\\RemoveSpace\\RemoveSpace.exe\" \"%1\""''' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\CheckSize]' + '\n'
               + R'@="Check Size"' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\CheckSize\command]' + '\n'
               + R'@=' + '''"''' + R"\"" + R'''C:\\Program Files (x86)\\ProjectRightClick\\CheckSize\\CheckSize.exe\" \"%1\""''' + '\n' + '\n')
    file.close()
    for line in open("AddToRegistry.reg", 'r'):
        print(line, end="")


# Function check if Python script is open with higher privilege
def is_admin():
    try:
        print("Is admin true?")
        time.sleep(2)
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


# Function copy code file with all required library
def copy_file():
    original = os.getcwd() + '\\CheckSize'
    target = 'C:\\Program Files (x86)\\ProjectRightClick\\CheckSize'
    copy_tree(original, target)
    print(original)
    print(target)
    original = os.getcwd() + '\\SwitchChar'
    target = 'C:\\Program Files (x86)\\ProjectRightClick\\SwitchChar'
    copy_tree(original, target)
    print(original)
    print(target)
    original = os.getcwd() + '\\RemoveSpace'
    target = 'C:\\Program Files (x86)\\ProjectRightClick\\RemoveSpace'
    copy_tree(original, target)
    print(original)
    print(target)
    time.sleep(2)


# Clause check if script is run with higher privilege and performs function for install program
if is_admin():
    registry()
    directory = os.path.join("C:\\", 'Program Files (x86)', 'ProjectRightClick')
    print(directory)
    if os.path.exists(directory):
        shutil.rmtree('C:\\Program Files (x86)\\ProjectRightClick')
    os.mkdir(directory)
    copy_file()
    print("Installing registry file...")
    time.sleep(2)
    os.system("regedit /s AddToRegistry.reg")
    print("Done...")
    time.sleep(2)
    input("Process complete. Press enter...")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
