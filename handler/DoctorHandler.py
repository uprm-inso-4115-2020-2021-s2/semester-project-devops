from flask import jsonify
from dao import DoctorDao
from util import util

class DoctorHandler:
    def build_doctor_dict(self, row):
        result = {}
        result['doctor_id'] = row[0]
        result['doctor_firstname'] = row[1]
        result['doctor_lastname'] = row[2]
        result['doctor_email'] = row[3]
        result['doctor_password'] = row[4]
        result['doctor_specialization'] = row[5]
        result['doctor_location'] = row[6]
        result['doctor_phone'] = row[7]
        return result

    def build_doctor_dict_public(self, row):
        result = {}
        result['doctor_firstname'] = row[0]
        result['doctor_lastname'] = row[1]
        result['doctor_email'] = row[2]
        result['doctor_specialization'] = row[3]
        result['doctor_location'] = row[4]
        result['doctor_phone'] = row[5]
        result['doctor_description'] = row[6]
        return result

    def build_doctor_attributes(self, doctor_id, doctor_firstname, doctor_lastname, doctor_email, doctor_password, doctor_specialization, doctor_location, doctor_phone, doctor_description, doctor_licence):
        result = {}
        result['doctor_id'] = doctor_id
        result['doctor_firstname'] = doctor_firstname
        result['doctor_lastname'] = doctor_lastname
        result['doctor_email'] = doctor_email
        result['doctor_password'] = doctor_password
        result['doctor_specialization'] = doctor_specialization
        result['doctor_location'] = doctor_location
        result['doctor_phone'] = doctor_phone
        result['description'] = doctor_description
        result['licence'] = doctor_licence
        return result

    def getAllDoctors(self):
        dao = DoctorDao.DoctorDAO()
        users_list = dao.getAllDoctors()
        result_list = []
        for row in users_list:
            result = self.build_doctor_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getDoctorById(self, doctor_id):
        dao = DoctorDao.DoctorDAO()
        row = dao.getDoctorById(doctor_id)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            doctors = self.build_doctor_dict(row)
            return jsonify(Doctors = doctors)
    
    def getDoctorBySearchFiltered(self, term, filter):
        processedTerm = util.Utilities().termProcessing(term)
        dao = DoctorDao.DoctorDAO()
        doctor_list = dao.getDoctorBySearchFiltered(processedTerm.lower(), filter)
        result_list = []
        if not doctor_list:
            return jsonify(Error = "No doctors meet search criteria"), 404
        else:
            for row in doctor_list:
                result = self.build_doctor_dict_public(row)
                result_list.append(result)
            return jsonify(Doctors = result_list)
    
    def getDoctorBySearch(self, term):
        processedTerm = util.Utilities().termProcessing(term)
        dao = DoctorDao.DoctorDAO()
        doctor_list = dao.getDoctorBySearch(processedTerm.lower())
        result_list = []
        if not doctor_list:
            return jsonify(Error = "No doctors meet search criteria"), 404
        else:
            for row in doctor_list:
                result = self.build_doctor_dict_public(row)
                result_list.append(result)
            return jsonify(Doctors = result_list)

    def getDoctorByEmailAndPass(self, json):
        email = json['email']
        password = json['password']
        if email and password:
            dao = DoctorDao.DoctorDAO()
            row = dao.getDoctorByEmailAndPass(email, password)
            if not row:
                return jsonify(Error = "Doctor Not Found"), 404
            return jsonify(Patient = "Doctor Found!"), 201
        return jsonify(Error="Missing attributes in request"), 400

    def getDoctorByFirstAndLastName(self, json):
        firstname = json['FirstName']
        lastname = json['LastName']
        if firstname and lastname:
            dao = DoctorDao.DoctorDAO()
            row = dao.getDoctorByFirstAndLastName(firstname, lastname)
            if not row:
                return jsonify(Error = "Doctor Not Found"), 404
            doctors = self.build_doctor_dict(row)
        return jsonify(Doctors=doctors)

    def insertDoctorJson(self, json):
            print(json)
            doctor_firstname = json['FirstName']
            doctor_lastname = json['LastName']
            doctor_email = json['Email']
            doctor_password = json['Password']
            doctor_specialization = json['Specialization']
            doctor_location = json['Location']
            doctor_phone = json['Phone']
            doctor_description = json['Description']
            doctor_licence = json['Licence']
            if doctor_firstname and doctor_lastname and doctor_email and doctor_password and doctor_specialization and doctor_location and doctor_phone and doctor_description and doctor_licence:
                dao = DoctorDao.DoctorDAO()
                doctor_id = dao.insert(doctor_firstname, doctor_lastname, doctor_email, doctor_password, doctor_specialization, doctor_location, doctor_phone,doctor_description, doctor_licence)
                result = self.build_doctor_attributes(doctor_id, doctor_firstname, doctor_lastname, doctor_email, doctor_password, doctor_specialization, doctor_location, doctor_phone, doctor_description, doctor_licence)
                return jsonify(Doctor=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteDoctor(self, doctor_id):
        dao = DoctorDao.DoctorDAO()
        if not dao.getDoctorById(doctor_id):
            return jsonify(Error = "Doctor not found."), 404
        else:
            dao.delete(doctor_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateDoctorJson(self, doctor_id, json):
        dao = DoctorDao.DoctorDAO()
        if not dao.getDoctorById(doctor_id):
            return jsonify(Error="Admin not found."), 404
        else:
            doctor_firstname = json['FirstName']
            doctor_lastname = json['LastName']
            doctor_email = json['Email']
            doctor_password = json['Password']
            doctor_specialization = json['Specialization']
            doctor_location = json['Location']
            doctor_phone = json['Phone']
            doctor_description = json['Description']
            doctor_licence = json['Licence']
            if doctor_firstname and doctor_lastname and doctor_email and doctor_password and doctor_specialization and doctor_location and doctor_phone and doctor_description and doctor_licence:
                dao.update(doctor_id, doctor_firstname, doctor_lastname, doctor_email, doctor_password, doctor_specialization, doctor_location,  doctor_phone, doctor_description, doctor_licence)
                result = self.build_doctor_attributes(doctor_id, doctor_firstname, doctor_lastname, doctor_email, doctor_password, doctor_specialization, doctor_location, doctor_phone, doctor_description, doctor_licence)
                return jsonify(Doctor=result), 200