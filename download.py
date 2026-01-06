# download.py
from pytubefix import YouTube
import json
import os
import convert

def get_configs():
    config_path = os.getcwd() + "/config.json"
    with open(config_path, "r") as config:
            variables = json.load(config)

    url = variables["url"]
    res = variables["resolution"]
    symbols_remove = variables["incorrect_symbols_remove"]
    ifconvert = variables["convert_to_mp3"]
    output = variables["output_path"]

    return url, res, symbols_remove, ifconvert, output


def download(url, res, symbols_remove, ifconvert, output):

    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

    #incorrect symbols might break the save process, so they need to be deleted from file's name
    if symbols_remove == True:
        eng = "abcdefghijklmnopqrstuvwxyzZYXWVUTSRQPONMLKJIHGFEDCBA"
        ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        space = " "
        numbers = "1234567890"
        correct_symbols = eng + ru + numbers + space

        title = yt.title
        file = ""


        for c in title:
            if c in correct_symbols:
                file += c
    else:
        file = yt.title

    if res == ".m4a" or res == ".mp3":
        ys = yt.streams.get_audio_only()
    elif res == ".mp4":
        #360p support only
        ys = yt.streams.get_highest_resolution()
    #elif user_choice == ".mp4_720":
        #dosomething

    if os.path.isfile(output + "/" + file + res):
        os.remove(output + "/" + file + res)

    ys.download(output_path=output, filename=file + res)

    if res == ".mp3":
        # Если mp3 по дефолту, то конвертируем скрытно
        convert.convert_to_mp3(file, res, output)

    return file

def get_title():
    url = get_configs()
    yt = YouTube(url[0])
    return yt.title

