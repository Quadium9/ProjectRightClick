import os
import shutil
from distutils.dir_util import copy_tree
import sys
import time
import ctypes


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
               + R'@=' + '''"''' + R"\"" + R'''C:\\Program Files (x86)\\ProjectRightClick\\SwitchChar.exe\" \"%1\""''' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\CheckSize]' + '\n'
               + R'@="Check Size"' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\CheckSize\command]' + '\n'
               + R'@=' + '''"''' + R"\"" + R'''C:\\Program Files (x86)\\ProjectRightClick\\CheckSize.exe\" \"%1\""''' + '\n' + '\n')
    file.close()
    for line in open("AddToRegistry.reg", 'r'):
        print(line, end="")


def is_admin():
    try:
        print("Admin is true")
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def copy_file():
    original = os.getcwd() + '\\CheckSize'
    target = 'C:\\Program Files (x86)\\ProjectRightClick\\'
    copy_tree(original, target)
    print(original)
    print(target)
    original = os.getcwd() + '\\SwitchChar'
    target = 'C:\\Program Files (x86)\\ProjectRightClick\\'
    copy_tree(original, target)
    print(original)
    print(target)


if is_admin():
    registry()
    directory = os.path.join("C:\\", 'Program Files (x86)', 'ProjectRightClick')
    print(directory)
    if os.path.exists(directory):
        shutil.rmtree('C:\\Program Files (x86)\\ProjectRightClick')
    os.mkdir(directory)
    copy_file()
    print("Installing registry file...")
    time.sleep(3)
    os.system("regedit /s AddToRegistry.reg")
    print("Done...")
    input("Process complete. Press enter...")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
