from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests

app = Flask(__name__)

#몽고db에 접속하는 코드
client = MongoClient('mongodb+srv://isnoopy:5492@cluster0.izbrf.mongodb.net/?retryWrites=true&w=majority')
#aws에 접속하는 코드. db 에접속하는 aws ip를 왜 쓰는거지? 여튼 이 방법으로 db접속하는법도 알아내야함.
#client = MongoClient('43.200.183.105', 27017, username="isnoopy", password="5492")
db = client.dbsparta_plus_week2

@app.route('/')
def main():
    # DB에서 저장된 단어 찾아서 HTML에 나타내기

    return render_template("index.html")

@app.route('/<keyword>')
def connect(keyword):
    # DB에서 저장된 단어 찾아서 HTML에 나타내기
    personal_info=db.personal_info.find_one({"id":keyword})
    print(personal_info["name"])
    return render_template("personal.html",personal_info=personal_info)

@app.route('/personal')
def personal():
    # DB에서 저장된 단어 찾아서 HTML에 나타내기

    return render_template("personal.html")

@app.route('/test')
def test():
    # DB에서 저장된 단어 찾아서 HTML에 나타내기

    return render_template("test.html")

"""

@app.route('/detail/<keyword>')
def detail(keyword):
    #db에서 정보 읽어오기
    status_receive = request.args.get("status_give")
    #find_result= db.word.find_one({"word":keyword})
    find_result = db.words.find_one({"word": keyword})
    #print("키워드")
    #print(keyword)
    #print("읽은 도큐먼트")
    #print(find_result)

    #result ={ "word":"hello", "pronunciation":"həˈloʊ", "definitions":["	(만났을 때의 인사로) 안녕(하세요); 인사; (전화에서나 남의 관심을 끌 때) 여보세요", "이런, 어머나(놀라움을 나타냄)"]}

    return render_template("detail.html", find_result=find_result,status=status_receive)


@app.route('/api/save_word', methods=['POST'])
def save_word():
    # 단어 저장하기
    word_receive = request.form["word_give"]
    definition_receive = request.form["definition_give"]
    doc = {"word" : word_receive, "definition":definition_receive}#table = collection, record = document, field = field
    db.words.insert_one(doc)
    return jsonify({'result': 'success', 'msg': f'단어{word_receive} 저장'})


@app.route('/api/delete_word', methods=['POST'])
def delete_word():
    # 단어 삭제하기
    print("단어 삭제")
    word_receive = request.form["word_give"]
    db.words.delete_one({"word":word_receive})
    return jsonify({'result': 'success', 'msg': f'단어 {word_receive} 삭제'})

"""

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)