from flask import Flask, request, jsonify, render_template
import config
from Project.utils import MachinePrediction  # Corrected import
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('input.html')

@app.route('/input', methods=["POST", "GET"])
def predict_maintenance():
    if request.method == "POST":
        data = request.form
        Type = data["Type"]
        Air_temperature = float(data["Air_temperature"])
        Process_temperature = float(data["Process_temperature"])
        Rotational_speed = float(data["Rotational_speed"])
        Torque = float(data["Torque"])
        Tool_wear = float(data["Tool_wear"])
        Temperature_Difference = float(data["Temperature_Difference"])
        Power = float(data["Power"])
        Mean_Temperature = float(data["Mean_Temperature"])
        Wear_strain = float(data["Wear_strain"])

        machine = MachinePrediction(Type, Air_temperature, Process_temperature, Rotational_speed, Torque,
                                          Tool_wear, Temperature_Difference, Power,
                                          Mean_Temperature, Wear_strain)
        
        prediction = machine.get_prediction()
        if prediction == 0:
            msg = "The Machine is in Good Health"
        else:
            msg = "The Machine is damaged "

        print(prediction)

        return render_template('output.html', machine_prediction=prediction, message=msg)

if __name__ == "__main__":
    app.run(debug=True)

