from flask import Flask, jsonify, request, abort
import requests 
import json
from patientsDAO import patientsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#patients=[
 #   {"id":1, "Name": "Ger", "Symptoms": "Achy Breaky Heart", "DoctorId":101},
  #  {"id":2, "Name": "Bob", "Symptoms": "Ingrown Toe Nail", "DoctorId":102},
   # {"id":3, "Name": "Andrew", "Symptoms": "Tennis Elbow", "DoctorId":103},
    #]
#nextID=4

 #"http://127.0.0.1:5000/hospital2"
@app.route('/hospital2')
def getAll():
     results = patientsDAO.getAll()

     return jsonify(results)

#curl "http://127.0.0.1:5000/hospital/2"
@app.route('/hospital2/<int:id>')
def findByID(id):
    foundPatients = patientsDAO.findByID(id)

    return jsonify(foundPatients)

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Name\":\"Mary\",\"Symptoms\":\"Fiddlers Elbow\",\"DoctorId\":104}" http://127.0.0.1:5000/hospital2
@app.route('/hospital2', methods=['POST'])
def create():
    if not request.json:
        abort(400)
        
    patient = {
        "Name": request.json['Name'],
        "Symptoms": request.json['Symptoms'],
        "DoctorId": request.json['DoctorId'],
        }
    values = (patient['Name'], patient['Symptoms'], patient['DoctorId'])
    newId = patientsDAO.create(values)
    book['id'] = newId
    return jsonify(patient)

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Name\":\"Mary\",\"Symptoms\":\"Broken Arm\",\"DoctorId\":104}" http://127.0.0.1:5000/hospital2
@app.route('/hospital2/<int:id>', methods=['PUT'])
def update(id):
    foundpatients = patientsDAO.findByID(id)
    if not foundpatients:
        abort(404)
        
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'DoctorId' in reqJson and type(reqJson['DoctorId']) is not int:
        abort(400)

    if 'Name' in reqJson:
        foundPatients['Name'] = reqJson['Name']    
    if 'Symptoms' in reqJson:
        foundPatients['Symptoms'] = reqJson['Symptoms']
    if 'DoctorId' in reqJson:
        foundPatients['DoctorId'] = reqJson['DoctorId']
    values = (foundpatients['Name'], foundpatients['Symptoms'], foundpatients['DoctorId'], foundpatients['id'])
    patientsDAO.update(values)
    return jsonify(foundpatients)


#curl -X DELETE "http://127.0.0.1:5000/hospital1/1"
@app.route('/hospital2/<int:id>', methods=['DELETE'])
def delete(id):
    patientsDAO.delete(id)
    return jsonify({"done":True})

#@app.errorhandler(404)
#def not_found404(error):
#    return make_response( jsonify( {'error':'Not found' }), 404)
#
#@app.errorhandler(400)
#def not_found400(error):
#    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__=='__main__':
    app.run(debug=True)