# web-scraping-challenge

## Mission to Mars

### included

1. mission_to_mars.ipynb
2. scrape_mars.py
3. app.py
4. index.html in templates folder
5. mission_to_mars_01.png mission_to_mars_02.png and in screenshots folder

### Requirements
1. Scraping
    * [NASA Mars News](https://mars.nasa.gov/news/) - scrape website and collect the latest News Title and Paragraph Text
    * [JPL Mars Space Images - Featured Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) - use splinter to visit the site and find the image url for the current Featured Mars Image. Use the full size .jpg image.
    * [Mars Facts](https://space-facts.com/mars/) - use Pandas to scrape the table containing facts about the planet.
    * [Mars Hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) - visit the USGS Astrogeology site to obtain high resolution images for each of Mars's hemispheres.

2. MongoDB and Flask Application
    * convert jupyter notebook into a Python script scrape_mars.py and return one python dictionary
    * create a route called /scrape that will import scrape_mars.py and call scrape function, store the return value in Mongo as a python dictionary
    * create a template HTML file called index.html that will take the mars data dictionary and display all of the appropriate HTML elements.

3. Screenshots of final application

### Screenshots

<img src="https://github.com/tratnikc/web-scraping-challenge/blob/main/screenshots/mission_to_mars_01.png" width="400" height="400"/>

### Note: I have installed the chromedriver in my local machine to use Splinter.
