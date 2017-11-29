import threading
import time
from UI.data_fetcher import DataHelper


class WeatherData (threading.Thread):

    def __init__(self, time_stamp):
        threading.Thread.__init__(self)
        self.threadID = time_stamp
        self.init_values()
        self.current_weather = []
        self.weather_now_dict = {'temp' : 0,
                                  'wind' : 0,
                                  'direction' : 0,
                                  'description' : "",
                                  'temp_day' : 0,
                                  'temp_night' : 0}

    def run(self):
        print ("Starting " + self.threadID)
        helper = DataHelper('xxx', 'xxx')

        self.parse_current(helper.get_current_weather())
        self.parse_next_hours(helper.get_weather_forecast_for_coming_hours()['list'])
        self.parse_next_days(helper.get_weather_forecast_for_coming_days()['list'])

        print ("Exiting " + self.threadID)


    def parse_current(self,data):
        print (data)
        """
        self.current_temp = data['main']['temp']
        self.current_wind = data['wind']['speed']
        self.current_wind_direction = round(data['wind']['deg'], 1)
        self.current_description = data['weather'][0]['description']
        """
        self.weather_now_dict['temp'] = data['main']['temp']
        self.weather_now_dict['wind'] = data['wind']['speed']
        self.weather_now_dict['direction'] = round(data['wind']['deg'], 1)
        self.weather_now_dict['description'] = data['weather'][0]['description']

    def parse_next_hours(self,data):
        self.plus_3h_time = time.strftime('%H:%M', time.localtime(data[0]['dt']))
        self.plus_3h_temp = data[0]['main']['temp']
        self.plus_3h_wind = data[0]['wind']['speed']
        self.plus_3h_wind_direction = round(data[0]['wind']['deg'], 1)
        self.plus_3h_description = data[0]['weather'][0]['description']

        self.plus_6h_time = time.strftime('%H:%M', time.localtime(data[1]['dt']))
        self.plus_6h_temp = data[1]['main']['temp']
        self.plus_6h_wind = data[1]['wind']['speed']
        self.plus_6h_wind_direction = round(data[1]['wind']['deg'], 1)
        self.plus_6h_description = data[1]['weather'][0]['description']

        self.plus_9h_time = time.strftime('%H:%M', time.localtime(data[2]['dt']))
        self.plus_9h_temp = data[2]['main']['temp']
        self.plus_9h_wind = data[2]['wind']['speed']
        self.plus_9h_wind_direction = round(data[2]['wind']['deg'], 1)
        self.plus_9h_description = data[2]['weather'][0]['description']

    def parse_next_days(self,data):
        self.plus_1d_time = time.strftime('%H:%M', time.localtime(data[0]['dt']))
        self.plus_1d_temp_day = data[0]['temp']['day']
        self.plus_1d_temp_night = data[0]['temp']['night']
        self.plus_1d_wind = data[0]['speed']
        self.plus_1d_wind_direction = round(data[0]['deg'], 1)
        self.plus_1d_description = data[0]['weather'][0]['description']

        self.plus_2d_time = time.strftime('%H:%M', time.localtime(data[1]['dt']))
        self.plus_2d_temp_day = data[1]['temp']['day']
        self.plus_2d_temp_night = data[1]['temp']['night']
        self.plus_2d_wind = data[1]['speed']
        self.plus_2d_wind_direction = round(data[1]['deg'], 1)
        self.plus_2d_description = data[1]['weather'][0]['description']




    def init_values(self):

        # current weather
        self.current_temp = 0
        self.current_wind = 0
        self.current_wind_direction = 0
        self.current_description = ""
        self.current_icon = ""

        # forecast for coming hours
        self.plus_3h_time = ""
        self.plus_3h_temp = 0
        self.plus_3h_wind = 0
        self.plus_3h_wind_direction = 0
        self.plus_3h_description = ""

        self.plus_6h_time = ""
        self.plus_6h_temp = 0
        self.plus_6h_wind = 0
        self.plus_6h_wind_direction = 0
        self.plus_6h_description = ""

        self.plus_9h_time = ""
        self.plus_9h_temp = 0
        self.plus_9h_wind = 0
        self.plus_9h_wind_direction = 0
        self.plus_9h_description = ""

        # forecast for coming days
        self.plus_1d_time = ""
        self.plus_1d_temp_day = 0
        self.plus_1d_temp_night = 0
        self.plus_1d_wind = 0
        self.plus_1d_wind_direction = 0
        self.plus_1d_description = ""

        self.plus_2d_time = ""
        self.plus_2d_temp_day = 0
        self.plus_2d_temp_night = 0
        self.plus_2d_wind = 0
        self.plus_2d_wind_direction = 0
        self.plus_2d_description = ""





