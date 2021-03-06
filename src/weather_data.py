import threading
import time

from sensor_reader import SensorReader
from data_fetcher import DataHelper


class WeatherData (threading.Thread):

    def __init__(self, time_stamp):
        threading.Thread.__init__(self)
        self.threadID = time_stamp

        self._sensor_helper = SensorReader()
        self._inside = None

        self._weather_helper = DataHelper('xxxxx', 'xxxxx')
        self._current = None
        self._plus_3_hours = None
        self._plus_6_hours = None
        self._plus_9_hours = None
        self._plus_12_hours = None
        self._plus_1_days = None
        self._plus_2_days = None
        self._plus_3_days = None
        self._plus_4_days = None

    def run(self):
        print ("Starting to fetch data " + self.threadID)
        inside = self._sensor_helper.get_data()
        self._inside = InsideDetails(inside['temperature'], inside['humidity'])
        self._parse_current(self._weather_helper.get_current_weather())
        self._parse_next_hours(self._weather_helper.get_weather_forecast_for_coming_hours()['list'])
        self._parse_next_days(self._weather_helper.get_weather_forecast_for_coming_days()['list'])
        print ("Exiting " + self.threadID)

    def get_inside(self):
        return self._inside


    def get_current_weather(self):
        return self._current

    def get_forecast_next_3_hours(self):
        return self._plus_3_hours

    def get_forecast_next_6_hours(self):
        return self._plus_6_hours

    def get_forecast_next_9_hours(self):
        return self._plus_9_hours

    def get_forecast_next_12_hours(self):
        return self._plus_12_hours

    def get_forecast_plus_1d(self):
        return self._plus_1_days

    def get_forecast_plus_2d(self):
        return self._plus_2_days

    def get_forecast_plus_3d(self):
        return self._plus_3_days

    def get_forecast_plus_4d(self):
        return self._plus_4_days

    def _parse_current(self,data):
        self._current = self._parse_data(data)

    def _parse_next_hours(self,data):
        self._plus_3_hours = self._parse_data(data[0])
        self._plus_6_hours = self._parse_data(data[1])
        self._plus_9_hours = self._parse_data(data[2])
        self._plus_12_hours = self._parse_data(data[3])

    def _parse_next_days(self,data):
        self._plus_1_days = self._parse_data(data[1], True)
        self._plus_2_days = self._parse_data(data[2], True)
        self._plus_3_days = self._parse_data(data[3], True)
        self._plus_4_days = self._parse_data(data[4], True)

    def _parse_data (self, data, long_term=False):

        weather_id = data['weather'][0]['id']
        description = data['weather'][0]['description']
        print(str(data))
        if not long_term:
            time_stamp = time.strftime('%H:%M', time.localtime(data['dt']))
            temp = data['main']['temp']
            wind = data['wind']['speed']
            deg = data['wind']['deg']
            obj = WeatherDetails(time_stamp, wind, deg, weather_id, description, temp=temp)

        else:
            time_stamp = time.strftime('%d.%m.', time.localtime(data['dt']))
            wind = data['speed']
            deg = data['deg']
            temp_day = data['temp']['day']
            temp_night = data['temp']['night']
            obj = WeatherDetails(time_stamp, wind, deg, weather_id, description, temp_day=temp_day, temp_night=temp_night)

        return obj


class WeatherDetails (object):

    def __init__(self, time, wind ,deg, weather_id, description, temp=None, temp_day=None, temp_night=None):
        self.time = time
        self.wind = round(wind)
        self.deg = deg
        self.weather_id = weather_id
        self.description = description
        if temp is not None: self.temp = round(float(temp), 1)
        if temp_day is not None: self.temp_day = round(temp_day, 1)
        if temp_night is not None: self.temp_night = round(temp_night, 1)


class InsideDetails (object):

    def __init__(self,temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

