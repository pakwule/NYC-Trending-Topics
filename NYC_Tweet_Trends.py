import tweepy
from time import sleep
from pprint import *
import csv
#Info to get started
consumer_key="Xdh9afKAypPQmDYc3zATu1QiV"
consumer_secret="o1KoTU2pLHQxwRswr3Qtmirq82Ax4qi34Z1dOUN7uu0P4ITnSG"
access_token="245989329-KmnpqhpiO97AY0EZhcTOBpzN2HWL0xcbjgMoVNvF"
access_token_secret="EqEgg1qhS66NNk8o6vW2rlGEFb8E4M9N7awgqYftu3Msp"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret) #Authorizing developer access to Preston's twitter
auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)

def gettrends(woeid):
    trend_dict = {}
    trend_data = api.trends_place(woeid)
    pformat(trend_data)
    dictinfo = trend_data[0]
    listoftrends = dictinfo['trends']
    for element in listoftrends:
        try:
            int(element['tweet_volume']) >= 0
            trend_dict[element['name']] = element['tweet_volume']
        except:
            continue
    return trend_dict
#2514815, 2459115
nyctrends = gettrends(2459115)
print(nyctrends)
#Next... write trends to CSV file and visualize each in R
#make each trend and volume a separate list that can be put into a CSV
trendlistexport = [["Trending Topic","Tweet Volume"]]
for item in nyctrends:
    trendelement = []
    trendelement.append(item)
    trendelement.append(int(nyctrends[item]))
    trendlistexport.append(trendelement)
#print(trendlistexport)
with open('trendtweets.csv', 'w', newline='') as trendfile:
    writeto = csv.writer(trendfile, delimiter=',')
    writeto.writerows(trendlistexport)
    
    
