""" A simple example of using MQTT for RECEIVING messages. """

import mqtt_remote_method_calls as com
import time
#receiver constanlty runs in the background, then passess to the delegate, the sender doesn't have a delegate

class DelegateThatReceives(object):

    def say_it(self, message,n,who):
        for k in range (n):
            print(who,"sent", message)


def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    my_delegate = DelegateThatReceives()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    while True:
        time.sleep(0.01)  # Time to allow message processing


main()
