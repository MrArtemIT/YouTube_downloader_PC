import pytube
from rich import print
from rich.progress import track
from rich.console import Console
from pytube.cli import on_progress


import tkinter as tk
from tkinter import filedialog as fd 

import easygui

console = Console()

url = console.input("[bold green]URL video   [/]")
if url == 'ex':
    exit()
elif url == 'exit':
    exit()
else:
    pass
'''dire = console.input("[bold green]Enter the download directory   [/]")
if dire == 'ex':
    exit()
elif dire == 'exit':
    exit()
else:
    pass'''



'''def callback():
    global dire
    dire= fd.askdirectory() 

errmsg = 'Error!'
tk.Button(text='Click to Open File', 
       command=callback).pack(fill=tk.X)
tk.mainloop()'''
print("[bold green]Enter the download directory   [/]")
dire = easygui.diropenbox()


console.print("[bold red]+++++++++++++++++++[/]")
print(dire)
console.print("[bold red]+++++++++++++++++++[/]")
yt = pytube.YouTube(url, on_progress_callback=on_progress)
ft = yt.title
console.print("[bold green]Please wait...[/]")
vid = yt.streams.get_highest_resolution()

va = yt.author
vd = yt.description
console.print("[bold blue](((((((((((((((AUTHOR)))))))))))))))[/]")
print(va)
console.print("[bold blue](((((((((((((((DESCRIPTION)))))))))))))))[/]")
print(vd)
console.print("[bold blue]###############################################################[/]")
for n in track(range(100), description="Download..."):
    downloads = vid.download(dire)
console.print("[bold green]##############################################################[/]")
console.print("[bold green]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!![/]")
console.print("[bold green]##############################################################[/]")
console.input("[bold blue] Press Enter to exit [/]")