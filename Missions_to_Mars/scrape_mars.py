#!/usr/bin/env python
# coding: utf-8

# # Scraping NASA Mars News

#importing dependensies, imported webdriver because request was not able to handle the data
from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser


def scrape():
    executable_path = {"executable_path": r'C:\Users\Samita\Desktop\12-Web-Scraping-and-Document-Databases\Assignment\web-scraping-challenge\Missions_to_Mars\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url_news = "https://mars.nasa.gov/news/"
    browser.visit(url_news)
    html_news = browser.html
    soup_news = BeautifulSoup(html_news, 'html.parser')

    results = soup_news.find_all("div", class_= "list_text")
    print(results)

    titles= []

    for result in results:
        titles.append(result.find('a').text)
    news_title = titles[0]

    paragraphs = []
    for result in results:
        paragraphs.append(result.find("div", class_='article_teaser_body').text)

    news_paragraph = paragraphs[0]

    # # Scraping JPL Mars Space Image
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
    browser.visit(url2)
    html_image = browser.html
    soup = BeautifulSoup(html_image, 'html.parser')
    images = soup.find_all("div", class_="img")

    featured_images = []
    for image in images:
        featured_images.append(image.img['src'])
    
    featured_image_url = 'https://www.jpl.nasa.gov/' + featured_images[0]


    # # Scraping Mars Weather twitter account
    url3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    html_weather = browser.html
    soup_weather = BeautifulSoup(html_weather, "html.parser")

    tweets = soup_weather.find_all("div", class_="js-tweet-text-container")

    weather = []
    for tweet in tweets:
        weather.append(tweet.find('p').text)
    
    mars_weather = weather[0]


    # # Mars facts
    url4 = "https://space-facts.com/mars/"
    datafile = pd.read_html(url4)

    Mars_df = datafile[0]
    Mars_df.columns = ["Description", "Value"]
    Mars_df.set_index("Description", inplace = True)
    Mars_info = Mars_df.to_html(classes= "table table-striped")


    # # Mars Hemisphere
    url5 = "https://web.archive.org/web/20181114171728/https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url5)
    html_hemi = browser.html
    soup_hemi = BeautifulSoup(html_hemi, 'html.parser')

    Titles = []
    captions = soup_hemi.find_all('h3')
    for caption in captions:
        Titles.append(caption.text)
    
    image_url=[]
    count=0
    for thumb in Titles:
        browser.find_by_css('img.thumb')[count].click()
        image_url.append(browser.find_by_text('Sample')['href'])
        browser.back()
        count=count+1
    
    hemisphere_image_urls = []
    counter = 0
    for item in image_url:
        hemisphere_image_urls.append({"title":Titles[counter],"img_url":image_url[counter]})
        counter = counter+1

    mars_data = {
        "news_title":news_title,
        "news_paragraph":news_paragraph,
        "mars_image":featured_image_url,
        "mars_weather":mars_weather,
        "mars_facts":Mars_info,
        "hemisphere_image_url":hemisphere_image_urls
    }

    return mars_data

if __name__ =="__main__":
    print(scrape()) 

    





