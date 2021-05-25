from os import link
import pandas as pd
import requests
from bs4 import BeautifulSoup

addressToScrapeFrom = 'https://elblogdelnarco.com/?s=morelos'

page = requests.get( addressToScrapeFrom )
soup = BeautifulSoup ( page.content, 'html.parser' )

# get the full source code of the page - uncomment next line
# print(soup)

# get all a tags (links) - uncomment next line
# print(soup.find_all('a')) 

container = soup.find( id='content_box' )

# get the html inside of the element with id='content_box' - uncomment next line
# print( titles )

articles = container.find_all( 'article' )

# get all articles - uncomment next line
# print( articles )

# get specific article - uncomment next line
# print( articles[0] )

# reference properties with [ 'the_property_name' ], tags with find( 'name_of_the_tag' )

link = articles[0].find( 'header' ).find( 'h2' ).find( 'a' )[ 'href' ]
title = articles[0].find( 'header' ).find( 'h2' ).find( 'a' )[ 'title' ]
date = articles[0].find( class_='thetime' ).get_text()


# print( title ) - uncomment this line
# print( link ) - uncomment this line
# print( date ) - uncomment this line



# extract all titles and links and put them in a list - uncomment next line
all_titles = [ article.find( 'header' ).find( 'h2' ).find( 'a' )[ 'href' ] for article in articles]
all_links = [ article.find( 'header' ).find( 'h2' ).find( 'a' )[ 'title' ] for article in articles]
all_dates = [ article.find( class_='thetime' ).get_text() for article in articles ]

# print( all_titles )
# print( all_links )
# print (all_dates )

organized_data = pd.DataFrame({ 
   'title': all_titles,
    'link': all_links,
    'dates': all_dates,
})

print( organized_data )

# export to csv
organized_data.to_csv( 'blog_del_narco_morelos.csv' )