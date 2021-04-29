import psycopg2


class PatientDAO:

    def __init__(self):
        connection_url = psycopg2.connect(host='ec2-23-22-191-232.compute-1.amazonaws.com',
                                          user='aajrbzpsvjlsxu',
                                          password='deef4d315910a15bc6984baf16464da8d0abcea63083e7ec854bb2bb1bef26f2',
                                          dbname='d17d97tk4gskm8', port=5432)
        self.conn = connection_url

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

    def getPatientByEmailAndPass(self, email, passw):
        cursor = self.conn.cursor()
        query = "select * from Patient Where patient_email = %s and patient_password = %s;"
        cursor.execute(query, (email, passw))
        result = cursor.fetchone()
        return result

    def getPatientId(self, patient_firstname, patient_lastname, patient_email):
        cursor = self.conn.cursor()
        query = "SELECT patient_id from Patient WHERE patient_firstname = %s and patient_lastname = %s and patient_email = %s;"
        cursor.execute(query,(patient_firstname, patient_lastname, patient_email,))
        result = cursor.fetchone()
        return result


    def insert(self, patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone):
        cursor = self.conn.cursor()
        query = "insert into Patient(patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone) values (%s, %s, %s, %s, %s, %s, %s, %s) ;"
        cursor.execute(query, (patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone))
        patient_id = self.getPatientId(patient_firstname, patient_lastname, patient_email)
        self.conn.commit()
        return patient_id

    def delete(self, patient_id):
        cursor = self.conn.cursor()
        query = "delete from Patient where patient_id = %s;"
        cursor.execute(query, (patient_id,))
        self.conn.commit()
        return patient_id

    def update(self, patient_id, patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone):
        cursor = self.conn.cursor()
        query = "update Patient set patient_firstname = %s, patient_lastname = %s, patient_email = %s, patient_password = %s, patient_birthday = %s, patient_gender = %s, patient_medicalplan = %s, patient_phone = %s where patient_id = %s;"
        cursor.execute(query, (patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone, patient_id,))
        self.conn.commit()
        return patient_id