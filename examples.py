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
print("My timeline:")
for status in statuses:
    print("%s: %s" % (status['user']['screen_name'], status['text']))

print('/')

# retrieve followers
screen_name = "angryhermitbot"
print("Followers of %s: " % screen_name)
follower_ids = t.followers.ids(screen_name=screen_name)['ids']
for follower_id in follower_ids:
    user = t.users.show(user_id=follower_id)
    print(user['screen_name'])

print('/')

# mentions of you
print("Mentions of me:")
statuses = t.statuses.mentions_timeline()
for status in statuses:
    print("%s: %s" % (status['user']['screen_name'], status['text']))

print('/')

# search for tweets on a topic
print("Mentions of frankenstein:")
topic = "frankenstein"
statuses = t.search.tweets(q=topic)['statuses']
for status in statuses:
    print("%s: %s" % (status['user']['screen_name'], status['text']))

# send a message
# message = "this is a message"
# log.info("Sending \"%s\"" % message)    
# t.statuses.update(status=message)
