import os.path
import subprocess
import requests
import json
from subprocess import STDOUT,PIPE

if not os.path.isfile("version.txt"):
    a = open("version.txt", "w")
    a.write(":3")
    a.close()
jre = "javaw"
webUrl = "https://api.github.com/repos/olauncher/olauncher/releases/latest"
version = requests.get(webUrl)
a = open("version.txt", "r")
current = a.read()
a.close()

if version.status_code == 200:
    content = json.loads(version.text)
    release = content["assets"][0]
    if current != content["name"]:
        a = open("version.txt", "w")
        a.write(content["name"])
        a.close()
        current = content["name"]
        jar = requests.get(release["browser_download_url"], stream=True)
        if jar.status_code == 200:
            with open("bootstrap.jar", 'wb') as a:
                for chunk in jar.iter_content(chunk_size=128):
                    a.write(chunk)
        else:
            raise Exception("no internet?")
subprocess.Popen([jre,"-Dnet.minecraft.launcher.WindowTitle=Minecraft Launcher "+current[1:len(current)],"-jar","bootstrap.jar"], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
