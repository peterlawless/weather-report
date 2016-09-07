from secret import api_key
import requests
import re


class WeatherReport:
    def __init__(self, zip_code, api_key):
        self.zip_code = zip_code
        self.api_key = api_key

    def get_json(self, endpoint):
        base = "http://api.wunderground.com/api/"
        url = base + api_key + "/" + endpoint + "/q/zmw:" + self.zip_code + ".1.99999.json"
        return requests.get(url).json()

    def get_current_conditions(self):
        data = self.get_json('conditions')['current_observation']
        print(data['display_location']['full'])
        print(data['weather'], "with a visibility of ",
              data['visibility_mi'], " miles.")
        print("Wind is blowing ", data['wind_dir'], "at ",
              data['wind_mph'], "mph with gusts reaching ",
              data['wind_gust_mph'], " mph.")
        print("Temperature: ", data['temperature_string'])
        print()

    def get_ten_day_forecast(self):
        data = self.get_json('forecast10day')['forecast']['txt_forecast']['forecastday']
        for item in data:
            print(item['title'] + ":")
            print(item['fcttext'], "\n")

    def get_alerts(self):
        data = self.get_json('alerts')['alerts'][0]
        print(data['description'], "in effect until", data['expires'])

    def get_sunrise_and_sunset(self):
        data = self.get_json('astronomy')['sun_phase']
        print("Sunrise at", data['sunrise']['hour'] + ":" +
              data['sunrise']['minute'])
        print("Sunset at", data['sunset']['hour'] + ":" +
              data['sunset']['minute'])


def main():
    while True:
        zip_code = input("Enter the 5-digit zip code for your location: ")
        if not re.search(r'^[0-9]{5}$', zip_code):
            print("Invalid input.")
            continue
        else:
            break
    while True:
        print("Please select your report: ")
        print("1. Current Conditions")
        print("2. Ten Day Forecast.")
        print("3. Current Weather Alerts")
        print("4. Sunrise and Sunset Times")
        selection = input('>>> ')
        if selection not in ['1', '2', '3', '4']:
            print("Invalid input.")
            continue
        else:
            break
    weather_report = WeatherReport(zip_code, api_key)
    if selection == '1':
        weather_report.get_current_conditions()
    elif selection == '2':
        weather_report.get_ten_day_forecast()
    elif selection == '3':
        weather_report.get_alerts()
    elif selection == '4':
        weather_report.get_sunrise_and_sunset()

if __name__ == '__main__':
    main()
