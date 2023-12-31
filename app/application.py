from pytube import YouTube
import validators
import click
import sys
import os

def verify_cli_args(arguemnts : list):
    if not validators.url(arguemnts[0]):
        click.echo("The URL entered is invalid")
        click.echo("Arguments format: <video url> <directory_path> <output file name>")
        return False

    if not os.path.isdir(arguemnts[1]):
        click.echo("The directory entered is invalid")
        click.echo("Expected arguments: -l <video url> -d <directory_path> -o <output file name>(optional)")
        return False

    return True

def get_quality_stream(link: YouTube):
    resolutions = ["1080p", "720p", "480", "360p", "240p"]
    for resolution in resolutions:
        streams = link.streams.filter(res=resolution, progressive=True)
        if len(streams) != 0:
            return streams.first()
    return None

def download_video(link, directory, name):
    if verify_cli_args([link, directory, name]):
        try:
            get_video = YouTube(link)
            get_stream = get_quality_stream(get_video)
            if name is not None:
                video_name = name if "mp4" in name else name + ".mp4"
                get_stream.download(output_path=directory)
            else:
                path = get_stream.download(output_path=directory)
            click.echo("Video was successfully downloaded. The file can be found at " + directory if directory != "."
                  else "Video was successfully downloaded. The file can be found at " + sys.path[-2])
        except:
            click.echo("Invalid URL entered. Please make sure that it is a URL to a YouTube video, not a playlist, "
                  "channel or YouTube homepage ")
    pass