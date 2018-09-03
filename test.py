#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename : test.py
# date : 2018-09-03

# IMPORT
import json, config
import requests
from requests_oauthlib import OAuth1Session
from dateutil.parser import parse
from datetime import datetime
from time import sleep
import argparse

twitter = OAuth1Session(config.CONSUMER_KEY,
                        config.CONSUMER_SECRET,
                        config.ACCESS_TOKEN,
                        config.ACCESS_TOKEN_SECRET)
TW_END_POINT = 'https://api.twitter.com/1.1/search/tweets.json'

LINE_END_POINT = "https://notify-api.line.me/api/notify"

def line_notify(message):
    
    token = config.LINE_ACCESS_TOKEN
    headers = {"Authorization" : "Bearer "+ token}

    payload = {"message" :  'Tweet内容:' + message}
    
    r = requests.post(LINE_END_POINT ,headers = headers ,params=payload)
    
def search_tweet(query):
    query = query + " exclude:retweets lang:ja"
    params = {
        'q': query,
        'count': 5
    }
    req = twitter.get(TW_END_POINT,params=params)
    if req.status_code == 200:
        tweets = json.loads(req.text)
        return tweets['statuses']
    else:
        return -1
    

# DEFINE METHOD
if __name__ == '__main__' :

    parser = argparse.ArgumentParser(description='検索対象のツイートがあったらLINEに通知するスクリプト。５分に一回検索をかけて知らせてくれる')

    parser.add_argument(
        "-q",
        "--query",
        help="検索ワード。複数あるときはスペース区切りをダブルクォーテーションで括ってください。",
        required=True,
        action="store"
    )

    args = parser.parse_args()
    query = args.query
    now_time = datetime.now()

    while(1):
        tweets = search_tweet(query)
        if tweets != -1:
            for tw in tweets:
                dt = parse(tw['created_at'],ignoretz=True)
                if dt > now_time:
                    line_notify(tw['text'])
        else:
            line_notify('error')
            exit(-1)
            
        now_time = datetime.now()
        sleep(360)
        
