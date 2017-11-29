import requests
import json


class DataHelper():

    URL_BASE = 'http://api.openweathermap.org/data/2.5'
    UNITS = 'metric'

    def __init__(self, key, city_id):
        self.city_id = city_id
        self.key = key

    def get_current_weather(self):
        return json.loads(self._get_current())

    def get_weather_forecast_for_coming_hours(self):
        return json.loads(self._get_forecast_next_hours())

    def get_weather_forecast_for_coming_days(self):
        return json.loads(self._get_forecast_next_days())

    def _get_current(self):
        url = self.URL_BASE + '/weather?id=' + self.city_id + '&appid=' + self.key + '&units=' + self.UNITS
        return requests.get(url).text

    def _get_forecast_next_hours(self):
        url = self.URL_BASE + '/forecast?id=' + self.city_id + '&appid=' + self.key + '&units=' + self.UNITS
        return requests.get(url).text

    def _get_forecast_next_days(self):
        url = self.URL_BASE + '/forecast/daily?id=' + self.city_id + '&appid=' + self.key + '&units=' + self.UNITS + '&cnt=4'
        return requests.get(url).text

