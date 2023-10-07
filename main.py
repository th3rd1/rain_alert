import requests
# import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "87f2e59d9d39ca248fb3c2613be32c53"
account_sid = "AC9d2ea2228ff6ae3398d6344273e7aaf6"
auth_token = "ace565c973450dfdd93658746739e885"


weather_params = {
    "lat": 17.287330,
    "lon": -62.697868,
    "appid": api_key,
    "exclude": "current,minutely,daily",
    "units": "metric"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:5]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
print(will_rain)

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain, remember to bring an umbrella.",
        from_="+18449062538",
        to="+18479174438"
    )


    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    # message = client.messages \
    #     .create(
    #     body="It is going to rain, remember to bring an umbrella.",
    #     twilio #: from_="+18449062538",
    #     user #: to="+18479174438"
