# Import SDK packages
import ssl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("TestDevice1", 4, False, True);

# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("ENDPOINT", 8883)
myMQTTClient.configureCredentials("rootCA.pem", "privateKey.pem", "cert.pem")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()
myMQTTClient.publish("myFirstTopic", "hello from TestDevice1!", 0)
# myMQTTClient.subscribe("test/topic", 1, customCallback)
myMQTTClient.unsubscribe("myFirstTopic")
myMQTTClient.disconnect()
