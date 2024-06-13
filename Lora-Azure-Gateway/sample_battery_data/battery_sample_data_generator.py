import json
import os
import time
import random
from datetime import datetime

time_now = datetime.now() #Tag und aktuelle Uhrzeit
time_str = time_now.strftime("%Y-%m-%d %H:%M:%S") #Konvertierung zum String

def get_battery_data():
    timestamp = time_str
    battery_voltage     = round(3.7  + (0.1 * random.random()), 2) #Spannung
    battery_current     = round(30   + (0.2 * random.random()), 2) #Stromstärke
    battery_capacity    = round(2600 - (100 * random.random()), 2) #Kapazität
    battery_soc         = round(100  - (10  * random.random()), 2) #State of Charge
    return {"timestamp":    timestamp, 
            "voltage":      battery_voltage, 
            "current":      battery_current, 
            "capacity":     battery_capacity, 
            "soc":          battery_soc}

def write_to_json(data, folder, filename): #Batteriedaten in JSON-Datei schreiben
    if not os.path.exists(folder): #Sicherstellung das Ordner für JSON-Dateien existiert
        os.makedirs(folder)
    
    filepath = os.path.join(folder, filename)
    with open(filepath, "w") as json_file: #w: write
        json.dump(data, json_file)

__name__ == "__main__"
folder_path = "battery_data" #Ordner für JSON-Dateien

while True:
    timestamp = int(time.time()) #Unix-Zeitstempel
    filename = f"battery_data_{timestamp}.json"
    battery_data = get_battery_data()
    write_to_json(battery_data, folder_path, filename)
    print("Battery data written to JSON:", battery_data)
    time.sleep(2) #Neue Datei alle 2 Sekunden

    
