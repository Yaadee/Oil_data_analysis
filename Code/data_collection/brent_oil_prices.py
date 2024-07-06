import wbdata
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def scrape_geopolitical_events():
    url = 'https://www.reuters.com/news/archive/oil'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    events = []
    for item in soup.find_all('article', class_='story'):
        event_title = item.find('h3', class_='story-title').text.strip()
        event_date = item.find('time').get('datetime').split('T')[0]
        event_description = item.find('p', class_='summary').text.strip()
        events.append({
            'Source': 'Reuters',
            'date': event_date,
            'Title': event_title,
            'Description': event_description
        })
    
    return events

if __name__ == "__main__":
    geopolitical_events = scrape_geopolitical_events()
    events_df = pd.DataFrame(geopolitical_events)
    events_df.to_csv('geopolitical_events.csv', index=False)

