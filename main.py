import pytube as pt
import math
from os import system
import pathlib

# ignore
millnames = ['', ' Thousand', ' Million', ' Billion', ' Trillion']
desktop = pathlib.Path.home() / 'Desktop'

# Definitions
def purple(text):
    system("")
    faded = ""
    red = 122
    for character in text:
        red += 3
        if red > 255:
            red = 255
        faded += (f"\033[38;2;{red};0;220m{character}")
    return faded

def white(text):
    faded = "\033[97m" + text + "\033[0m"
    return faded


def red(text):
    system("")
    faded = ""
    green = 150
    for character in text:
        green -= 5
        if green < 0:
            green = 0
        faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
    return faded

def millify(n):
    n = float(n)
    millidx = max(0, min(len(millnames) - 1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))

    return '{:.2f}{}'.format(n / 10 ** (3 * millidx), millnames[millidx])

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

def video(yt):
    video_resolutions = []
    for video in yt.streams.filter(progressive=True):
        video_resolutions.append(video.resolution)

    print("Available Resolutions (mp4/video): ")
    for res in video_resolutions:
        print(str(res))

def audio(yt):
    audio_resolutions = []
    for audio in yt.streams.filter(progressive=True):
        audio_resolutions.append(audio.resolution)

    print("Available Resolutions (mp3/audio): ")
    for res in audio_resolutions:
        print(str(res))

def download(x):
    try:
        yt = pt.YouTube(x)
        audio(yt)
        video(yt)

        print(
            f"//////////////////////\n {red('1 : download highest resolution for video')} \n {red('2 : download highest resolution for audio')} \n {red('3 : download both (video/audio)')}")
        answer = int(input(red("Select something : ")))

        if answer == 1:
            only_vid = yt.streams.filter(only_audio=False, progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            only_vid.download(desktop)
            print(f"Succesfully downloaded {only_vid} to {desktop}")
            print(purple("Thanks for using // Github : Edinbo"))
        elif answer == 2:
            only_audio = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
            only_audio.download(desktop)
            print(f"Succesfully downloaded {only_audio} to {desktop}")
            print(purple("Thanks for using // Github : Edinbo"))
        elif answer == 3:
            both_audio = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()
            both_video = yt.streams.filter(only_audio=False, progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            both_audio.download(desktop)
            both_video.download(desktop)
            print(f"Succesfully downloaded {both_video, both_audio} to {desktop}")
            print(purple("Thanks for using // Github : Edinbo"))
    except:
        print(red("Try downloading again, it seems like it didn't work"))
        x = input(purple("Let's try using the same YouTube link : "))
        download(x)

def question():
    download_answer = input(purple("Do you want to download this video? (y/n)"))
    if download_answer.lower() != "y":
        print(purple("Thanks for using // Github : Edinbo"))
        exit()
    else:
        download(video_link)

def main(video_link):
    try:
        yt = pt.YouTube(video_link)
        title, author, views, rating, channel_id, channel_url, publish_date, video_length, thumbnail = yt.title, yt.author, yt.views, yt.rating, yt.channel_id, yt.channel_url, yt.publish_date, yt.length, yt.thumbnail_url
        print(f" {red('Video Title')} : {white(str(title))} \n {red('Author/Creator')} : {white(str(author))} \n {red('Total Views')} : {white(str(millify(views)))} \n {red('Video/Song Length(h,m,s)')} : {white(str(convert(video_length)))} \n {red('Publish Date')} : {white(str(publish_date))} \n {red('Rating')} : {white(str(rating))} \n {red('Thumbnail')} : {white(str(thumbnail))} \n {red('Channel ID')} : {white(str(channel_id))} \n {red('Channel URL')} : {white(str(channel_url))}")
    except:
        print(red("Invalid Link!"))
        main(input(purple("YouTube video link : ")))

# main functionality
video_link = input(purple("YouTube video link : "))
main(video_link)
question()
