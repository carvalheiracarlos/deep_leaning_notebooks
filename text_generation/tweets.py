import snscrape.modules.twitter as sntwitter
import pandas as pd 



query = '(from:jairbolsonaro) until:2022-10-31 -filter:links -filter:replies'
tweets = []
limit = 25000

with open('./xorume_do_bolsonaro.txt', 'w') as fp:
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            fp.close()
            break
        else:
            tweets.append([
                tweet.content
                ])
            fp.write('%s\n' % tweet.content)
        


data_frame = pd.DataFrame(tweets, columns=['Content'])
data_frame.to_csv('./xorume_do_bolsonaro.csv')

print(data_frame)