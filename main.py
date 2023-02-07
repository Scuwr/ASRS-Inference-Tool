import redis
import json

r = redis.Redis(port=6397)

database = "v1:"
usertable = "users:"
usernames = "usernames:"
storytable = "stories:"
annotationtable = "annotations:"

def get_annotation(username, storyid):
    userid = [key.decode('utf-8') for key in r.smembers(database + usernames + username)][0].split(':')[2]
    annotation = r.hget(f'{database + annotationtable + userid}:{storyid}', 'annotation')

    data = json.loads(annotation)
    print(data)

get_annotation('cmarnold', 1)