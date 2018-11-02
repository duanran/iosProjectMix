import ImageToWord
from flask import Flask
from flask import request
import os,base64
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/imageUpload',methods=['POST'])
def image_upload():
    if request.method == 'POST':
        imgBase64 = request.form['img'];
        imgData=base64.b64decode(imgBase64);
        imgPath = '/Users/apple/Desktop/2.jpg';
        file = open(imgPath,'wb');
        file.write(imgData);
        file.close();
        code = ImageToWord.imgToWord(imgPath);

        print ('code='+code);
        return json.dumps({'words':code});



if __name__ == '__main__':
    app.run(host='172.16.40.252',port=9999)
