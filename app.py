from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

import os
import psycopg2


load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = f'posgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}'


@app.route('/')
def index():
    images = [img for img in os.listdir(app.config['UPLOAD_FOLDER'])]
    if not images:
        return render_template('index.html')
    return render_template('index.html', images=images)
        


@app.route('/upload', methods=['POST'])
def upload():
    db_connect = connect_to_db()
    images = request.files.getlist('images')
    print(images)

    for img in images:
        filename =  secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
