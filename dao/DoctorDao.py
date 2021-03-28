import psycopg2


class DoctorDAO:

    def __init__(self):
        connection_url = psycopg2.connect(host='database-inso.cm7e4m7oyhhe.us-east-2.rds.amazonaws.com',
                                          user='backend', password='backend', dbname='postgres', port=5432)
        self.conn = connection_url

    def getAllDoctors(self):
        cursor = self.conn.cursor()
        query = "select * from Doctor;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDoctorById(self, doctor_id):
        cursor = self.conn.cursor()
        query = "select * from Doctor Where doctor_id = %s;"
        cursor.execute(query, (doctor_id,))
        result = cursor.fetchone()
        return result

    def insert(self, doctor_firstname, doctor_lastname, doctor_email, doctor_password, doctor_specialization, doctor_location, doctor_phone):
        cursor = self.conn.cursor()
        query = "insert into Doctor(doctor_firstname, doctor_lastname, doctor_email, doctor_password, doctor_specialization, doctor_location, doctor_phone) values (%s, %s, %s, %s, %s, %s, %s, %s) ;"
        cursor.execute(query, (doctor_firstname, doctor_lastname, doctor_email, doctor_password, doctor_specialization, doctor_location, doctor_phone))
        #query = "SELECT LAST_INSERT_ID();"
        #cursor.execute(query)
        userid = cursor.fetchall()[0]
        self.conn.commit()
        return userid

    def delete(self, doctor_id):
        cursor = self.conn.cursor()
        query = "delete from Doctor where doctor_id = %s;"
        cursor.execute(query, (doctor_id,))
        self.conn.commit()
        return doctor_id

    def update(self, doctor_id, doctor_firstname, doctor_lastname, doctor_email, doctor_password, doctor_specialization, doctor_location, doctor_phone):
        cursor = self.conn.cursor()
        query = "update Doctor set doctor_firstname = %s, doctor_lastname = %s, doctor_email = %s, doctor_password = %s, doctor_specializationl = %s, doctor_location = %s, doctor_phone = %s where doctor_id = %s;"
        cursor.execute(query, (doctor_firstname, doctor_lastname, doctor_email, doctor_password, doctor_specialization, doctor_location, doctor_phone, doctor_id,))
        self.conn.commit()
        return doctor_id