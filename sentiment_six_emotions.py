
import pandas as pd
from transformers import pipeline

df = pd.read_csv("Reviews (1).csv", encoding = "ISO-8859-1")


dfs = pd.DataFrame(columns=['University','Professor','Review','sadness', 'joy', 'love', 'anger', 'fear', 'surprise'])
classifier = pipeline("text-classification", model='bhadresh-savani/distilbert-base-uncased-emotion',return_all_scores=True)

for index, row in df.iterrows():
    uni=row['University']
    pro=row['Professor']
    rev=row['Review']

    dfs_row = [uni, pro, rev]
   # print(uni, pro, rev)
    try:
        prediction = classifier(rev, )
   # print([item["label"] for item in prediction[0] ] )
        dfs_row.extend([item["score"] for item in prediction[0]])
        dfs.loc[len(dfs.index)] =  dfs_row
        print(dfs.head())

    except:
        print("value error")
    #print(dfs.head())
    #print(prediction)
dfs.to_csv('review_six_emotions.csv')