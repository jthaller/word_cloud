'''Jeremy Thaller
August 2nd, 2020. Munich.

Quick one day build. I ended up not re-using any code.

This script opens a json, fixes the encoding bug, then creates a pandas data frame with 
sender and content columns. The messages are cleaned with regex and then saved as a pickle.
'''

import pickle
import re, string
import pandas as pd
import json


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
            obj[key] = obj[key].replace('â\x80\x99', "\'") #needed to brute force convert these characters
            obj[key] = obj[key].replace('\u00e2\u0080\u0099', "\'") #needed to brute force convert these characters
            obj[key] = obj[key].encode('latin_1').decode('utf-8')
        elif isinstance(obj[key], list):
            obj[key] = list(map(lambda x: x if type(x) != str else x.encode('latin_1').decode('utf-8'), obj[key]))
        pass
    return obj

with open(sarah_json1) as f:
     fixed_json = json.load(f, object_hook=parse_obj)
     df = pd.json_normalize(fixed_json["messages"])

with open(sarah_json2) as f:
    fixed_json = json.load(f, object_hook=parse_obj)
    df.append(pd.json_normalize(fixed_json["messages"]))
    print(df.head())

# drop the messages with shares and pictures and stuff
df = df[df.type == 'Generic']
df = df[df.content.notnull()]
df = df.drop(columns = 'type')

# drop the unused columns. We only care about the "content column" and I'll keep the "sender" column for now
df = df.drop(columns = ['type', 'ip', 'audio_files','reactions', 'photos', 'call_duration', 'share.link', 'missed', 'videos', 'gifs', 'files', 'sticker.uri', 'timestamp_ms'], errors='ignore')



# clean up content 
# df.content = df.content.str.lower()
df = df.replace(['(?:\@|https?\://)\S+'], '', regex=True)
df = df.replace(regex='hone{1,}y{1,}', value='honey')
df = df.replace(regex='(?i)b{3,}', value=' bb')
df = df.replace(regex='(?i)sarah{1,}', value=' Sarah')
df = df.replace(regex='\*', value='')
print(df.head(5))

#save as a pickle. This will be read in by make_cloud.py
with open('sarah_cleaned_messages_df.pickle', 'wb') as handle:
    pickle.dump(df, handle, protocol=pickle.HIGHEST_PROTOCOL)


