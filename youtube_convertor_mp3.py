from pytube import YouTube
from tkinter import filedialog
from tkinter import * 
def download_file(url,save_path):
    try:
        video = YouTube(url)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename=f"{video.title}.mp3",output_path=save_path)
   
        print("The video is downloaded in MP3")
    except KeyError:
        print("Unable to fetch video information. Please check the video URL or your network connection.")
def open_file():
    folder = filedialog.askdirectory()
    if folder:
        print('Select folder:{}'.format(folder))
    return folder

url_input = input('Enter url please: ')
to_see= open_file()
if __name__=='__main__':
    root = Tk()
    root.withdraw()
    if to_see:
        print('Start downalod')
        download_file(url_input,to_see)
    else:
        print('Wrong ip')
