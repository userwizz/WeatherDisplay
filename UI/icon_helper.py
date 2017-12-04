
class IconHelper (object):

    def __init__(self):
        self.values = {
            # thunderstorm
            200: '63.png',
            201: '63.png',
            202: '63.png',
            210: '63.png',
            211: '63.png',
            212: '64.png',
            221: '61.png',
            230: '63.png',
            231: '63.png',
            232: '63.png',
            # drizzle
            300: '31.png',
            301: '31.png',
            302: '31.png',
            310: '31.png',
            311: '31.png',
            312: '31.png',
            313: '31.png',
            314: '31.png',
            321: '31.png',
            # rain
            500: '21.png',
            501: '22.png',
            502: '23.png',
            503: '23.png',
            504: '23.png',
            511: '33.png',
            520: '33.png',
            521: '33.png',
            522: '33.png',
            531: '33.png',
            # snow
            600: '41.png',
            601: '42.png',
            602: '41.png',
            611: '71.png',
            612: '72.png',
            615: '71.png',
            616: '73.png',
            620: '51.png',
            621: '52.png',
            622: '53.png',
            # atmosphere
            701: '91.png',
            711: '91.png',
            721: '91.png',
            731: '91.png',
            741: '91.png',
            761: '91.png',
            762: '91.png',
            771: '91.png',
            781: '91.png',
            # clear
            800: '1.png',
            # clouds
            801: '2.png',
            802: '3.png',
            803: '3.png',
            804: '3.png',

        }

    def get_icon_path(self, weather_id):
        if weather_id in self.values:
            print (str(weather_id) + ' -> icon =  ' + self.values[weather_id])
            return '../resource/' + self.values[weather_id]
        else:
            print ('No icon found for: ' + str(weather_id))
            return '../resource/92.png'


