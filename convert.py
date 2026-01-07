import ffmpeg
import os

def convert_to_mp3(file, res, output):
    source = output + "/" + file + res
    new = output + "/" + ("CONVERTED") + file + ".mp3"

    ffmpegGlobalArguments = ['-n']

    stream = ffmpeg.input(source)
    stream = ffmpeg.output(stream, new, loglevel="quiet")
    stream = stream.global_args(*ffmpegGlobalArguments)
    ffmpeg.run(stream)

    os.remove(source)
    os.rename(new, output + "/" + file +".mp3")
