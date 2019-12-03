# web-scraping-challenge

I built a web application that scrapes various websites for data related to the Mars and displays the information in a single HTML page. 

1. Scraping:
Initial scraping was done using Jupyter Notebook, BeautifulSoup, Pandas, Requests/Splinter. Scraping was done on following websites:

NASA Mars News Site: Latest news title and paragraph text was scrapped and assigned to variables

JPL featured Space image: used splinter to navigate the site and find image url for current featured image
and assigned to variable

Mars weather twitter: Scrapped lastest Mars weather tweet and saved it under a variable name

Mars facts: Used pandas to convert the data to a HTML table string

USGS Astrogeology site: navigated, obtained image url, and image title of Mar's hemisphere as dictionary. 

2. MongoDB and flask application:

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

Used Jupyter notebook to convert python data into a Python script and return one Python dictionary containing all of the scraped data.

Next, created a route that will import your scraped script and call scrape function.

Stored the return value in Mongo as a Python dictionary.

Created a root route / that will query Mongo database and pass the mars data into an HTML template to display the data.

Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 