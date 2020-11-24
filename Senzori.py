from sense_hat import SenseHat
import time
import json
import paho.mqtt.publish as publish

MQTT_HOST = 'mqtt.beia-telemetrie.ro'
MQTT_TOPIC = 'training/device/alexandru-negoita'

sense = SenseHat()
sense.clear()

logfile='Negoita-Alexandru.txt'
        
while True:
    pressure = sense.get_pressure()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    print(pressure)
    print(temp)
    print(humidity)

    payload_dict = {"TEMPERATURE" :temp,
            "HUMIDITY": humidity,
            "PRESSURE": pressure}
    def local_save(data):
        file=open(logfile, 'a+')
        file.write(data+'\r\n')
        file.close()
    message="Presure ="+str(pressure)+", Temperature ="+str(temp)+", Humidity ="+ str(humidity)
    try:
        publish.single(MQTT_TOPIC, qos = 1, hostname = MQTT_HOST, payload = json.dumps(payload_dict))
        local_save(message)
    except:
        time.sleep(0.01)
    time.sleep(5)