import oauth2 as oauth
from urllib.parse import quote_plus
import json

# 
# The code in this file won't work until you set up your Twitter "app"
# at https://dev.twitter.com/apps
# After you set up the app, copy the four long messy strings and put them here.
#

CONSUMER_KEY = "quI4EXqGt0qvBAuDl4q0ripBm"
CONSUMER_SECRET = "krTlB3yad0h43cLd4NoRAoNkFV7zmiim6TKCgp8DNElMUNSuKy"
ACCESS_KEY = "419716095-fxSL9wPlcwcsHij2z1FG4j3bml9b9vlNSobbJACY"
ACCESS_SECRET = "fOfl8gbBKF8MmSFLumHXDHMmRWQ3pLDkfnRkTMHgWRM6e"

# Call this function after starting Python.  It creates a Twitter client object (in variable client)
# that is authorized (based on your account credentials and the keys above) to talk
# to the Twitter API. You won't be able to use the other functions in this file until you've
# called authTwitter()
#
def authTwitter():
    
    global client   
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
    client = oauth.Client(consumer, access_token)


# Study the documenation at https://dev.twitter.com/rest/public/search
# to learn about construction Twitter queries and the format of the results
# returned by Twitter
#

# Try:
#       searchTwitter("finals")
#
# Iowa City's lat/lng is [41.6611277, -91.5301683] so also try:
#      searchTwitter("finals", latlngcenter=[41.6611277, -91.5301683])
#
def searchTwitter(searchString, count = 20, radius = 10, latlngcenter = None):
    global query
    global response
    global data
    global resultDict
    global tweets
    
    query = "https://api.twitter.com/1.1/search/tweets.json?q=" + quote_plus(searchString) + "&count=" + str(count)

    if latlngcenter != None:
        query = query + "&geocode=" + str(latlngcenter[0]) + "," + str(latlngcenter[1]) + "," + str(radius) + "km"

    response, data = client.request(query)
    data = data.decode('utf8')
    resultDict = json.loads(data)
    # The key information in resultDict is the value associated with key 'statuses' (Twitter refers to
    # tweets as 'statuses'
    tweets = resultDict['statuses']
    gCount = 0
    for tweet in tweets:
        if tweet['coordinates'] != None:
            gCount = gCount + 1
            print(tweet['coordinates'], printable(tweet['text']))
        else:
            print(printable(tweet['text']))            
        print()
    print(gCount)
    

def whoIsFollowedBy(screenName):
    global response
    global resultDict
    
    query = "https://api.twitter.com/1.1/friends/list.json?&count=50"
    query = query + "&screen_name={}".format(screenName)
    response, data = client.request(query)
    data = data.decode('utf8')
    resultDict = json.loads(data)
    for person in resultDict['users']:
        print(person['screen_name'])
    
def getMyRecentTweets():
    global response
    global data
    global statusList 
    query = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    response, data = client.request(query)
    data = data.decode('utf8')
    statusList = json.loads(data)
    for tweet in statusList:
        print(printable(tweet['text']))
        print()

def printable(s):
    result = ''
    for c in s:
        result = result + (c if c <= '\uffff' else '?')
    return result
 
