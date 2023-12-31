import click
from app import application

@click.group()
def cli():
	pass

@cli.command()
@click.option('-l', '--link', type=str, help='link to video', default='')
@click.option('-d', '--directory', type=str, help='path for the video location', default='')
@click.option('-o', '--output-name', type=str, help='Name for the video', default='')
def download(link, directory, output_name):
	application.download_video(link, directory, output_name)

@cli.command()
def test_download():
	application.download_video('https://www.youtube.com/watch?v=xVWeRnStdSA', '.', 'Huh.pm4')