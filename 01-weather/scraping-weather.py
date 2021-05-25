import pandas as pd
import requests
from bs4 import BeautifulSoup

addressToScrapeFrom = 'https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995'

page = requests.get( addressToScrapeFrom )
soup = BeautifulSoup ( page.content, 'html.parser' )

# get the full source code of the page - uncomment next line
# print(soup)

# get all a tags (links) - uncomment next line
# print(soup.find_all('a')) 

week = soup.find( id='seven-day-forecast-container' )

# get the html inside of the element with id='seven-day-forecast-container' - uncomment next line
# print( week )

items = week.find_all( class_='tombstone-container' )

# get all items - uncomment next line
# print( items )

# get specific item - uncomment next line
# print( items[0] )

# print( items[0].find( class_='period-name' ).get_text() )
# print( items[0].find( class_='short-desc' ).get_text() )
# print( items[0].find( class_='temp' ).get_text() )

# extract all period-names from items and put them in a list - uncomment next line
period_names = [ item.find(class_='period-name').get_text() for item in items ]
short_descriptions = [ item.find(class_='short-desc').get_text() for item in items ]
temperatures = [ item.find(class_='temp').get_text() for item in items ]

# print( period_names ) - uncomment next line
# print( short_descriptions ) - uncomment next line
# print( temperatures ) - uncomment next line

weather_stuff = pd.DataFrame({ 
    'period': period_names,
    'short_descriptions': short_descriptions,
    'temperatures': temperatures,  
})

print( weather_stuff )

# export to csv
weather_stuff.to_csv( 'weather.csv' )