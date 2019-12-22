import requests
import json
from xlwt import*

url = "http://127.0.0.1:5000/hospital2"

response = requests.get(url)
data = response.json()

#output to console

print(data)

#output patients individually
for patient in data["patients"]:
    print(patients)

#save this to a file
filename = 'patients.json'
if filename:
    #writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

#write to an excel file
w = Workbook()
ws = w.add_sheet('patients')
row = 0;
ws.write(row,0,"Name")
ws.write(row,1,"Symptoms")
ws.write(row,2,"DoctorId")
#ws.write(row,3,"price")
row += 1
for patients in data["patients"]:
    ws.write(row,0, patients["Name"])
    ws.write(row,1, patients["Symptoms"])
    ws.write(row,2, patients["DoctorId"])
    #ws.write(row,3, car["price"])
    row +=1
w.save('patients.xls')