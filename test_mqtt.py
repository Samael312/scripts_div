import paho.mqtt.client as mqtt
import sys

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("✅ ¡CONECTADO EXITOSAMENTE!")
        client.subscribe("universidad/jaen/#")
    else:
        print(f"❌ Error de conexión. Código: {rc}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect


broker = "autorack.proxy.rlwy.net"
port = 35512

try:
    print(f"Intentando conectar a {broker}:{port}...")
    client.connect(broker, port, 60)
    client.loop_forever()
except Exception as e:
    print(f"💥 No se pudo establecer la conexión: {e}")