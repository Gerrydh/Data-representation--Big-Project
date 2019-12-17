from flask import Flask, jsonify, request, abort
import requests 
import json

app = Flask(__name__, static_url_path='', static_folder='.')

patients=[
    {"id":1, "Name": "Ger", "Symptoms": "Achy Breaky Heart", "DoctorId":101},
    {"id":2, "Name": "Bob", "Symptoms": "Ingrown Toe Nail", "DoctorId":102},
    {"id":3, "Name": "Andrew", "Symptoms": "Tennis Elbow", "DoctorId":103},
    ]
nextID=4


 #"http://127.0.0.1:5000/hospital"
@app.route('/hospital')
def getAll():
     return jsonify(patients)

#curl "http://127.0.0.1:5000/hospital/2"
@app.route('/hospital/<int:id>')
def findByID(id):
    foundPatients = list(filter(lambda t: t['id']== id, patients))
    if len(foundPatients)== 0:
        return jsonify({}), 204

    return jsonify(foundPatients[0])

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Name\":\"Mary\",\"Symptoms\":\"Fiddlers Elbow\",\"DoctorId\":104}" http://127.0.0.1:5000/hospital
@app.route('/hospital', methods=['POST'])
def create():
    global nextID
    if not request.json:
        abort(400)
        #other checking
    patient = {
        "id": nextID,
        "Name": request.json['Name'],
        "Symptoms": request.json['Symptoms'],
        "DoctorId": request.json['DoctorId'],
        }
    nextID += 1
    patients.append(patient)
    return jsonify(patient)

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Name\":\"Mary\",\"Symptoms\":\"Broken Arm\",\"DoctorId\":104}" http://127.0.0.1:5000/hospital
@app.route('/hospital/<int:id>', methods=['PUT'])
def update(id):
    foundpatients = list(filter(lambda t: t['id']== id, patients))
    if (len(foundpatients)==0):
        abort(404)
        foundPatient = foundpatients[0]
        if not request.json:
            abort(400)
        reqJson = request.json
        if 'DoctorId' in reqJson and type(reqJson['DoctorId']) is not int:
            abort(400)
        if 'Name' in reqJson:
            foundPatient['Name'] = reqJson['Name']    
        if 'Symptoms' in reqJson:
            foundPatient['Symptoms'] = reqJson['Symptoms']
        if 'DoctorId' in reqJson:
            foundPatient['DoctorId'] = reqJson['DoctorId']
    return jsonify(foundPatient)

    return "in update for id"+str(id)

#curl -X DELETE "http://127.0.0.1:5000/hospital/1"
@app.route('/hospital/<int:id>', methods=['DELETE'])
def delete(id):
    foundPatients = list(filter(lambda t: t['id']== id, patients))
    if (len(foundPatients) == 0):
        abort(404)
    patients.remove(foundPatients[0])
    return jsonify({"done":True})

#curl -i -H "Authorization: token 01e25055726d94d79756dc9f3d377722251c6a627564e8ad5ae5c9fac03dbb7c" https://127.0.0.1:5000/hospital
apikey = '01e25055726d94d79756dc9f3d377722251c6a627564e8ad5ae5c9fac03dbb7c'
url = 'http://127.0.0.1:5000/hospital'
filename = "repo.json"

response = requests.get(url, auth=('token', apikey))

repoJSON = response.json()

file = open(filename, 'w')

json.dump(repoJSON, file, indent=4)

if __name__=='__main__':
    app.run(debug=True)