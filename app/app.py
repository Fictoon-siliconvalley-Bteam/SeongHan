from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


application = Flask(__name__)



@application.route('/')
def upload():
    return render_template('upload.html')


@application.route('/uploader', methods=['GET', 'POST'])
def upload_process():
    if request.method == 'POST':
        f = request.files['files']
        f.save('./uploads/'+secure_filename(f.filename))
        return '파일 업로드 완료'




