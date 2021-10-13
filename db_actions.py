import mysql.connector

def add_videos_db(download_list, Videos, videos_db):
	for video in download_list:
		add_video = Videos(titulo=video['titulo'], url=video['url'], tipo=video['formato'])
		videos_db.session.add(add_video)
	videos_db.session.commit()

	#sql = "INSERT INTO videos (titulo, url, tipo) VALUES (%s, %s, %s)"


