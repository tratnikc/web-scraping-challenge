# import libraries
from flask import Flask, render_template
from scrape_mars import main_scrape

# create instance of Flask app
app = Flask(__name__)


# List of dictionaries
movie_list = ["Amelie","Sleepless in Seattle", "The Golden Compass"]

# create route that renders html template
@app.route("/")
def main():
    #pull some data from mongo
    #show that data
    return render_template("index.html", list = movie_list)

@app.route("/scrape")
def scrape(): 
    main_scrape()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
