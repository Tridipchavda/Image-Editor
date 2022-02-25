from pytube import *
from tkinter.filedialog import *
from tkinter import *

file_size=0
def Download():
    global file_size
    try:
        url= textbar.get()
        print(url)
        Dow_button.config(text="Please wait...")
        Dow_button.config(state=DISABLED)
        
        path=askdirectory()
        if path is None:
            return
        
        obj = YouTube(url)
        strm = obj.streams.first()
        print(strm)
        strm.download(path)

        Dow_button.config(text="Start Download")
        Dow_button.config(state=NORMAL)
        
        print("done")

    except Exception as e:
        print(e)
        print("Download failed")

load = Tk()
load.geometry("400x550")

load.title("YouTube Downloader")

load.iconbitmap('img_main.ico')

file = PhotoImage(file="Icon.png")
Iconimg=Label(load,image=file)
Iconimg.pack(side=TOP)

textbar=Entry(load,font=("verdana",16))
textbar.pack(side=TOP,fill="x",pady="20",padx="10")

Dow_button=Button(load,text="Start Download",font=("verdana",16),command=Download)
Dow_button.pack(side=TOP)
load.mainloop()
