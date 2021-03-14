import psycopg2


class PatientDAO:
    # fix this url crap tonight
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", user='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    ##def __init__(self):
    ##    connection_url = psycopg2.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha',
    ##                                     db='BeyondHorizonsDB', port=6606)
    ##    ##connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        ##self.conn = connection_url

    def getAllPatients(self):
        cursor = self.conn.cursor()
        query = "select * from Patient;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPatientById(self, patient_id):
        cursor = self.conn.cursor()
        query = "select * from Patient Where patient_id = %s;"
        cursor.execute(query, (patient_id,))
        result = cursor.fetchone()
        return result

    def insert(self, patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone):
        cursor = self.conn.cursor()
        query = "insert into Patient(patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone) values (%s, %s, %s, %s, %s, %s, %s, %s) ;"
        cursor.execute(query, (patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone))
        #query = "SELECT LAST_INSERT_ID();"
        #cursor.execute(query)
        userid = cursor.fetchall()[0]
        self.conn.commit()
        return userid

    def delete(self, patient_id):
        cursor = self.conn.cursor()
        query = "delete from Patient where patient_id = %s;"
        cursor.execute(query, (patient_id,))
        self.conn.commit()
        return patient_id

    def update(self, patient_id, patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone):
        cursor = self.conn.cursor()
        query = "update Patient set patient_firstname = %s, patient_lastname = %s, patient_email = %s, patient_password = %s, patient_birthdayl = %s, patient_gender = %s, patient_meidcalplan = %s, patient_phone = %s where patient_id = %s;"
        cursor.execute(query, (patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone, patient_id,))
        self.conn.commit()
        return patient_id