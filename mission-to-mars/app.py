# import libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape_all, insert_into_mongo


# create instance of Flask app
app = Flask(__name__)

# use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# create route that renders html template
@app.route("/")
def main():
    #pull some data from mongo
    record = mongo.db.mars_info.find_one()
        
    #show that data
    return render_template("index.html", mars_record = record)

@app.route("/scrape")
def scrape(): 
    scrape_all()
    insert_into_mongo()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
