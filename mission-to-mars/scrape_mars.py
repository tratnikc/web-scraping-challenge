# dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import pymongo

mars_dict = {}

def scrape_all():
# chrome driver
# initialize browser MAC
# ----------------------
    executable_path = {'executable_path': "/usr/local/bin/chromedriver"}
    browser = Browser('chrome', **executable_path, headless=False)

# NASA Mars News
# visit NASA Mars News website https://mars.nasa.gov/news/
# ---------------------------------------------------------
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

# scrape page into Soup
# ----------------------
    html = browser.html
    soup = bs(html, 'html.parser')

    sidebar = soup.find_all('ul', class_='item_list')

    for article in sidebar:
        news_title = article.find('div', class_ = 'content_title').get_text()
        news_paragraph = article.find('div', class_='article_teaser_body').get_text()

    mars_dict['news_title'] = news_title
    mars_dict['news_paragraph'] = news_paragraph


# JPL Mars Space Images - Featured Image
# --------------------------------------
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    image_button = browser.find_by_id('full_image')
    image_button.click()
    more_info = browser.links.find_by_partial_text('more info')
    more_info.click()

    html = browser.html
    soup = bs(html, 'html.parser')

    img_url = soup.find('img', class_='main_image')['src']

    url = jpl_url.split('spaceimages')[0]
    url = url[:-1]

    featured_image_url = url + img_url
    mars_dict['featured_image_url'] = featured_image_url


# Mars Facts
# ------------------------------------------------

    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)

    facts_df = pd.read_html(facts_url)[0]

    facts_df.columns=["Description","Mars"]

    facts_df.set_index("Description", inplace=True)

# convert dataframe to html
    facts_html = facts_df.to_html()
    mars_dict['mars_facts'] = facts_html


# Mars Hemispheres
# -----------------------------------------

    h_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(h_url)

    hemi_url = h_url.split('search')[0]

    html = browser.html
    soup = bs(html, 'html.parser')

    divs = soup.find_all('div', class_ = 'collapsible results')

    hemisphere_img_urls = []
    for div in divs:
        items = div.find_all('div', class_='item')
        for item in items:
            dict_sphere  = {}
            
            href = item.find('a')['href']
            href = hemi_url + href
            title = item.find('h3').get_text()

            browser.visit(href)
            time.sleep(2)
            img_link = browser.links.find_by_text('Sample').first['href']
            
            dict_sphere["title"] = title
            dict_sphere["img_url"] = img_link
            
            hemisphere_img_urls.append(dict_sphere)

    browser.quit()
    mars_dict['hemispheres'] = hemisphere_img_urls
    # mars_dict = {"news_title": news_title,
    #          "news_paragraph" : news_paragraph,
    #          "featured_image_url" : featured_image_url,
    #          "mars_facts" : facts_html,
    #          "hemispheres" : hemisphere_img_urls
    #         }
    


# insert to mongoDB
# --------------------------

# setup connection to mongoDB
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

# select database and collection to use; database is mars_db
    db = client.mars_db

    for x in client.list_databases():
        print(x)

# collection is called mars_info
    data = db.mars_info

# insert to data to mars_info collection
    data.insert_one(mars_dict)

    record = db.mars_info.find_one()
    



