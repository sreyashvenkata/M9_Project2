import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.current_page = 1

    def scrape_data(self):
        url = urljoin(self.base_url, f'page/{self.current_page}')
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: {response.status_code}")
            return None

    def parse_data(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        quotes = []
        for quote_elem in soup.find_all('span', class_='text'):
            quote_text = quote_elem.text.strip()
            quotes.append({'Quote': quote_text})

        return quotes

    def has_next_page(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        next_button = soup.find('li', class_='next')
        return next_button is not None

    def scrape_all_pages(self):
        all_quotes = []

        while True:
            html_content = self.scrape_data()

            if html_content:
                quotes_data = self.parse_data(html_content)
                all_quotes.extend(quotes_data)

                if not self.has_next_page(html_content):
                    break
                else:
                    self.current_page += 1
            else:
                break

        return all_quotes