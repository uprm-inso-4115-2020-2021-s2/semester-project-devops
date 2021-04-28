import psycopg2


class DoctorDAO:

    def __init__(self):
        connection_url = psycopg2.connect(host='ec2-23-22-191-232.compute-1.amazonaws.com',
                                          user='aajrbzpsvjlsxu',
                                          password='deef4d315910a15bc6984baf16464da8d0abcea63083e7ec854bb2bb1bef26f2',
                                          dbname='d17d97tk4gskm8', port=5432)
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

    def getDoctorByEmailAndPass(self, email, passw):
        cursor = self.conn.cursor()
        query = "select * from Doctor Where doctor_email = %s and doctor_password = %s;"
        cursor.execute(query, (email, passw))
        result = cursor.fetchone()
        return result

        # Add this function
    def getDoctorBySearchFiltered(self, term, filter):
        liketerm = '%' + term + '%'
        cursor = self.conn.cursor()
        if filter == "location":
            query = "select doctor_firstname,doctor_lastname,doctor_email,doctor_specialization,doctor_location,doctor_phone,doctor_description from Doctor Where LOWER(doctor_location) LIKE %s;"
        elif filter == "specialization":
            query = "select doctor_firstname,doctor_lastname,doctor_email,doctor_specialization,doctor_location,doctor_phone,doctor_description from Doctor Where LOWER(doctor_specialization) LIKE %s;"
        elif filter == "lastname":
            query = "select doctor_firstname,doctor_lastname,doctor_email,doctor_specialization,doctor_location,doctor_phone,doctor_description from Doctor Where LOWER(doctor_lastname) LIKE %s;"
        elif filter == "firstname":
            query = "select doctor_firstname,doctor_lastname,doctor_email,doctor_specialization,doctor_location,doctor_phone,doctor_description from Doctor Where LOWER(doctor_firstname) LIKE %s;"
        else:
            query = "select doctor_firstname,doctor_lastname,doctor_email,doctor_specialization,doctor_location,doctor_phone,doctor_description from Doctor;"
        cursor.execute(query, (liketerm,))
        result = []
        for row in cursor:
            result.append(row)
        return result

        # Add this function
    def getDoctorBySearch(self, term):
        liketerm = '%' + term + '%'
        result = []
        cursor = self.conn.cursor()

        query = "select doctor_firstname,doctor_lastname,doctor_email,doctor_specialization,doctor_location,doctor_phone,doctor_description from Doctor Where LOWER(doctor_location) LIKE %s;"
        cursor.execute(query, (liketerm,))
        for row in cursor:
             result.append(row)
        query = "select doctor_firstname,doctor_lastname,doctor_email,doctor_specialization,doctor_location,doctor_phone,doctor_description from Doctor Where LOWER(doctor_specialization) LIKE %s;"
        cursor.execute(query, (liketerm,))
        for row in cursor:
            result.append(row)
        query = "select doctor_firstname,doctor_lastname,doctor_email,doctor_specialization,doctor_location,doctor_phone,doctor_description from Doctor Where LOWER(doctor_lastname) LIKE %s;"
        cursor.execute(query, (liketerm,))
        for row in cursor:
             result.append(row)
        query = "select doctor_firstname,doctor_lastname,doctor_email,doctor_specialization,doctor_location,doctor_phone,doctor_description from Doctor Where LOWER(doctor_firstname) LIKE %s;"
        cursor.execute(query, (liketerm,))
        for row in cursor:
            result.append(row)

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