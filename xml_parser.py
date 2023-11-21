import requests
from bs4 import BeautifulSoup
import pandas as pd

class WebPageScraper:
    def __init__(self, page_url):
        self.page_url = page_url

    def fetch_page_content(self):
        response = requests.get(self.page_url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Error: {response.status_code}")
            return None

    def scrape_page(self, page_content):
        soup = BeautifulSoup(page_content, 'html.parser')

        # Extract information from the webpage
        contributors_section = soup.find('table', {'id': 'contributors'})
        
        # Check if the section is found
        if contributors_section:
            contributors = []
            for contributor_elem in contributors_section.find_all('a'):
                contributor_name = contributor_elem.text.strip()
                contributors.append({'Contributor': contributor_name})
            contributor_count = contributors_section.find_all('span', {'class': 'contrib-count'})
            contributor_counts = [int(count.text.strip()) for count in contributor_count]
        else:
            contributors = []
            contributor_counts = []

        return {'Contributors': contributors, 'ContributorCounts': contributor_counts}