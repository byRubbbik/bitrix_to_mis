from flask import jsonify, request
import requests
import json

from app import app
from app.configuration.config import HEADERS


@app.get("/patient/search")
def patient_search():
    iin = request.args.get("iin")

    link = f"https://api.medelement.com/doctor/v1/patients?iin[]={int(iin)}"
    response = requests.get(link, headers=HEADERS)

    return jsonify(json.loads(response.text))

# successful
@app.get("/specialists/choise")
def choise_spec():
    link = f"https://api.medelement.com/specialties/v1/linked_to_doctor"
    response = requests.get(link, headers=HEADERS)

    return jsonify(json.loads(response.text))

# successful
@app.get("/specialists/timetable")
def specialists_timetable():
    date = request.args.get("date")
    specialty_code = request.args.get("specialty_code")

    link = f"https://api.medelement.com/v1/specialists/timetable?date={date}&specialty_code={int(specialty_code)}"
    response = requests.get(link, headers=HEADERS)

    return jsonify(json.loads(response.text))

# successful
@app.get("/specialists/check_reception")
def check_reception():
    reception_code = request.args.get("reception_code")

    link = f"https://api.medelement.com/v1/doctor/reception/{int(reception_code)}"
    response = requests.get(link, headers=HEADERS)

    return jsonify(json.loads(response.text))


@app.get("/specialists/create_reception")
def create_reception():
    data = {
        "patient_code": int(request.args.get("patient_code")),
        "specialist_code": int(request.args.get("specialist_code")),
        "company_cabinet_code": int(request.args.get("company_cabinet_code")),
        "starttime": request.args.get("starttime"),
        "endtime": request.args.get("endtime"),
        "nomenclature_code": int(request.args.get("nomenclature_code")),
        "description": request.args.get("description")
    }
    link = "https://api.medelement.com/v1/doctor/reception"
    response = requests.post(link, headers=HEADERS, data=data)

    return jsonify(json.loads(response.text))


@app.get("/reception/delete")
def delete_reception():
    reception_code = request.args.get("reception_code")
    link = f"https://api.medelement.com/specialties/v2/doctor/reception/remove"
    data = {
        "reception_code": int(reception_code)
    }
    response = requests.post(link, headers=HEADERS, data=data)
    
    return jsonify(json.loads(response.text))


@app.get("/reception/transfer")
def transfer_reception():
    
    link = f"https://api.medelement.com/specialties/v2/doctor/reception/change_reception_date"
    data = {
        "reception_code": int(request.args.get("reception_code")),
        "doctor_code": int(request.args.get("doctor_code")),
        "start_time": request.args.get("start_time"),
        "end_time": request.args.get("end_time"),
    }
    response = requests.post(link, headers=HEADERS, data=data)
    
    return jsonify(json.loads(response.text))


@app.get("/patient/create")
def patient_create():
    name = request.args.get("name")
    lastname = request.args.get("lastname")
    middlename = request.args.get("middlename")
    gender = request.args.get("gender")
    patient_email = request.args.get("patient_email")
    birthday = request.args.get("birthday")

    data = {
        "name": name,
        "lastname": lastname,
        "middlename": middlename,
        "gender": int(gender),
        "patient_email": patient_email,
        "birthday": birthday
    }

    link = "https://api.medelement.com/doctor/v1/patient"
    response = requests.post(link, headers=HEADERS, data=data)

    return jsonify(json.loads(response.text))
