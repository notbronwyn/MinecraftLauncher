import sys
import zipfile
import os
import shutil

def buildWindows():
    import py2exe
    py2exe.freeze(
        windows=[{"script":'MinecraftLauncher.pyw',"icon_resources":[(1,"favicon.ico")]}],
        zipfile=None,
    )
    shutil.make_archive("bin/MinecraftLauncher","zip","dist")
def buildLinux():
    a = open("MinecraftLauncher.pyw", "rb")
    content = a.read()
    a.close()
    a = open("bin/MinecraftLauncher", "wb")
    a.write(b"#!/usr/bin/env python3\n"+content)
    a.close()
if sys.argv[0] == "windows":
    buildWindows()
elif sys.argv[0] == "linux":
    buildLinux()
elif sys.argv[0] == "cleanup":
    shutil.rmtree("bin")
    shutil.rmtree("dist")
    print(os.getcwd())
elif sys.args[0] == "actions":
    os.chdir("D:\\a\\MinecraftLauncher\\MinecraftLauncher")
    if not os.path.isdir("bin"):
        os.mkdir("bin")
    buildWindows()
    buildLinux()
