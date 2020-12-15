# import libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# List of dictionaries
movie_list = ["Amelie","Sleepless in Seattle", "The Golden Compass"]

# create route that renders html template
@app.route("/")
def main():
    return render_template("index.html", list = movie_list)


if __name__ == "__main__":
    app.run(debug=True)
