import asyncio
import json
import urllib
import traceback

async def get_user(self, name):
    data = urllib.request.urlopen(f"https://api.scratch.mit.edu/user/{name}")
    dj = json.load(data)
    if dj["code"] in "NotFound":
        return traceback.print_tb()
    self.json = data.read()
    self.id = dj["id"]
    self.name = dj["name"]
    self.scratchteam = dj["scratchteam"]
    self.joined_at = dj["history"]["joined"]
    self.status = dj["profile"]["status"]
    self.about = dj["profile"]["bio"]
    self.country = dj["profile"]["country"]
    return self

async def get_icon(name, size):
    userdata = await get_user(name=name)
    id = userdata.id
    data = urllib.request.urlopen(f"https://cdn2.scratch.mit.edu/get_image/user/{id}_{size}x{size}.png")
    return data

async def get_message_count(name):
    a = urllib.request.urlopen(f"https://api.scratch.mit.edu/users/{name}/messages/count")
    b = json.load(a)
    return b["count"]
