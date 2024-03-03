import py2exe

py2exe.freeze(
    windows=[{"script":'MinecraftLauncher.pyw',"icon_resources":[(1,"favicon.ico")]}],
    #zipfile='library.zip',
    zipfile=None,
   )
