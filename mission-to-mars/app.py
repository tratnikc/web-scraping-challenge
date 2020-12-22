# import libraries
from flask import Flask, render_template, redirect
import pymongo
from scrape_mars import scrape_all, insert_into_mongo


# create instance of Flask app
app = Flask(__name__)

# use PyMongo to establish Mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.mars_db

# collection name
colname = db.mars_info


# List of dictionaries
movie_list = ["Amelie","Sleepless in Seattle", "The Golden Compass"]

# create route that renders html template
@app.route("/")
def main():
    #pull some data from mongo
    record = colname.find_one()
        
    #show that data
    return render_template("index.html", mars_record = record)

@app.route("/scrape")
def scrape(): 
    scrape_all()
    insert_into_mongo()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
