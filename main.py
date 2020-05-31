import time
import paho.mqtt.client as mqtt


ORG = "******"
DEVICE_TYPE = "raspi" 
TOKEN = "************"
DEVICE_ID = "*********"

server = ORG + ".messaging.internetofthings.ibmcloud.com"
pubTopic1 = "iot-2/evt/status1/fmt/json"

authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;


GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print("Calibrating.....")
time.sleep(2)


while True:
       GPIO.output(TRIG, True)
       time.sleep(0.00001)
       GPIO.output(TRIG, False)

       while GPIO.input(ECHO)==0:
          pulse_start = time.time()

       while GPIO.input(ECHO)==1:
          pulse_end = time.time()

       pulse_duration = pulse_end - pulse_start

       distance = pulse_duration * 17150
       distance = round(distance+1.15, 2)

       mqttc.publish(pubTopic1, distance)
       print("published")
  
  
       time.sleep(5*60)