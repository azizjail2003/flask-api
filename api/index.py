from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    url = 'http://estatmar.ma:8081/api/v1/formdata/135'
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZjM1ZDVkMjc5NDMyMTJhZjA3MmI5OTc2ZjM4MjA4MWEzZTc1M2U1YzFmYTk1Njg1YTkyNDI1MzdkNGVjYWJmYjgxNDE5MWRmM2UzYjA5NDYiLCJpYXQiOjE3MDkyODg5ODYuMjU3OTI2LCJuYmYiOjE3MDkyODg5ODYuMjU3OTMsImV4cCI6MTcxNzIzNzc4Ni4yNDk2NjUsInN1YiI6IjI3Iiwic2NvcGVzIjpbXX0.PRx5J-54zEArBk6QNduUXS12OEYorElTFU05wuAuKlIPmQmxUAYWrDC4M_ZkRXitx_6bOyl_7MpF3NgB_ydQFo3tezqKyBe1DsQ3yov9XIobkpLdmFK7lQZ2eD6_9JHyBmrHRESAe_LuSc3PBj_nNB_YRyYLfWUe12aRpbrLdoxDlq7KGlhgK1Vq0oAtiaTtH9hjkgOsUrbazsnN-_uJR2bfPtG-wwE0hZVZeOq0NRItwXv1AfYMNQtGU6QHHEFPiU1TSUCIAVaSwmdGvCjPJ_mdt61IJuVarl7asOYj0mnCMW7u29h4xHKjv2FLpXFob2EPZUoVoPmRqs4XG9LsCpccjMEKuIY_Bo1a13eH5fgM-PEgU582VUtCmYESfLWissNNmFlldqZpZzcq-NkZQ7-roHYx6dXMauh6ks3MflMXOGZGMnnHRxraNBSF3PrkljE8Ki7cq_S2LfymgXkswu9EL4mxnXVXfn1iopboniHl24WfVHop74HV-xtWW2kDxJZJeK6_ivALYRDDuEwsXUujaIBWMkdUuq4dpOL6r4AZaM-MTKAWYD8UR1PxLKylkfnigVqVlz26SFmgQrS7YiWFTTXu3Yhrilb4oNuZ9z9QyZEDvpDabZNpcRWu4lo5b0szeVx9WTeCBpgXMkEC1G0_hHNDYVv-npiEPzNRtDQ'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data, 200



@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404