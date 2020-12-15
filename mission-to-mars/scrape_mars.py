# dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# chrome driver
# initialize brower MAC
def init_browser():
    executable_path = {'executable_path': "/usr/local/bin/chromedriver"}
    return Browser('chrome', **executable_path, headless=False)

# NASA Mars News
def scrape_info():
    browser = init_browser()
    # visit NASA Mars News website https://mars.nasa.gov/news/
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)
    
    # scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    sidebar = soup.find_all('ul', class_='item_list')

    for article in sidebar:
        news_title = article.find('div', class_ = 'content_title').get_text()
        news_paragraph = article.find('div', class_='article_teaser_body').get_text()
    
    # close the browser after scraping
    browser.quit()

    # return the title and paragraph
    return news_title, news_paragraph


# JPL Mars Space Images - Featured Image
def mars_featured_image():
    browser = init_browser()
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
    return featured_image_url


# Mars Facts
def mars_facts():
    browser = init_browser()
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)

    facts_df = pd.read_html(facts_url)[0]

    facts_df.columns=["Description","Mars"]

    facts_df.set_index("Description", inplace=True)

    facts_df


# Mars Hemispheres

h_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(h_url)


# %%
hemi_url = h_url.split('search')[0]
hemi_url


# %%
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


# %%
hemisphere_img_urls


# %%
browser.quit()


# %%



