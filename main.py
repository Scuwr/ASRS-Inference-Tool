import redis
import json

import torch
from diffusers import StableDiffusionPipeline

r = redis.Redis(port=6397)

database = "v1:"
usertable = "users:"
usernames = "usernames:"
storytable = "stories:"
annotationtable = "annotations:"

def get_annotation(username, storyid):
    userid = [key.decode('utf-8') for key in r.smembers(database + usernames + username)][0].split(':')[2]
    annotation = r.hget(f'{database + annotationtable + userid}:{storyid}', 'annotation')

    return json.loads(annotation)

annotation = get_annotation('cmarnold', 1)
name = annotation['node_names'][1]['name']

model_id = "CompVis/stable-diffusion-v1-4"
model = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
model = model.to('cuda:0')

for node in annotation['node_names']:
    prompt = node['name']
    image = model(prompt).images[0]
    short_name = " ".join(prompt.split(' ')[:2])
    print(short_name)
    image.save(f'inference/{short_name}.png')