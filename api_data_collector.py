import requests
import pandas as pd

class APIDataCollector:
    def __init__(self, api_url):
        self.api_url = api_url

    def make_request(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def process_response(self, data):
        records = []
        for launch in data:
            record = {
                'LaunchID': launch['id'],
                'Name': launch['name'],
                'Details': launch['details'],
                'Date': launch['date_utc'],
                'RocketID': launch['rocket'],

            }
            records.append(record)

        df = pd.DataFrame(records)

        return df