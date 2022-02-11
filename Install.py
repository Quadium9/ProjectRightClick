import os
import shutil
import sys
import ctypes
import subprocess


def registry():
    if not os.path.isfile("AddToRegistry.reg"):
        file = open("AddToRegistry.reg", "w")
        file.close()
    file = open("AddToRegistry.reg", 'r+')
    cwd = os.getcwd()
    o = R'\\'
    ccwd = ""
    for char in cwd:
        if char == o[0]:
            ccwd = ccwd + o[0] + o[0]
        else:
            ccwd += char
    file.write(R"Windows Registry Editor Version 5.00" + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script] ' + '\n'
               + R'"MUIVerb" = "My Tool" ' + '\n'
               + R'"subcommands"=""' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell]' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\SwitchChar]' + '\n'
               + R'@="Switch Char"' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\SwitchChar\command]' + '\n'
               + R'@=' + '''"''' + R"\"" + ccwd + R"\\" + R'''SwitchChar\\SwitchChar.exe\" \"%1\""''' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\CheckSize]' + '\n'
               + R'@="Check Size"' + '\n' + '\n'
               + R'[HKEY_CLASSES_ROOT\*\shell\Run script\shell\CheckSize\command]' + '\n'
               + R'@=' + '''"''' + R"\"" + ccwd + R"\\" + R'''CheckSize\\CheckSize.exe\" \"%1\""''' + '\n' + '\n')
    for line in file:
        print(line, end="")
    file.close()


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def copy_file():
    original = os.getcwd() + '\\CheckSize\\CheckSize.exe'
    target = 'C:\\Program Files (x86)\\ProjectRightClick\\'
    shutil.copy(original, target)
    original = os.getcwd() + '\\SwitchChar\\SwitchChar.exe'
    target = 'C:\\Program Files (x86)\\ProjectRightClick\\'
    shutil.copy(original, target)


if is_admin():
    registry()
    directory = os.path.join("C:\\", 'Program Files (x86)', 'ProjectRightClick')
    if os.path.exists(directory):
        shutil.rmtree('C:\\Program Files (x86)\\ProjectRightClick')
    os.mkdir(directory)
    copy_file()
    os.system("regedit /s AddToRegistry.reg")
    input("Process complete. Press enter...")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

