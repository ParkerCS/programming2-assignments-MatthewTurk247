# PROBLEM 1 (12pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweetslocated on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.
import requests
from bs4 import BeautifulSoup as soup

url = "https://twitter.com/neiltyson"
page = requests.get(url)

html = page.text
page_soup = soup(html, 'html.parser')

tweets = [x.text.strip() for x in page_soup.findAll("div", class_="js-tweet-text-container")][:5]
print('--------- Twitter ---------')
for tweet in tweets:
    print(tweet)

# string = itself minus 8

# (20pts)
# Below is a link to a 10-day weather forecast at weather.com
# Use urllib and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (10pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:  
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.

url = "https://weather.com/weather/tenday/l/Chicago+IL+USIL0225:1:US"
page = requests.get(url)

html = page.text
page_soup = soup(html, 'html.parser')
ten_days = [x.text.strip() for x in page_soup.findAll("span", class_="date-time")]
descriptions = [x.text.strip() for x in page_soup.findAll("td", class_="description")]
temps = [x.text.strip() for x in page_soup.findAll("td", class_="temp")]
precip = [x.text.strip() for x in page_soup.findAll("td", class_="precip")]
wind = [x.text.strip() for x in page_soup.findAll("td", class_="wind")]
humidity = [x.text.strip() for x in page_soup.findAll("td", class_="humidity")]
dates = [x.text.lower() for x in page_soup.findAll("span", class_="day-detail")]

def short_to_full(d):
    if d == "Mon":
        return "Monday"
    elif d == "Tue":
        return "Tuesday"
    elif d == "Wed":
        return "Wednesday"
    elif d == "Thu":
        return "Thursday"
    elif d == "Fri":
        return "Friday"
    elif d == "Sat":
        return "Saturday"
    elif d == "Sun":
        return "Sunday"
    else:
        return d

print('--------- Weather ---------')

for day in range(len(ten_days)):
    highs_lows = temps[day].replace("--", "°").split("°")[:2]
    high = highs_lows[0]
    low = highs_lows[1]
    if high == '':
        high = 'not available'

    print("{}, {} will be {} with a {} chance of rain and {} humidtiy. Expect wind to be {}. The high is {}° and the low is {}°.".format(short_to_full(ten_days[day]), dates[day].title(), descriptions[day].lower(), precip[day], humidity[day], wind[day], high, low))