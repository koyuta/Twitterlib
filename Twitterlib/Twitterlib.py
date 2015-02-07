#| -*- coding:utf-8 -*-
import json
from requests_oauthlib import OAuth1Session

TWITTER_API_URL = 'https://api.twitter.com/'

class TwitterClient(object):
    def __init__(self,consumer_key = None, consumer_secret = None, access_token_key = None, access_token_secret = None):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret
        self.client = OAuth1Session(consumer_key,consumer_secret,access_token_key,access_token_secret)
        self.max_id = None

    def __request(self, params, resource,  max_id = None):
        if max_id is not None:
            params.update({'max_id':max_id})
        req = self.client.get(TWITTER_API_URL + resource, params = params)
        if req.status_code == 200:
            timeline = json.loads(req.text)
            if isinstance(timeline, list):
                pass
            elif isinstance(timeline, dict):
                timeline = timeline['statuses']
            self.max_id = timeline[-1]['id_str']
            return timeline

    def __make_alltimelines(self, params, resource, max_count):
        all_timelines = []
        count = params['count']
        if params['count'] <= max_count:
            all_timelines = [timeline for timeline in self.__request(params, resource, self.max_id)]
        else:
            params['count'] = max_count
            for x in range(count/max_count):
                for timelines in self.__request(params, resource, self.max_id):
                    all_timelines.append(timelines)
            params['count'] = count % max_count
            for timelines in self.__request(params, resource, self.max_id):
                all_timelines.append(timelines)
            self.max_id = None
        return all_timelines

    def get_user_timeline(self, screen_name=None, count=20, include_rts=True, exclude_replies=False):
        max_count = 200
        resource = '1.1/statuses/user_timeline.json'
        params = {
                'screen_name':screen_name,
                'count':count,
                'include_rts':include_rts,
                'exclude_replies':exclude_replies,
                }
        return self.__make_alltimelines(params, resource, max_count)

    def search_tweets(self, keyword=None, count=20, result_type='mix'):
        max_count = 100
        resource = '1.1/search/tweets.json'
        params = {
                'q':keyword,
                'count':count,
                'result_type':result_type
                }
        return self.__make_alltimelines(params, resource, max_count)

