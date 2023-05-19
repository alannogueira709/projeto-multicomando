"""
from wifi import Wifi
from umqttsimple import MQTTClient

# Wifi settings
wifi = Wifi()

wifi_ssid = ""
wifi_pwd = ""

wifi.connect(wifi_ssid, wifi_pwd)

# MQTT settings
mqtt_server = ""
client_id = ubinascii.hexlify(machine.unique_id())
message_connection_success = "mestre: {} online".format(client_id)

topic_sub_status = b"mini_robos/status"
topic_pub_activity = b"mini_robos/activity"

last_message = 0
message_interval = 5

# Robô settings
robos_online = 0
robos_id = []

def sub_cb(topic, msg):
    global modo, leds, blink
    print((topic, msg))
    if topic == topic_sub_status:
    msg = str(msg)[2:-1]
    if msg.startswith("mini_robo"):
        _, robo_id = msg.split(":")
        if robo_id not in robos_id:
            robos_id.append(robo_id)
            robos_online = len(robos_id)
        

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
    sleep(10)
    reset()


try:
    client = connect_and_subscribe()
except OSError as e:
    restart_and_reconnect()
"""