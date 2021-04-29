from flask import jsonify
from dao import AppointmentDao


class AppointmentHandler:
    def build_appointment_dict(self, row):
        result = {}
        result['appointment_id'] = row[0]
        result['doctor_id'] = row[1]
        result['patient_id'] = row[2]
        result['appointment_date'] = row[3]
        return result

    def build_appointment_attributes(self, appointment_id, doctor_id, patient_id, appointment_date):
        result = {}
        result['appointment_id'] = appointment_id
        result['doctor_id'] = doctor_id
        result['patient_id'] = patient_id
        result['appointment_date'] = appointment_date
        return result

    def getAllAppointments(self):
        dao = AppointmentDao.AppointmentDAO()
        users_list = dao.getAllAppointments()
        result_list = []
        for row in users_list:
            result = self.build_appointment_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getAppointmentById(self, appointment_id):
        dao = AppointmentDao.AppointmentDAO()
        row = dao.getAppointmentById(appointment_id)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            appointments = self.build_appointment_dict(row)
            return jsonify(Appointments = appointments)

    def insertAppointmentJson(self, json):
            doctor_id = json['DoctorId']
            patient_id = json['PatientId']
            appointment_date = json['AppointmentDate']
            if doctor_id and patient_id and appointment_date:
                dao = AppointmentDao.AppointmentDAO()
                appointment_id = dao.insert(doctor_id, patient_id, appointment_date)
                result = self.build_appointment_attributes(appointment_id, doctor_id, patient_id, appointment_date)
                return jsonify(Appointment=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteAppointment(self, appointment_id):
        dao = AppointmentDao.AppointmentDAO()
        if not dao.getAppointmentById(appointment_id):
            return jsonify(Error = "Appointment not found."), 404
        else:
            dao.delete(appointment_id)
            return jsonify(DeleteStatus = "OK"), 200

    def updateAppointmentJson(self, appointment_id, json):
        dao = AppointmentDao.AppointmentDAO()
        if not dao.getAppointmentById(appointment_id):
            return jsonify(Error="Appointment not found."), 404
        else:
            doctor_id = json['DoctorId']
            patient_id = json['PatientId']
            appointment_date = json['AppointmentDate']
            if doctor_id and patient_id and appointment_date:
                dao.update(appointment_id, doctor_id, patient_id, appointment_date)
                result = self.build_appointment_attributes(appointment_id, doctor_id, patient_id, appointment_date)
                return jsonify(Appointment=result), 200