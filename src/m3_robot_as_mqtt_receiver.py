"""
Using a Brickman (robot) as the receiver of messages.
"""

# Same as m2_fake_robot_as_mqtt_sender,
# but have the robot really do the action.
# Implement just FORWARD at speeds X and Y is enough.
import time
import ev3dev.ev3 as ev3
class DriveSystem(object):
    """
    Controls the robot's motion via GO and STOP methods,
        along with various methods that GO/STOP under control of a sensor.
    """

    def __init__(self):
        """
        What comes in:  Two (optional) sensors.
        What goes out:  Nothing, i.e., None.
        Side effects:
          -- Stores the (optional) sensors.
          -- Constructs two Motors (for the left and right wheels).
        Type hints:
          :type color_sensor:              ColorSensor
          :type infrared_proximity_sensor: InfraredProximitySensor
        """
        self.left_motor = Motor('B')
        self.right_motor = Motor('C')


    def go(self, left_wheel_speed, right_wheel_speed):
        self.left_motor.turn_on(left_wheel_speed)
        self.right_motor.turn_on(right_wheel_speed)

    def stop(self):
        self.left_motor.turn_off()
        self.right_motor.turn_off()

    def go_straight_for_seconds(self, seconds, speed):
        start = time.time()
        self.go(speed, speed)
        # Note: using   time.sleep   to control the time to run is better.
        # We do it with a WHILE loop here for pedagogical reasons.
        while True:
            if time.time() - start >= seconds:
                self.stop()
                break
def main():
    DriveSystem.go()