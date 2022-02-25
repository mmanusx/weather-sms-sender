# https://www.openweathermap.org For Weather API
# https://www.latlong.net/  Latitude and Longitude Finder
import requests
from twilio.rest import Client  # twillo.com programble sms provider
import os

# twilio app
# from twilio console
account_sid = os.environ['***']
auth_token = os.environ['***']

# open weather app
LAT= 41.008240
LON= 28.978359
api_key = "ad20fc35f451a9d6f3054d4fb0adf517"
parameters = {"lat": LAT,
              "lon": LON,
              "appid": api_key,
              "exclude": "current,minutely,daily"

              }
url = "https://api.openweathermap.org/data/2.5/onecall"

# API connection
response = requests.get(url=url, params=parameters) # server için html client girilmeli kodlaı daha farklı
# print(response.status_code) # if response code is 200 connection success
response.raise_for_status()
data = response.json()                                                        # http://jsonviewer.stack.hu/ json reader
weather_slice = data["hourly"][:12]                                           # taking first 12 hour data list

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        #print("Bring an umbrella.")
# print(data["hourly"][0]["weather"][0]["id"])

if will_rain:
    # print("Bring an umbrella.")
    # twilio send sms codes
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+1859295',
        to='+9'
    )

    # print(message.sid)
    print(message.status)





