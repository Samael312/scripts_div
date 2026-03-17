import paho.mqtt.client as mqtt
import time
import json

BROKER = "autorack.proxy.rlwy.net"
PORT = 35512
TOPIC = "universidad/jaen/sensor1"

    
def on_publish(client, userdata, mid, reason_code=None, properties=None):
    print(f"📤 Confirmación recibida del Broker (ID: {mid})")

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ Conexión establecida con el puente de Railway")
    else:
        print(f"❌ Error de conexión: {rc}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_publish = on_publish

try:
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    while True:
        payload = {"valor": 25.4, "status": "ok"}
        mensaje = json.dumps(payload)
        client.publish(TOPIC, mensaje, qos=1)
        time.sleep(10)

except KeyboardInterrupt:
    print("Deteniendo...")
finally:
    client.loop_stop()
    client.disconnect()