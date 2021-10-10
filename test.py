import random
import pandas as pd


dt = pd.read_json("youtube_list.json")
print(random.choice(dt['links']))