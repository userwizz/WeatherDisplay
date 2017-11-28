import threading
from UI.data_fetcher import DataHelper


class WeatherData (threading.Thread):

    def __init__(self, time_stamp):
        threading.Thread.__init__(self)
        self.threadID = time_stamp

        self.current_temp = 0
        self.current_wind = 0
        self.current_wind_direction = 0
        self.current_description = ""
        self.current_icon = ""

    def run(self):
        print ("Starting " + self.threadID)
        self.get_data()
        print ("Exiting " + self.threadID)

    def get_data(self):
        helper = DataHelper('xxx', 'xxx')
        data = helper.get_current_weather()
        print(data)
        self.current_temp = data['main']['temp']
        self.current_wind = data['wind']['speed']
        self.current_wind_direction = round(data['wind']['deg'], 1)
        self.current_description = data['weather'][0]['description']


