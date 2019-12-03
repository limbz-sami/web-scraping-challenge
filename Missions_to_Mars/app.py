from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# setup mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#create route to query Mongodatabase
@app.route("/")
def home():
    # find one record from mongodb
    mars_data = mongo.db.mars_data.find_one()

    # Return the mars data into an html template 
    return render_template('index.html', mars_data= mars_data)


@app.route("/scrape")
def scrapper():
    #run scrape funtion
    
    mars_scrape = scrape_mars.scrape()

    #update mongodb using update and upsert
    mongo.db.mars_data.update({},mars_scrape, upsert=True)

    #redirect back to homepage
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
