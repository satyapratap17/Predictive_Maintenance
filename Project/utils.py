import pickle
import json
import numpy as np
import config

class MachinePrediction():
    def __init__(self, Type, Air_temperature, Process_temperature, Rotational_speed, Torque,
                 Tool_wear, Temperature_Difference, Power, Mean_Temperature, Wear_strain):
        self.Type = Type
        self.Air_temperature = Air_temperature
        self.Process_temperature = Process_temperature
        self.Rotational_speed = Rotational_speed
        self.Torque = Torque
        self.Tool_wear = Tool_wear
        self.Temperature_Difference = Temperature_Difference
        self.Power = Power
        self.Mean_Temperature = Mean_Temperature
        self.Wear_strain = Wear_strain

    def load_model(self):
        # Load the model and JSON data
        with open(config.MODEL_FILE_PATH, "rb") as file:
            self.model = pickle.load(file)
        with open(config.JSON_FILE_PATH, "r") as file:
            self.json_data = json.load(file)

    def get_prediction(self):
        self.load_model()  # Load the model and JSON data
        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.json_data["Type"][self.Type]
        test_array[1] = self.Air_temperature
        test_array[2] = self.Process_temperature
        test_array[3] = self.Rotational_speed
        test_array[4] = self.Torque
        test_array[5] = self.Tool_wear
        test_array[6] = self.Temperature_Difference
        test_array[7] = self.Power
        test_array[8] = self.Mean_Temperature
        test_array[9] = self.Wear_strain

        prediction = self.model.predict([test_array])
        return prediction[0]


    




