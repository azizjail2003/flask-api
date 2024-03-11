from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    url = 'http://estatmar.ma:8081/api/v1/formdata/135'
    
    response = requests.get(url, headers=headers)
    data = response.json()
    return data, 200



@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404