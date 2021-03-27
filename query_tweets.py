import tweepy
import io
target = io.open("mytweets.txt", 'w', encoding='utf-8')

import csv




consumer_key = '2XFmdLC5dtjfXHkQoRNx5YOxP'
consumer_secret = 'WZO1Y4DUrXStsFPCORLZQy6VTqBMPPMcM7ZX37gyfX5tvKFATu'

access_token = '717047673711239169-PRkvMJn8gzn6yAnFfWj2jFlB3lQK4S4'
access_token_secret = 'rqTN60hRqKC7NtzPNXAmQ3H1oPqcfzdrThTj4YY77Uzq1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#news = api.get_status("1217645826870272000")
#print(news.text)

#newsFile = open("news_outlets.txt", "r")

#count = 0;
#for aline in newsFile.readlines():
    #print(aline)
    #news = api.get_status(str(aline)).text

    #print(news)
    #count += 1;
    #if (count > 100):
    #    break

#newsFile.close()



#public_tweets = api.home_timeline()
statuses = api.user_timeline(screen_name='NYPDTips',
                           # 200 is the maximum allowed count
                           count=20000,
                           include_rts = True,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'

                           )

#print(tweets)
count = 0;
target = io.open("nypdtips.csv", 'w', encoding='utf-8')
#writer = csv.writer(csv_file, delimiter=',')
target.write("tweet_text\t")
target.write("id\t")

for status in statuses:
    print(status)
    #print(status.id)
    count += 1
    #print(status.full_text)
    #target.write(status.full_text + "\t")
    #target.write(str(status.id) + "\n")
    #writer.writerow(status.full_text.encode(encoding='UTF-8'))

print("total: " + str(count))
#for status in statuses:
   #print(dir(status))
    #print(type(status))
    #print("text: " + status.full_text)
   # print("entities: " + str(status.entities))
    #print("geo: " + str(status.geo))
    #print("coordinates: " + str(status.coordinates))
    #print("place: " + str(status.place) + "\n")
    #print("source: " + str(status.source))

   # print("parse: " + str(status.parse))
    #print(dir(status.parse))
   # print("text: " + status.text + "\n")


     #print("ID: {}".format(info.id))
     #print(info.created_at)
     #print(info.full_text)
    #line = status.full_text;
    #line = line.replace('\r', '').replace('\n', '')

    #target.write(line + '\n')


#print("\n")
#search = api.search(q="KVUE", count = 10)

#trends = api.trends_place()

#print("Search: " + str(search))
#print(str(type(search)))

#for tweet in search:

    #print(type(tweet.text))
    #print(tweet.text)