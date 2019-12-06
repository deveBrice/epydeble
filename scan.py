import bluetooth, json, datetime
from blscan import get_nearby_devices#, get_rssi_for_devices
import geoip2.database, sqlite3

print("Performing inquiry ... ", end='', flush=True)

nearby_devices = get_nearby_devices()

current_datetime = datetime.datetime.now()
reader = geoip2.database.Reader('./GeoLite2/GeoLite2-City.mmdb')
response = reader.city('109.14.186.24')
time = "{}-{}-{} {}:{}:{}".format(current_datetime.year, current_datetime.month, current_datetime.day, current_datetime.hour, current_datetime.minute, current_datetime.second)

baseDeDonnees = sqlite3.connect('devices.db')
curseur = baseDeDonnees.cursor()
for device in nearby_devices:
    curseur.execute("INSERT INTO Devices (nom, datetime, localisation) VALUES (?, ?, ?)", (device[0], time, response.city.name))
    baseDeDonnees.commit()

baseDeDonnees.close()

nearby_devices = {row[0]: {"name": row[1], "datetime": time, "country": response.city.name} for row in nearby_devices}
reader.close()

print("Found {} devices".format(len(nearby_devices)))
print("Getting RSSI ... ", end='', flush=True)

#get_rssi_for_devices(nearby_devices)

print("Done")
print("Logging ... ", end='', flush=True)

with open("devices.json", "w") as f:
    f.write(json.dumps(nearby_devices))

print("Done")
