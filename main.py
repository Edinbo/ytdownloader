import pytube as pt
import math
from os import system
import os

# ignore
millnames = ['',' Thousand',' Million',' Billion',' Trillion']
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Definitions
def purple(text):
    system(""); faded = ""
    red = 122
    for character in text:
        red += 3
        if red > 255:
            red = 255
        faded += (f"\033[38;2;{red};0;220m{character}")
    return faded

def white(text):
    faded = "\033[97m"
    for character in text:
        faded += character
    faded += "\033[25m"
    return faded

def red(text):
    system(""); faded = ""
    green = 150
    for character in text:
        green -= 5
        if green < 0:
            green = 0
        faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
    return faded

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.2f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

def download(x):
    try:
        yt = pt.YouTube(x)
        video_resolutions = []
        for video in yt.streams.filter(progressive=True, only_video=True):
            video_resolutions.append(video.resolution)

        print("Available Resolutions (mp4/video): ")
        for res in video_resolutions:
            print(str(res.lenght) + str(res))

        audio_resolutions = []
        for audio in yt.streams.filter(progressive=True, only_audio=True):
            audio_resolutions.append(audio.resolution)

        print("Available Resolutions (mp3/audio): ")
        for res in audio_resolutions:
            print(str(res.lenght) + str(res))

        print(f"//////////////////////\n {red('1 : download all resolutions for video')} \n {red('2 : download all resolutions for audio')} \n {red('3 : download all resolutions for both')}")
        answer = input("Select something : ")
        if answer == 1:
            only_vid = yt.streams.filter(only_video=True)
            only_vid.download(desktop)
        if answer == 2:
            only_audio = yt.streams.filter(only_audio=True)
            only_audio.download(desktop)
        if answer == 3:
            all_vids = yt.streams.all()
            all_vids.download(desktop)
    except:
        print(red("Try downloading again it seems that it didnt work"))
        x = input("Lets try using the same youtube link : ")
        download(x)
        
def question():
    download_answer = input(purple("Do you want do download this video? (y/n)"))
    if download_answer.lower() != "y":
        print(purple("Thanks for using / Github : Edinbo"))
        exit()
    else:
        download(video_link)
        
def main(video_link):
    try:
        yt = pt.YouTube(video_link)
        title, author, views, rating, channel_id, channel_url, publish_date, video_length, thumbnail = yt.title, yt.author, yt.views, yt.rating, yt.channel_id, yt.channel_url, yt.publish_date, yt.length, yt.thumbnail_url
        print(white(f" {red('Video Title')} : {white(title)} \n {red('Author/Creator')} : {white(author)} \n {red('Total Views')} : {white(millify(views))} \n {red('Video/Song Length(h,m,s)')} : {white(convert(video_length))} \n {red('Publish Date')} : {white(publish_date)} \n {red('Rating')} : {white(rating)} \n {red('Thumbnail')} : {white(thumbnail)} \n {red('Channel ID')} : {white(channel_id)} \n {red('Channel URL')} : {white(channel_url)}"))
    except:
        print(red("Invalid Link!"))
        main(input(purple("Youtube video link : ")))



# main functionality
video_link = input(purple("Youtube video link : "))
main(video_link)
question()



