import os
import sys
import subprocess
import requests
import json
import zipfile
import shutil
import tkinter.messagebox
from os import getenv
from subprocess import STDOUT,PIPE
#variables
webUrl = "https://api.github.com/repos/olauncher/olauncher/releases/latest"
path = ""
jre = shutil.which("javaw")
#platform specific code
if sys.platform == "win32":
    path = os.path.expandvars("%APPDATA%")
    if not os.path.isdir(path+"\\.minecraft"):
        os.mkdir(path+"\\.minecraft")
    path = path+"\\.minecraft\\"
elif sys.platform == "linux":
    path = os.path.expandvars("$HOME")
    if not os.path.isdir(path+"/.minecraft"):
        os.mkdir(path+"/.minecraft")
    path = path+"/.minecraft/"
os.chdir(path)
if not jre:
    tkinter.messagebox.showerror(title="Error", message="Java is required to play Minecraft. Please install Java")
    raise Exception("Java not installed!")
else:
    #starts the launcher
    if not os.path.isfile(path+"version.txt"):
        a = open(path+"version.txt", "w")
        a.write(":3")
        a.close()
        tkinter.messagebox.showinfo(title="First Launch Info", message="A Minecraft Java Edition account is required to play the game!")
    version = requests.get(webUrl)
    a = open(path+"version.txt", "r")
    current = a.read()
    a.close()
    if version.status_code == 200:
        content = json.loads(version.text)
        release = content["assets"][0]
        if current != content["name"]:
            a = open(path+"version.txt", "w")
            a.write(content["name"])
            a.close()
            current = content["name"]
            jar = requests.get(release["browser_download_url"], stream=True)
            if jar.status_code == 200:
                with open(path+"redist.jar", 'wb') as a:
                    for chunk in jar.iter_content(chunk_size=128):
                        a.write(chunk)
            elif not os.path.isfile(path+"redist.jar"):
                tkinter.messagebox.showerror(title="Error", message="OLauncher Redist failed to download")
                raise Exception("no internet?")
    subprocess.Popen([jre,"-Dnet.minecraft.launcher.WindowTitle=Minecraft Launcher "+current[1:len(current)],"-jar",path+"redist.jar"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
