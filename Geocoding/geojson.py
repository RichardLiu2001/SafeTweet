import pygeoj
import tweepy
import io
import pyap
import re
import googlemaps
from commonregex import CommonRegex
import pprint
from ernie import SentenceClassifier, Models, AggregationStrategies

classifier = SentenceClassifier(model_path='./model')

def predict(data):
    probabilities = classifier.predict_one(data,
                                       aggregation_strategy=AggregationStrategies.Mean)
    label = None
    if probabilities[0] > probabilities[1]:
        label = "DANGER"
    else:
        label = "SAFE"
    return label

gmaps = googlemaps.Client(key='AIzaSyAKLe-3vkSSHZ67pkBrxEjCnZDffKOUXNU')

consumer_key = '2XFmdLC5dtjfXHkQoRNx5YOxP'
consumer_secret = 'WZO1Y4DUrXStsFPCORLZQy6VTqBMPPMcM7ZX37gyfX5tvKFATu'

access_token = '717047673711239169-PRkvMJn8gzn6yAnFfWj2jFlB3lQK4S4'
access_token_secret = 'rqTN60hRqKC7NtzPNXAmQ3H1oPqcfzdrThTj4YY77Uzq1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twitter_account = "SLMPD"
statuses = api.user_timeline(screen_name=twitter_account,
                           # 200 is the maximum allowed count
                           count=20000,
                           include_rts = True,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'

                           )



#file = pygeoj.load(filepath="nypdtips.geojson")
f = open(twitter_account + ".txt", "a")
#f.write("Now the file has more content!")

geocoding_calls = 0
hits = 0
for status in statuses:
    #print(status.entities['media'][0]['url'])
    #print(status.entities['media'][0]['expanded_url'])
    prediction = predict(status.full_text)
    print(status.full_text + "\n")
    print(prediction)
    if (prediction == "SAFE"):
        continue
    geocode_result = gmaps.geocode(status.full_text)
    geocoding_calls += 1
    if len(geocode_result) == 0:
        continue
    hits += 1
    coordinates = geocode_result[0]['geometry']['location']
    lat = coordinates['lat']
    lng = coordinates['lng']
    url = "https://twitter.com/twitter/statuses/" + str(status.id)
    #print(url + "\n")
    #print(str(lat) + ", " + str(lng) + "\n")
    #newfile.add_feature(properties={"url": url},
                        #geometry={"coordinates": [[(lat, lng)]]})
    f.write(url + "," + str(lat) + "," + str(lng) + "\n")
# add more features...
# features.append(...)



f.close()

print("geocoding api calls: " + str(geocoding_calls))
print("hits: " + str(hits))
#newfile.save("nypdtips.geojson")