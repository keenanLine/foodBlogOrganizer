import requests
import re
import feedparser

def scrape():

    sproutedkitchenURL = "https://www.sproutedkitchen.com/?format=rss"
    loveandlemonsURL = "https://www.loveandlemons.com/feed/"
    cookieandkateURL = "https://cookieandkate.com/feed/"
    myNewRootsURL = "http://feeds.feedburner.com/My-New-Roots"
    naturallyEllaURL = "https://naturallyella.com/feed/"
    whatsCookingGoodLookingURL = "http://www.whatscookinggoodlooking.com/?format=rss"
    dollyAndOatmealURL = "http://www.dollyandoatmeal.com/?format=rss"
    theFirstMessURL = "http://feeds.feedburner.com/TheFirstMess"
    myDarlingLemonTimeURL = "http://www.mydarlinglemonthyme.com/feed"

    foodBlogs = [sproutedkitchenURL, loveandlemonsURL, cookieandkateURL]

    text = feedparser.parse(foodBlogs[0])
    print(text['entries'][0]["media_content"][0]['url'])

    dictionaryList = []

    for i in range(0,len(foodBlogs)):
        text = feedparser.parse(foodBlogs[i])
        for j in range(0,2):
            newDictionary = {}
            print(text['entries'][j]['title'])
            newDictionary['title'] = text['entries'][j]['title']
            newDictionary['link'] = text['entries'][j]['link']
            newDictionary['terms'] = []
            for k in range(0,len(text['entries'][j]['tags'])):
                newDictionary['terms'].append(text['entries'][j]['tags'][k]['term'])
            if "media_content" in text['entries'][0].keys():
                newDictionary['image'] = text['entries'][0]["media_content"][0]['url']
        dictionaryList.append(newDictionary)

    return dictionaryList


