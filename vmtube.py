from flask import Flask, render_template, url_for, flash, redirect, request, send_from_directory, after_this_request, session, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from formularios import VideosForm
from datetime import datetime
import requests, re, os, time
from pandas import read_csv
from validations import *
from download import *
from db_actions import *
import io

vmtube = Flask(__name__)

DOWNLOADS_PATH = r'\vmtube\downloads\\'
ALLOWED_DOMAINS = ['.youtube.com', 'youtu.be']
IMAGE_PATH = os.path.join('static', 'img')
SERVER_LIMIT = int(900)

vmtube.config['SECRET_KEY'] = 'sua chave secreta'

# MySQL Database
vmtube.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:senha usuário@localhost/database'

videos_db = SQLAlchemy(vmtube)

migrate = Migrate(vmtube, videos_db)

class Videos(videos_db.Model):
    id = videos_db.Column(videos_db.Integer, primary_key=True)
    titulo = videos_db.Column(videos_db.String(200), nullable=False)
    url = videos_db.Column(videos_db.Text, nullable=False)
    tipo = videos_db.Column(videos_db.String(200), nullable=False)
    data = videos_db.Column(videos_db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<name %r>' % self.name


@vmtube.route('/', methods=['GET', 'POST'])
@vmtube.route('/baixar-do-youtube', methods=['GET', 'POST'])
def main_page():
    
    pix = os.path.join(IMAGE_PATH, 'pix.png')
    form = VideosForm()
    if request.method == 'POST':
        if form.videos.data:
            URL = form.videos.data
            URL = URL.replace(',','').split('\n')

            #  ----------       Validação dos domínios      --------------

            negado = url_validation(URL, ALLOWED_DOMAINS)
            if negado :
                flash(f'O domínio: {negado} não é um domínio válido.')
                return redirect(url_for('main_page'))


            #   ----------      Validação dos videos      --------------

            negado = download_validation(URL)
            if negado:    
                flash(f'A URL: {negado} está indisponível para download.')
                return redirect(url_for('main_page'))


            #  -----------      Validação do tamanho dos downloads        -----------

            formato = request.form['formato']
            negado = size_validation(URL, SERVER_LIMIT, formato)
            if negado:    
                flash('Tamanho total de download superior ao suportado.')
                return redirect(url_for('main_page'))


            #   ----------      Fazendo os downloads        --------------

            if (formato=='mp4'):
                download_list = download_video(URL, DOWNLOADS_PATH)
            else:
                download_list = download_musica(URL, DOWNLOADS_PATH)

            add_videos_db(download_list, Videos, videos_db)
            session['Pix'] = pix
            session['Download'] = download_list
        return redirect(url_for('baixando'))
    return render_template('main_page.html', form=form, pix=pix)

@vmtube.route('/baixar-videos', methods=['GET'])
def baixando():
    pix = os.path.join(IMAGE_PATH, 'pix.png')
    downloads = session['Download']
    return render_template('baixar-video.html', downloads=downloads, pix=pix) 


@vmtube.route('/downloads/<name>', methods=['GET'])
def download_file(name):
    file_path = DOWNLOADS_PATH+name
    return_data = io.BytesIO()
    with open(file_path, 'rb') as fo:
        return_data.write(fo.read())
    return_data.seek(0)

    os.remove(file_path)

    return send_file(return_data, mimetype='application/mp4', attachment_filename=name)
