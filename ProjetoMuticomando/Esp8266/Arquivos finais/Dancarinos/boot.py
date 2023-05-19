from wifi import Wifi
from umqttsimple import MQTTClient

from controlMotor import ControlMotor
from controlLed import ControlLed
from player import Player
from composeActs import Composer

import machine
from time import sleep
import ubinascii
import gc
import json
gc.collect()

# WIFI connection
wifi_connection = Wifi()

wifi_ssid = "rasp-robos"
wifi_pwd = "vxypx2n7"

wifi_connection.connect(wifi_ssid, wifi_pwd)

# MQTT connection
mqtt_server = "192.168.0.110"
client_id = ubinascii.hexlify(machine.unique_id())
message_connection_success = "mini_robo: {}".format(client_id)

topic_pub_status = b"mini_robos/status"
topic_sub_activity = b"mini_robos/activity"

last_message = 0
message_interval = 5

# Robô settings
modo = ""
leds = ""
blink = False

# Components
motors = ControlMotor()
led_control = ControlLed()
#player = Player(0)


def controle(msg):
    global leds, blink
    if blink:
        print(leds)
        led_control.blink(leds, 1)
            
    if msg == "frente":
        motors.controlAll(600, 600)
    elif msg == "tras":
        motors.controlAll(-600, -600)
    elif msg == "direita":
        motors.controlAll(600, -600)
    elif msg == "esquerda":
        motors.controlAll(-600, 600)
    elif msg == "parar":
        motors.controlAll(0, 0)
    elif msg == "true" or msg == "false":
        blink = (True if msg == "true" else False)
        print("Estado do blink %s" % blink)
    elif msg.startswith("musica"):
        _, musica = msg.split("-")
        #player.play_folder(1, musica)
    elif msg.startswith("led"):
        _, leds = msg.split("-") 
        print(leds)
        led_control.change(leds)


def apresentacao(file_position):
    file_name = file_position + ".json"
    
    with open(file_name) as presentation:
        presentation = json.load(presentation)
        lenght = presentation["length"]
        #musica = presentation["music"]
        #player.play_folder(0, musica)
        composer = Composer(presentation, lenght)
        composer.execute()
            
            
def sub_cb(topic, msg):
    global modo
    
    if msg:
        msg = msg.decode("utf-8")
        msg = msg[1:-1]
        if topic == topic_sub_activity:
            if msg == "ControleRemoto" or msg == "Apresentacao":
                modo = msg
                print("Entrando no modo %s" % (modo))
            else:
                if modo == "ControleRemoto":
                    controle(msg)
                elif modo == "Apresentacao":
                    apresentacao(msg)


def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub_activity
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.publish(topic_pub_status, message_connection_success)
  client.subscribe(topic_sub_activity)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub_activity))
  return client


def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  sleep(5)
  

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()