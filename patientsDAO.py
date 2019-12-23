import mysql.connector
class patientsDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="kim123",
    #user="gerardh",
    #password="Nov2019123"
        database="patients"
        )
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into patients (Name, Symptoms, DoctorId) values (%s, %s, %s)"

        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
    
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from patients"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        return returnArray
    
    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from patients where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql = "update patients set Name= %s, Symptoms=%s, DoctorId where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from patients where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id', 'Name', 'Symptoms', "DoctorId"]

        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
            
        return item

patientsDAO = patientsDAO()