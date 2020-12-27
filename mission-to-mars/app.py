# import libraries
from flask import Flask, render_template, redirect
import pymongo
from scrape_mars import scrape_all


# create instance of Flask app
app = Flask(__name__)

# use PyMongo to establish Mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
# define database to use
db = client.mission_to_mars
#define collection
mars = db.mars_info

# create route that renders html template
@app.route("/")
def main():
    #pull some data from mongo
    mars_record = db.mars_info.find_one()
    
    #show that data
    return render_template("index.html", mars_record = mars_record)

@app.route("/scrape")
def scrape(): 
    mars_dict = scrape_all()
    # update current record, if not found then insert record to mars_info collection
    mars.update({}, mars_dict, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
