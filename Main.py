from flask import Flask, request
from handler.PatientHandler import PatientHandler
from handler.DoctorHandler import DoctorHandler
from handler.AppointmentHandler import AppointmentHandler
from flask_cors import CORS

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is the DevOps App!!'

@app.route('/login/patient', methods=['POST'])
def loginpatient():
    print("REQUEST: ", request.json)
    return PatientHandler().getPatientByEmailAndPass(request.json)

@app.route('/login/doctor', methods=['POST'])
def logindoctor():
    print("REQUEST: ", request.json)
    return DoctorHandler().getDoctorByEmailAndPass(request.json)

@app.route('/patients', methods=['GET', 'POST', 'PUT'])
def patients():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PatientHandler().insertPatientJson(request.json)
    else:
        if not request.args:
            return PatientHandler().getAllPatients()

@app.route('/patient/update/<int:patientid>', methods=['PUT'])
def updatepatient(patientid):
    if request.method == 'PUT':
        print("REQUEST: ", request.json)
        return PatientHandler().updatePatientJson(patientid, request.json)

@app.route('/doctors', methods=['GET', 'POST', 'PUT'])
def doctors():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return DoctorHandler().insertDoctorJson(request.json)
    else:
        if not request.args:
            return DoctorHandler().getAllDoctors()

@app.route('/doctor/update/<int:doctorid>', methods=['PUT'])
def updatedoctor(doctorid):
    if request.method == 'PUT':
        print("REQUEST: ", request.json)
        return DoctorHandler().updateDoctorJson(doctorid, request.json)

@app.route('/doctor/name', methods=['GET'])
def doctorsbyname():
        print("REQUEST: ", request.json)
        return DoctorHandler().getDoctorByFirstAndLastName(request.json)

@app.route('/appointment', methods=['GET', 'POST', 'PUT'])
def appointment():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return AppointmentHandler().insertAppointmentJson(request.json)
    else:
        if not request.args:
            return AppointmentHandler().getAllAppointments()

@app.route('/appointment/update/<int:appointmentid>', methods=['PUT'])
def updateappointment(appointmentid):
    if request.method == 'PUT':
        print("REQUEST: ", request.json)
        return AppointmentHandler().updateAppointmentJson(appointmentid, request.json)

@app.route('/search/<string:filter>/<string:term>', methods=['GET'])
def doctorSearchFiltered(term, filter):
    return DoctorHandler().getDoctorBySearchFiltered(term,filter)

@app.route('/search/<string:term>', methods=['GET'])
def doctorSearch(term):
    return DoctorHandler().getDoctorBySearch(term)

if __name__ == '__main__':
    app.run()