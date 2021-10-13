from pytube import YouTube
from os import listdir
import emoji
import re

def strip_emoji(texto):
	novo_texto = re.sub(emoji.get_emoji_regexp(), r'', texto)
	return novo_texto.strip()

def download_video(URL, DOWNLOADS_PATH):
	files_name = []
	video_list = []
	dict_data = {}
	for video in URL:
		yt = YouTube(video)
		video_stream = yt.streams.get_highest_resolution()
		video_stream.download(DOWNLOADS_PATH, filename_prefix='VMTube_-_')
		dict_data['url'] = video
		dict_data['titulo'] = strip_emoji(video_stream.title)
		dict_data['size'] = str(int(video_stream.filesize/1000000))+'MB'
		dict_data['resolucao'] = video_stream.resolution
		for file in listdir(DOWNLOADS_PATH):
			if (file not in files_name):
				files_name.append(file)
				dict_data['filename'] = file
		dict_data['formato'] = 'video'
		video_list.append(dict_data.copy())
	return video_list

def download_musica(URL, DOWNLOADS_PATH):
	files_name = []
	music_list = []
	dict_data = {}
	for video in URL:
		yt = YouTube(video)
		video_stream = yt.streams.get_audio_only()
		video_stream.download(DOWNLOADS_PATH, filename_prefix='VMTube_-_')
		dict_data['url'] = video
		dict_data['titulo'] = strip_emoji(video_stream.title)
		dict_data['size'] = str(int(video_stream.filesize/1000000))+'MB'
		dict_data['resolucao'] = video_stream.abr
		for file in listdir(DOWNLOADS_PATH):
			if (file not in files_name):
				files_name.append(file)	
				dict_data['filename'] = file
		dict_data['formato'] = 'musica'
		music_list.append(dict_data.copy())
	return music_list