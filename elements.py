import pandas as pd
import json
import random

with open('youtube_list.json') as f:
    data = json.load(f)

# path = pd.DataFrame(data)
pathies = random.choice(data['links'])

print(pathies)

