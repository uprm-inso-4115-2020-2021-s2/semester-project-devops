import psycopg2


class AppointmentDAO:

    def __init__(self):
        connection_url = psycopg2.connect(host='database-inso.cm7e4m7oyhhe.us-east-2.rds.amazonaws.com',
                                          user='backend', password='backend', dbname='postgres', port=5432)
        self.conn = connection_url

    def getAllAppointments(self):
        cursor = self.conn.cursor()
        query = "select * from Appointment;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAppointmentById(self, appointment_id):
        cursor = self.conn.cursor()
        query = "select * from Appointment Where appointment_id = %s;"
        cursor.execute(query, (appointment_id,))
        result = cursor.fetchone()
        return result

    def insert(self, doctor_id, patient_id, appointment_date):
        cursor = self.conn.cursor()
        query = "insert into Appointment(doctor_id, patient_id, appointment_date) values (%s, %s, %s, %s, %s, %s, %s, %s) ;"
        cursor.execute(query, (doctor_id, patient_id, appointment_date))
        #query = "SELECT LAST_INSERT_ID();"
        #cursor.execute(query)
        userid = cursor.fetchall()[0]
        self.conn.commit()
        return userid

    def delete(self, appointment_id):
        cursor = self.conn.cursor()
        query = "delete from Appointment where appointment_id = %s;"
        cursor.execute(query, (appointment_id,))
        self.conn.commit()
        return appointment_id

    def update(self, appointment_id, doctor_id, patient_id, appointment_date):
        cursor = self.conn.cursor()
        query = "update Appointment set doctor_id = %s, patient_id = %s, appointment_date = %s where appointment_id = %s;"
        cursor.execute(query, (doctor_id, patient_id, appointment_date,))
        self.conn.commit()
        return appointment_id