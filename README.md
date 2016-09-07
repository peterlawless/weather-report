## weather-report

The purpose of this repository is to create a Python application that will pull
data from multiple <a href="http://api.wunderground.com/api/">Weather Underground API</a>
endpoints and present a weather report to the user.

The learning objectives for this assignment repository is to:

* Understand the purpose and structure of Web APIs
* Understand JSON structure
* Be able to access an API using a token
* Be able to make HTTP requests via requests
* Be able to pull and merge information from multiple API endpoints
* Be able to write tests that mock API responses

To successfully use this repository, you must sign up for an API key and save it
as a string with the variable name *api_key* in a file called secret.py in the
same directory as this repository.

When the you run the application weather.py, you will be asked for a zip code, and
 then you will be asked for a number to select from a menu of options including
current location, ten-day forecast, sunrise and sunset times, and current
 hurricanes (anywhere).
