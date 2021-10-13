from pytube import YouTube

def url_validation(URL, dominios):
	for video in URL:
		for dominio in dominios:
			if (dominio not in video):
				return video


def download_validation(URL):
	for video in URL:
		try:
			yt = YouTube(video)
		except: 
			return video

def size_validation(URL, SERVER_LIMIT, tipo):
	sizes = []
	for video in URL:
		yt = YouTube(video)
		if tipo=='mp4':
			video_stream = yt.streams.get_highest_resolution()
			sizes.append(video_stream.filesize/1000000)
		else:
			video_stream = yt.streams.get_audio_only()
			sizes.append(video_stream.filesize/1000000)
	if (sum(sizes) >= SERVER_LIMIT):
		return True	


        