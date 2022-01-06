from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from Fictoon.style.style_transfer1.cli import main


application = Flask(__name__)



@application.route('/')
def upload():
    return render_template('upload.html')


@application.route('/uploader', methods=['GET', 'POST'])
def upload_process():
    if request.method == 'POST':
        f = request.files['files']
        f2 = request.files['files2']
        f.save('./Fictoon/style/style_transfer1/' +secure_filename(f.filename))
        f2.save('./Fictoon/style/style_transfer1/' + secure_filename(f2.filename))
        return render_template('process.html')

@application.route('/process',methods=['GET','POST'])
def process():
    if request.method=='POST':
        main()
        return "변환중입니다."


