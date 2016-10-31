import tweepy
import csv
from multiprocessing import Pool
from contextlib import closing
from collections import namedtuple
from glob import glob
from goose import Goose
import sys
import os
from exceptions import OSError
goo = Goose()

try :
    from tweetMeta import consumer_key, consumer_secret, access_key, access_secret, target_user_id
except:
    print "copy tweetMeta_sample.py as tweetMeta.py and fill it with your tweeter API keys"
    sys.exit(0)


def get_all_tweets(screen_name,save=False):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    alltweets = []	
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        print "dumping tweets older than %s" % (oldest)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print "...%s tweets downloaded so far" % (len(alltweets))
    if not save:
		return alltweets
    else:
        out_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	    #write the csv	
        with open('%s_tweets.csv' % screen_name, 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(["id","created_at","text"])
            writer.writerows(out_tweets)



rt = get_all_tweets(target_user_id)

article_t=namedtuple('ARTICLE', ['url','title','text','links'])
outfile_name = 'bigtext.txt'
outfile = open(outfile_name,'w')
links = []
def LINK(url):
    if type(url) in [str,unicode]:
        links.append(str(url))
    else:
        pass
        

def LINE(text_line):
    outfile.write(text_line.encode('ascii', 'ignore')+'\n')
    
def ARTICLE(article):
    LINE(article.title)
    for sentence in article.text.split('\n'):
        LINE(sentence)
    return
    
def get_rt_txt(tweet):
    return tweet.retweeted_status.text

def get_text(tweet):
    try:
        t = get_rt_txt(tweet)
        return t
    except:
        return tweet.text
    
def has_links_in_text(text):
    if 'http' in text:
        return True
    else :
        return False
    
def get_links_in_text(text):
    for suffix in text.split('https://t.co/')[1:]:
        code = suffix[:10]
        #assume only one link per tweet
        return 'https://t.co/'+code

try:
    os.mkdir('links')
except OSError:
    [os.remove(link_file) for link_file in glob('links/*')] 

def probe_url(url):
    print 'probing ', url, ': ',
    url_key = url.split('https://t.co/')[1]
    name = 'links/{}.txt'.format(url_key)
    if not name in glob('links/*.txt'):
        try:
            article = goo.extract(url=url)
        except:
            print 'timeout '
            return
        if not 'https://twitter.com/' in article.canonical_link:
            with open(name,'w') as fout:
                fout.write(article.title.encode('ascii', 'ignore')+'\n')
                fout.write(article.cleaned_text.encode('ascii', 'ignore')+'\n')
                print 'OK'
    else:
        print 'cached'
	
texts = map(get_text,rt)

def process_tweet(tw):
    tw_text = get_text(tw)
    LINE(tw_text)
    if has_links_in_text(tw_text):
        url = get_links_in_text(tw_text)
        LINK(url)
    return 0
        
for tw in rt:
	process_tweet(tw)
with closing(Pool(20)) as p_pool:
     p_pool.map(probe_url, links)
outfile.close()

print 'Merging text files in ',
with open('allText.txt','w') as fout:
    print fout.name
    for fname in ['bigtext.txt']+glob('links/*.txt'):
	    print 'merging ',fname
	    with open(fname) as fin:
	        for lin in fin.readlines():
		        if len(lin)>3:
		           fout.write(lin)

