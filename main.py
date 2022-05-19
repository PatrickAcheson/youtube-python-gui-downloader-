from pytube import YouTube
import tkinter as tk
from tkinter.filedialog import askopenfilename


def media(name_var):
    video = YouTube(str(name_var.get()))
    title = video.title
    print(title)
    return video

def download_high(video, root):
    try:
        stream = video.streams.get_highest_resolution()
        stream.download()
        tk.Label(root, text = 'DOWNLOADED', font = 'arial 10').place(x = 120, y = 120)
        
    except NameError:
        print("Error")


def main():
    
    root = tk.Tk(className=' YouTube Downloader')
    root.geometry("350x200")
    root.resizable(0,0)

    root.iconbitmap("youtube.ico")

    name_var = tk.StringVar()

    name_label = tk.Label(root, text = 'Link:', font=('calibre',10, 'bold'))
    name_entry = tk.Entry(root, textvariable = name_var, font=('calibre',10,'normal'))
    titleBtn = tk.Label(root, text='BNGs YouTube Downloader', font = 'arial 15 bold')
    btn1 = tk.Button(root, text = 'Download', command= lambda: download_high(media(name_var), root))
    note_label = tk.Label(root, text = 'NOTE: videos download to current directory', font=('calibre',10, 'bold'))

    name_label.place(x = 70, y = 40)
    name_entry.place(x = 105, y = 40)
    btn1.place(x = 140, y = 75)
    titleBtn.place(x = 35, y = 1)
    note_label.place(x = 35, y = 170)

    root.mainloop()


main()
