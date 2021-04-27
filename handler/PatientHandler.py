from flask import jsonify
from dao import PatientDao


class PatientHandler:
    def build_patient_dict(self, row):
        result = {}
        result['patient_id'] = row[0]
        result['patient_firstname'] = row[1]
        result['patient_lastname'] = row[2]
        result['patient_email'] = row[3]
        result['patient_password'] = row[4]
        result['patient_birthday'] = row[5]
        result['patient_gender'] = row[6]
        result['patient_medicalplan'] = row[7]
        result['patient_phone'] = row[8]
        return result

    def build_patient_attributes(self, patient_id, patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone):
        result = {}
        result['patient_id'] = patient_id
        result['patient_firstname'] = patient_firstname
        result['patient_lastname'] = patient_lastname
        result['patient_email'] = patient_email
        result['patient_password'] = patient_password
        result['patient_birthday'] = patient_birthday
        result['patient_gender'] = patient_gender
        result['patient_medicalplan'] = patient_medicalplan
        result['patient_phone'] = patient_phone
        return result

    def getAllPatients(self):
        dao = PatientDao.PatientDAO()
        users_list = dao.getAllPatients()
        result_list = []
        for row in users_list:
            result = self.build_patient_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getPatientById(self, patient_id):
        dao = PatientDao.PatientDAO()
        row = dao.getPatientById(patient_id)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            patients = self.build_patient_dict(row)
            return jsonify(Patients = patients)

    def getPatientByEmailAndPass(self, json):
        email = json['email']
        password = json['password']
        if email and password:
            dao = PatientDao.PatientDAO()
            row = dao.getPatientByEmailAndPass(email, password)
            if not row:
                return jsonify(Error = "User Not Found"), 404
            return jsonify(Patient = "Patient Found!"), 201
        return jsonify(Error="Missing attributes in request"), 400

    def insertPatientJson(self, json):
            patient_firstname = json['FirstName']
            patient_lastname = json['LastName']
            patient_email = json['Email']
            patient_password = json['Password']
            patient_birthday = json['Birthday']
            patient_gender = json['Gander']
            patient_medicalplan = json['MedicalPlan']
            patient_phone = json['Phone']
            if patient_firstname and patient_lastname and patient_email and patient_password and patient_birthday and patient_gender and patient_medicalplan and patient_phone:
                dao = PatientDao.PatientDAO()
                patient_id = dao.insert(patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone)
                result = self.build_patient_attributes(patient_id, patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone)
                return jsonify(Patient=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deletePatient(self, patient_id):
        dao = PatientDao.PatientDAO()
        if not dao.getPatientById(patient_id):
            return jsonify(Error = "Patient not found."), 404
        else:
            dao.delete(patient_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updatePatientJson(self, patient_id, json):
        dao = PatientDao.PatientDAO()
        if not dao.getPatientById(patient_id):
            return jsonify(Error="Admin not found."), 404
        else:
            patient_firstname = json['FirstName']
            patient_lastname = json['LastName']
            patient_email = json['Email']
            patient_password = json['Password']
            patient_birthday = json['Birthday']
            patient_gender = json['Gander']
            patient_medicalplan = json['MedicalPlan']
            patient_phone = json['Phone']
            if patient_firstname and patient_lastname and patient_email and patient_password and patient_birthday and patient_gender and patient_medicalplan and patient_phone:
                dao.update(patient_id, patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone)
                result = self.build_patient_attributes(patient_id, patient_firstname, patient_lastname, patient_email, patient_password, patient_birthday, patient_gender, patient_medicalplan, patient_phone)
                return jsonify(Patient=result), 200