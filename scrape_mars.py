{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "import pandas as pd\n",
    "import requests \n",
    "import os\n",
    "from splinter import Browser\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import time\n",
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "executable_path = {'executable_path':\"C:\\\\Users\\\\15404\\\\.wdm\\\\drivers\\\\chromedriver\\\\win32\\\\87.0.4280.88\\\\chromedriver.exe\" }\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA to Host Virtual Briefing on February Perseverance Mars Rover Landing\n",
      "\n",
      "NASA leadership and members of the mission will discuss the agency’s latest rover, which touches down on the Red Planet on Feb. 18.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "url=\"https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest\"\n",
    "response = requests.get(url)\n",
    "soup = bs(response.text,'html.parser')\n",
    "\n",
    "\n",
    "\n",
    "first_title = soup.find('div', class_= \"content_title\").find('a').text.strip()\n",
    "first_paragph = soup.find('div', class_= \"rollover_description_inner\").text.strip()\n",
    "\n",
    "#printing results\n",
    "print(first_title)\n",
    "print(\"\\n\"+first_paragph)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "featured_image_url = \"https://www.jpl.nasa.gov/images/southern-dunes-2/\"\n",
    "browser.visit(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "#using pandas to extract table info\n",
    "url=\"https://space-facts.com/mars/\"\n",
    "table_string= pd.read_html(url)\n",
    "\n",
    "print(len(table_string))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                      0                              1\n",
      "0  Equatorial Diameter:                       6,792 km\n",
      "1       Polar Diameter:                       6,752 km\n",
      "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
      "3                Moons:            2 (Phobos & Deimos)\n",
      "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
      "5         Orbit Period:           687 days (1.9 years)\n",
      "6  Surface Temperature:                   -87 to -5 °C\n",
      "7         First Record:              2nd millennium BC\n",
      "8          Recorded By:           Egyptian astronomers\n",
      "  Mars - Earth Comparison             Mars            Earth\n",
      "0               Diameter:         6,779 km        12,742 km\n",
      "1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
      "2                  Moons:                2                1\n",
      "3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
      "4         Length of Year:   687 Earth days      365.24 days\n",
      "5            Temperature:     -87 to -5 °C      -88 to 58°C\n",
      "                      0                              1\n",
      "0  Equatorial Diameter:                       6,792 km\n",
      "1       Polar Diameter:                       6,752 km\n",
      "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
      "3                Moons:            2 (Phobos & Deimos)\n",
      "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
      "5         Orbit Period:           687 days (1.9 years)\n",
      "6  Surface Temperature:                   -87 to -5 °C\n",
      "7         First Record:              2nd millennium BC\n",
      "8          Recorded By:           Egyptian astronomers\n"
     ]
    }
   ],
   "source": [
    "print(table_string[0])\n",
    "print (table_string[1])\n",
    "print (table_string[2])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls = [\n",
    "    {\"Cerberus Hemisphere Enhanced\": \"Cerberus\", \"img_url\": \"https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\"},\n",
    "    {\"Schiaparelli Hemisphere Enhanced\": \"Schiaparelli\", \"img_url\": \"https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced\"},\n",
    "    {\"Syrtis Major Hemisphere Enhanced\": \"Syrtis\", \"img_url\": \"https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced\"},\n",
    "    {\"Valles Marineris Hemisphere Enhanced\": \"valles\", \"img_url\": \"https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced\"},\n",
    "]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "mongo = PyMongo(app, uri=\"mongodb://localhost:27017/\")\n",
    "#route to render html\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "\n",
    "    # Run the scrape function\n",
    "    costa_data = scrape_costa.scrape_info()\n",
    "\n",
    "    # Update the Mongo database using update and upsert=True\n",
    "    mongo.db.collection.update({}, costa_data, upsert=True)\n",
    "\n",
    "    # Redirect back to home page\n",
    "    return redirect(\"/\")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
