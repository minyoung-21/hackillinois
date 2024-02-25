import requests
from decouple import config

def get_live_forecasts(venue_names):
    url = "https://besttime.app/api/v1/forecasts/live"
    forecasts = {}
    for venue_name in venue_names:
        params = {
            'api_key_private': config('BESTTIME_PRIV_API_KEY'),
            'venue_name': venue_name,
        }
        response = requests.get(url, params=params)
        data = response.json()
        forecasts[venue_name] = data
    return forecasts