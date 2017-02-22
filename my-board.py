# Import SDK packages
# import ssl - is this useful?
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# For Websocket connection
myMQTTClient = AWSIoTMQTTClient("my-board", useWebsocket=True)

# AWS IoT MQTT Client
myMQTTClient.configureIAMCredentials("ID", "SECRET")

# Configurations
# For Websocket
myMQTTClient.configureEndpoint("ENDPOINT", 443)

# For Websocket, we only need to configure the root CA
myMQTTClient.configureCredentials("rootCA.pem")

myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()
myMQTTClient.publish("myFirstTopic", "hello from my-board, I'm using a WebSocket!", 0)
# myMQTTClient.subscribe("test/topic", 1, customCallback)
myMQTTClient.unsubscribe("myFirstTopic")
myMQTTClient.disconnect()