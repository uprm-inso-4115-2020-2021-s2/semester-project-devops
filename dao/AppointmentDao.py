import psycopg2


class AppointmentDAO:

    def __init__(self):
        connection_url = psycopg2.connect(host='ec2-23-22-191-232.compute-1.amazonaws.com',
                                          user='aajrbzpsvjlsxu',
                                          password='deef4d315910a15bc6984baf16464da8d0abcea63083e7ec854bb2bb1bef26f2',
                                          dbname='d17d97tk4gskm8', port=5432)
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

    def getAppointmentId(self, doctor_id, patient_id, appointment_date):
        cursor = self.conn.cursor()
        query = "SELECT appointment_id from Appointment WHERE doctor_id = %s and patient_id = %s and appointment_date = %s;"
        cursor.execute(query,(doctor_id, patient_id, appointment_date,))
        result = cursor.fetchone()
        return result

    def insert(self, doctor_id, patient_id, appointment_date):
        cursor = self.conn.cursor()
        query = "insert into Appointment(doctor_id, patient_id, appointment_date) values (%s, %s, %s) ;"
        cursor.execute(query, (doctor_id, patient_id, appointment_date))
        appointment_id = self.getAppointmentId(doctor_id, patient_id, appointment_date)
        self.conn.commit()
        return appointment_id

    def delete(self, appointment_id):
        cursor = self.conn.cursor()
        query = "delete from Appointment where appointment_id = %s;"
        cursor.execute(query, (appointment_id,))
        self.conn.commit()
        return appointment_id

    def update(self, appointment_id, doctor_id, patient_id, appointment_date):
        cursor = self.conn.cursor()
        query = "update Appointment set doctor_id = %s, patient_id = %s, appointment_date = %s where appointment_id = %s;"
        cursor.execute(query, (doctor_id, patient_id, appointment_date, appointment_id))
        self.conn.commit()
        return appointment_id