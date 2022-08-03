from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd


app = Flask(__name__)


@app.route('/')
def main():
    myname = "Sparta"
    return render_template("index.html", name =myname)


@app.route('/detail')
def detail():
    return render_template("detail.html")

@app.route('/upload')
def render_file():
    return render_template('upload.html')

# file이 submit되면 전달되는 페이지
# upload.html에서 form이 제출되면 /file_uploaded로 옮겨지게 되어 있음.
@app.route('/file_uploaded', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST': # POST 방식으로 전달된 경우
        f = request.files['file1']
        # 파일 객체 혹은 파일 스트림을 가져오고, html 파일에서 넘겨지는 값의 이름을 file1으로 했기 때문에 file1임.
        f.save(f'uploads/{secure_filename(f.filename)}') # 업로드된 파일을 특정 폴더에저장하고,
        df_to_html = pd.read_csv(f'uploads/{secure_filename(f.filename)}').to_html() # html로 변환하여 보여줌
        return df_to_html






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)