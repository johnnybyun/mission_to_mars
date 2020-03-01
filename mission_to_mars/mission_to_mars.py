from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

def scrape():

    scrapings = {}

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    time.sleep(10)


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('li', class_='slide').find('a').find('h3').text

    news_p = soup.find('li', class_='slide').find('div', class_='article_teaser_body').text

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(5)

    # HTML object
    html = browser.html


    soup = BeautifulSoup(html, 'html.parser')


    image = soup.find('div', class_='image_and_description_container').find_all('img')[1]
    suffix=image['src']



    prefix = 'https://www.jpl.nasa.gov'
    featured_image_url = prefix + suffix



    url = 'https://twitter.com/marswxreport?lang=en'


    response = requests.get(url)
    time.sleep(3)



    soup = BeautifulSoup(response.text, 'html.parser')


    mars_weather = soup.find('p', class_="TweetTextSize")


    url = 'https://space-facts.com/mars/'


    # use the pandas ‘read_html’ function to automatically scrape any tabular data from a page.
    tables = pd.read_html(url)
    tables[0]
    time.sleep(3)




    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemisphere_elements = soup.find_all('h3')
    hemisphere_elements
    hemispheres = [each.text for each in hemisphere_elements]

    time.sleep(15)


    # In[22]:


    hemisphere_image_urls = []
    for i in range(0, 4):
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)
        time.sleep(15)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        dictionary = {}
        partial = hemispheres[i].split(' ')[0]
        browser.click_link_by_partial_text(partial)
        time.sleep(15)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        link = soup.find('a', target="_blank")['href']
        dictionary['title'] = hemispheres[i]
        dictionary['img_url'] = link
        hemisphere_image_urls.append(dictionary)

    # news_title ='The MarCO Mission Comes to an End'
    # news_p = 'The pair of briefcase-sized satellites made history when they sailed past Mars in 2019.'
    # featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA23707-640x350.jpg'
    # mars_weather = 'InSight sol 447 (2020-02-28)...
    # hemisphere_image_urls = [{'title': 'Cerberus Hemisphere Enhanced'...

    scrapings = {}
    scrapings['news_title'] = news_title
    scrapings['news_p'] = news_p
    scrapings['featured_image_url'] = featured_image_url
    scrapings['mars_weather'] = mars_weather
    scrapings['hemisphere_image_urls'] = hemisphere_image_urls

    return scrapings



