# import libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape_all


# create instance of Flask app
app = Flask(__name__)

# use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)



# create route that renders html template
@app.route("/")
def main():
    #pull some data from mongo
    mars_record = mongo.db.mars_db.find_one()
    print("MAIN" + mars_record)
        
    #show that data
    return render_template("index.html", mars_record = mars_record)

@app.route("/scrape")
def scrape(): 
    scrape_all()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
