from pytubefix import YouTube
import os

def oauth_check():
    print("Starting Oauth Authentication...")
    url = 'https://youtu.be/FX4BaKDM5TQ?si=2txrlDkOBNiH4B4u'

    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

    ys = yt.streams.get_audio_only()
    ys.download(filename='Deletehis')

    if os.path.isfile('Deletethis'):
        os.remove('Deletethis')

    print("Finished!")

if __name__ == "__main__":
    oauth_check()
