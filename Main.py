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

@app.route('/patients', methods=['GET', 'POST'])
def patients():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PatientHandler().insertPatientJson(request.json)
    else:
        if not request.args:
            return PatientHandler().getAllPatients()

@app.route('/doctors', methods=['GET', 'POST'])
def doctors():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return DoctorHandler().insertDoctorJson(request.json)
    else:
        if not request.args:
            return DoctorHandler().getAllDoctors()

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return AppointmentHandler().insertAppointmentJson(request.json)
    else:
        if not request.args:
            return AppointmentHandler().getAllAppointments()

if __name__ == '__main__':
    app.run()