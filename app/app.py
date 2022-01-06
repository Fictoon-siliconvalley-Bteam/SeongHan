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
        f2 = request.files['files2']
        f.save('./Fictoon/style-transfer-pytorch/style_transfer/'+secure_filename(f.filename))
        f2.save('./Fictoon/style-transfer-pytorch/style_transfer/' + secure_filename(f2.filename))
        return '파일 업로드 완료'





