import Adafruit_DHT

class SensorReader(object):

    def __init__(self):
        self._sensor = Adafruit_DHT.AM2302
        self._pin = 4
        self._humidity = 0
        self._temperature = 0

    def get_data(self):
        """ Try to grab a sensor reading.  Use the read_retry method which will retry up
        to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        """
        humidity, temperature = Adafruit_DHT.read_retry(self._sensor, self._pin)

        """ Note that sometimes you won't get a reading and
        the results will be null (because Linux can't
        guarantee the timing of calls to read the sensor).
        If this happens try again!
        """
        if humidity is not None and temperature is not None:
            self._temperature = round(temperature, 1)
            self._humidity = round(humidity, 1)
        return {'temperature' : self._temperature, 'humidity': self._humidity}