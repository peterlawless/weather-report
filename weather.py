from secret import api_key
import requests
import requests_mock
import re


def main():
    while True:
        zip_code = input("Enter the 5-digit zip code for your location: ")
        if not re.search(r'^[0-9]{5}$', zip_code):
            print("Invalid input.")
            continue
        else:
            break
    base = "http://api.wunderground.com/api/"
    url = base + api_key + "/conditions/q/zmw:" + zip_code + ".1.99999.json"

    x = requests.get(url).json()['current_observation']
    print(x['temperature_string'])

if __name__ == '__main__':
    main()
