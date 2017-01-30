#!/usr/bin/env python

# Thanking everyone who wished you birthday
import requests
import json
# Timestamp after which select posts example 12:00:00 AM 

AFTER = 1485648000 # 30-01-2017 12:00:00 AM
####
# GET ACCESS TOKEN before executing this Script
# get token from https://developers.facebook.com/tools/explorer/
# with publish_actions and user_posts
####							

TOKEN = None

def get_posts():
    """Returns dictionary of id, who posted on wall between start and end time"""
    url = 'https://graph.facebook.com/me/posts?since=' + str(AFTER)
    payload = {'access_token': TOKEN}
    r = requests.get(url, params=payload)
    result = json.loads(r.text)
    return result['data']
 
def comment_all(wallposts):
    """Comments Thanks on all posts"""
    for wallpost in wallposts:
        url = 'https://graph.facebook.com/%s/comments' % wallpost['id']
        message = 'Thanks !! :)'
        payload = {'access_token': TOKEN} 
        data = {'message': message}
        s = requests.post(url, params=payload, data=data)
        print "Wall post %s done" % wallpost['id']

if __name__ == '__main__':
	if TOKEN is None:
		print 'get token from https://developers.facebook.com/tools/explorer/ with publish_actions and user_posts'
    comment_all(get_posts())
