# Import Dependencies
from flask import Flask, render_template
from flask_pymongo import PyMongo
inport scraping

app = Flask(__name__)

#use Flask_pymongo to set up mongo connections
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = Pymongo(app)

#Define route for the HTML page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)
    
# Add next route and function to our code
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)

# Tell Flask to run
if__name__ == "__main__":
    app.run()