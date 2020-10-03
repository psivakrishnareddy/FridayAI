
import requests
import json

# API key here
api_key = "xxx"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?" + "APPID=" + api_key


def get_current_weather(city_name):
    # Give city name

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
    # print(x)
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]

        current_humidiy = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

        WD = {
            'CT': str(int(current_temperature) - 275) + '°C',
            'CP':  str(current_pressure) + 'hPa',
            'CH':  str(current_humidiy) + '%',
            'desp':  str(weather_description),
            'ws': str(x['wind']['speed']) + 'kmph',
            'name': str(x['name'])

        }

        # print following values
        print('Weather Details of : ' + str(x['name']))

        return WD

    else:
        return None


# get_current_weather('sriharikota')
