#!/usr/bin/env python

"""
https://dev.twitter.com/rest/reference/get

"""

import json
from housepy import config, log
from tweeter import t

# get your own timeline
statuses = t.statuses.home_timeline()
# statuses = t.statuses.user_timeline(screen_name="h0use")  # get someone elses
for status in statuses:
    print("%s: %s" % (status['user']['screen_name'], status['text']))

print('/')

# retrieve followers
follower_ids = t.followers.ids(screen_name="angryhermitbot")['ids']
for follower_id in follower_ids:
    user = t.users.show(user_id=follower_id)
    print(user['screen_name'])

print('/')

# mentions of you
statuses = t.statuses.mentions_timeline()
for status in statuses:
    print("%s: %s" % (status['user']['screen_name'], status['text']))

print('/')

# search for tweets on a topic
topic = "frankenstein"
statuses = t.search.tweets(q=topic)['statuses']
for status in statuses:
    print("%s: %s" % (status['user']['screen_name'], status['text']))

# send a message
# message = "this is a message"
# log.info("Sending \"%s\"" % message)    
# t.statuses.update(status=message)
