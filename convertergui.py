from tkinter import *
from pytube import YouTube
import os
from pathlib import Path


def download(url):
    #while True:
    try:
        # url input from user
        yt = YouTube(str(url))

        print("Waiting...")
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # save the file in Downloads folder as defult
        destination = str(Path.home() / "Downloads")

	
	

        # download the file
        out_file = video.download(output_path=destination)

        #Save the file as .mp3 (Optional)
        # try:
        #     # save the file
        #     base, ext = os.path.splitext(out_file)
        #     new_file = base + '.mp3'
        #     os.rename(out_file, new_file)
        #     # result of success
        # except:
        #     print("File already exists")

        print("Download complete")

    except Exception as e:
        #print(e)
        notif.config(fg="red", text="Video could not be downloaded \nPlease enter a valid URL")





# Main Screen
master = Tk()
master.title("Youtube Video Downloader")

# Labels
Label(master, text="Youtube Video Converter", fg="red", font=("Calibri", 15)).grid(sticky=N, padx=100, row=0)
Label(master, text="Please enter the link to your video below : ", font=("Calibri", 15)).grid(sticky=N, row=1, pady=15)
notif = Label(master, font=("Calibri", 12))
notif.grid(sticky=N, pady=1, row=4)

# Vars
url = StringVar()
# Entry --> accept single-line text strings from a user
txt = Entry(master, width=50, textvariable=url)
txt.grid(sticky=N, row=2)

# Button
def click():
    res = txt.get()
    download(res)
def clear_text():
        txt.delete(0, 'end')

Button(master, width=20, text="Download", font=("Calibri", 12), command=lambda:[click(),clear_text()]).grid(sticky=N, row=3, pady=15)

master.mainloop()
