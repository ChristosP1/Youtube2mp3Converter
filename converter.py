from pytube import YouTube
import os

#while True:
try:
    # url input from user
    yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))

    print("Waiting...")
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # save the file in Downloads folder as defult
    destination = "C:\\Users\\chris\\Downloads"


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
