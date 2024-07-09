from flask import Flask, request, jsonify
from flask_cors import CORS
from core.UsrData import UsrData
from core.TimeTools import TimeTools

uploader = UsrData()
timetools = TimeTools()

app = Flask(__name__)
CORS(app)

#데이터 받기
@app.route('/upload', methods=['POST'])
def receive_data():
    data = request.json
    

    print(data)

    uploader.upload(data)

    response = {"status": "success"}

    return jsonify(response)

@app.route('/top3', methods=['GET'])

def top_3():
    top3 = timetools.get_top3(uploader.datas)

    response = {'first': top3[0], 'second': top3[1], 'third': top3[2]}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)