import scrapy
from bs4 import BeautifulSoup
import csv

class AFLCIOSpider(scrapy.Spider):
    name = 'aflcio_beautifulsoup_spider'
    allowed_domains = ['aflcio.org']
    start_urls = ['https://aflcio.org/what-unions-do/social-economic-justice/advocacy/legislative-alerts']

    def parse(self, response):
        # Create a BeautifulSoup object from the response content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all legislative alert items (adjust according to the actual HTML structure)
        legislative_alerts = soup.find_all('div', class_='views-row')

        # Prepare CSV output
        with open('legislative_alerts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            # Extract data for each legislative alert
            for alert in legislative_alerts:
                title_tag = alert.find('h2')
                if title_tag:
                    title = title_tag.get_text(strip=True)
                    url = title_tag.find('a')['href'] if title_tag.find('a') else None

                    # Write to CSV
                    writer.writerow({'title': title, 'url': url})
