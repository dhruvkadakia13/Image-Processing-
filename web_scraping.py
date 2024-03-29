pip install beautifulsoup4
pip install requests

import requests
from bs4 import BeautifulSoup
from csv import writer
response = requests.get('Enter the URL of the site needed to be scraped')
soup = BeautifulSoup(response.content, 'html.parser')
posts = soup.findAll('div', class_='one.half')
with open('election.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Name']
    csv_writer.writerow(headers)
    for post in posts:
        title = post.find('tr', class_='border_black_bottom').get_text().replace('\n', '')
        name = post.find('tr', class_='border_black_bottom').get_text().replace('\n', '')
        csv_writer.writerow([title, name])
        
