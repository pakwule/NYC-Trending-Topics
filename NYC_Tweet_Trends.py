import tweepy
from time import sleep
from pprint import *
import csv
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='Insert Username', api_key='Insert Plotly API Key')
#Info to get started
consumer_key="Insert Your Key"
consumer_secret="Insert Secret Script"
access_token="Insert Access Token"
access_token_secret="Insert Token Secret Script"

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
#Next... write trends to CSV file and visualize
#make each trend and volume a separate list that can be put into a CSV
trendlistexport = [["Trending Topic","Tweet Volume"]] #Makes trendlist to write into csv
for item in nyctrends:
    trendelement = []
    trendelement.append(item)
    trendelement.append(int(nyctrends[item]))
    trendlistexport.append(trendelement)
with open('trendtweets.csv', 'w', newline='') as trendfile: #puts trend list items in CSV
    writeto = csv.writer(trendfile, delimiter=',')
    writeto.writerows(trendlistexport)
xtrends = []
trendvolumes = []
for item in trendlistexport:
    xvalue = item[0]
    xtrends.append(xvalue)
for item in trendlistexport:
    yvalue = item[1]
    trendvolumes.append(yvalue)
del xtrends[0]
del trendvolumes[0]

data = [go.Bar(
            x=xtrends,
            y=trendvolumes)]
data = data
layout = go.Layout(
    title='Trending Topic vs. Volume of Tweets',
    xaxis=dict(
        title='Trending Topic',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Volume of Tweets',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='styling-names')


