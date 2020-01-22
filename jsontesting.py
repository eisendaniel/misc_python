import json
with open("dicts.json") as f:
    dicts = json.load(f)

partition = dicts["partition"]
labels = dicts["labels"]
