from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

import os


try:
    os.listdir(os.path.join(os.getcwd(), 'upload-folder'))
except:
    os.mkdir(os.path.join(os.getcwd(), 'upload-folder'))

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'upload-folder')


@app.route('/')
def index():
    images = [img for img in os.listdir(app.config['UPLOAD_FOLDER'])]
    if not images:
        return render_template('index.html')
    return render_template('index.html', images=images)
        


@app.route('/upload', methods=['POST'])
def upload():
    images = request.files.getlist('images')
    print(images)

    for img in images:
        filename =  secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
