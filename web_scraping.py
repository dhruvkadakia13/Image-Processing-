#pip install beautifulsoup4
#pip install requests

# we import the class that we need scraping our blog
import requests
from bs4 import BeautifulSoup
from csv import writer
# we create a response variable
response = requests.get('https://electoralsearch.in/Home/VoterInformation')
# we initialize beautiful soup and pass in our response
soup = BeautifulSoup(response.content, 'html.parser')
# we create a variable called posts and we know that our all our blog posts are in a div called blog-entry-content
posts = soup.findAll('div', class_='one.half')
# writing to csv file
with open('election.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    # creating headers in the csv file
    headers = ['Title', 'Name']
    # writing a row of headers in the csv
    csv_writer.writerow(headers)
    # now lets loop through our posts
    for post in posts:
        title = post.find('tr', class_='border_black_bottom')#.get_text().replace('\n', '')
        name = post.find('tr', class_='border_black_bottom')#.get_text().replace('\n', '')
        csv_writer.writerow([title, name])
        
