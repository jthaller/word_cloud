import pickle
import re, string
import numpy as np
import pandas as pd

import json
import pickle
import pandas as pd



mike_json1 = "messages_json/inbox/ZeranJi_XXnwiz4w7g/message_1.json"
mike_json2 = "messages_json/inbox/ZeranJi_XXnwiz4w7g/message_2.json"


rohan_json1 = "messages_json/inbox/RohanKadambi_NQvgRgwgtQ/message_1.json"
rohan_json2 = "messages_json/inbox/RohanKadambi_NQvgRgwgtQ/message_2.json"
rohan_json3 = "messages_json/inbox/RohanKadambi_NQvgRgwgtQ/message_3.json"

sarah_json1 = "messages_json/inbox/SarahRitzmann_qZoMJVMdAQ/message_1.json"
sarah_json2 = "messages_json/inbox/SarahRitzmann_qZoMJVMdAQ/message_2.json"
#there is a message_4.json but I don't think it's a great idea to include messages from 9th grade.
#oldest message in rohan_json3 is from Jan 4 2015

thomas = "Thomas Malchodi"
thomas_json1 = "messages_json/inbox/ThomasMalchodi_PFq8d7gKmg/message_1.json"

true = True


#open JSON, add to dataframe

#needed because facebook did shitty encoding. It was supposed to be utf-8, but then got decoded into latin-1. 
#this function undoes that and fixes the json.
def parse_obj(obj):
    for key in obj:
        if isinstance(obj[key], str):
            obj[key] = obj[key].encode('latin_1').decode('utf-8')
        elif isinstance(obj[key], list):
            obj[key] = list(map(lambda x: x if type(x) != str else x.encode('latin_1').decode('utf-8'), obj[key]))
        pass
    return obj

with open(sarah_json1) as f:
     fixed_json = json.load(f, object_hook=parse_obj)
     df = pd.json_normalize(fixed_json["messages"])


with open(sarah_json2, "r") as f:
    fixed_json = json.load(f, object_hook=parse_obj)
    df.append(pd.json_normalize(fixed_json["messages"]))
    print(df.head())


df = df.drop(columns = ['audio_files','reactions', 'photos', 'call_duration', 'share.link', 'missed', 'videos', 'gifs', 'files', 'sticker.uri', 'timestamp_ms'])

print(df['type'].unique())
df = df[df.type == 'Generic']
df = df[df.content.notnull()]
df = df.drop(columns = 'type')
print(df.head())

# clean up content 
df = df.replace(['(?:\@|https?\://)\S+'], '', regex=True)
# df = df.replace(['honey*'], 'honey')

# df = df.replace('/[^0-9a-zA-Z]/g', "")
#idk wtf went wrong with facebook's encoding that this needs to be fixed
# df = re.sub(r'[\xc2-\xf4][\x80-\xbf]+',lambda m: m.group(0).encode('latin1').decode('utf8'), df)
print(df.head())

print(df.content.str.split(expand=True).stack().value_counts()[20:40])
# print(df.content.str.split(expand=True).stack())


with open('sarah_cleaned_messages_df.pickle', 'wb') as handle:
    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)


