from flask import jsonify, request
import requests
import json

from app import app
from app.configuration.config import HEADERS


@app.get("/patient/")
def patient():
    return jsonify({"message": "successful"})

# successful
@app.get("/specialties/choise")
def choise_spec():
    link = f"https://api.medelement.com/specialties/v1/linked_to_doctor"
    response = requests.get(link, headers=HEADERS)

    return jsonify(json.loads(response.text))

# successful
@app.get("/specialists/timetable")
def specialists_timetable():
    date = request.args.get("date")
    specialty_code = request.args.get("specialty_code")

    link = f"https://api.medelement.com/v1/specialists/timetable?date={date}&specialty_code={specialty_code}"
    response = requests.get(link, headers=HEADERS)

    return jsonify(json.loads(response.text))

# successful
@app.get("/specialists/check_reception")
def check_reception():
    reception_code = request.args.get("reception_code")

    link = f"https://api.medelement.com/v1/doctor/reception/{reception_code}"
    response = requests.get(link, headers=HEADERS)

    return jsonify(json.loads(response.text))