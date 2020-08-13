"""
Under developemnt. It is not optimised.
"""
import elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from textblob import TextBlob
import pandas as pd
import time

# es = Elasticsearch(hosts=[{"host":'elasticsearch'}]) # what should I put here?
es = Elasticsearch(hosts="http://elastic:changeme@elasticsearch:9200/")

df = pd.read_csv('data/BBC-News-Train.csv', sep=',', usecols=['Text'])
text = TextBlob(df.to_string())

def index_text():
    # TODO: change
    for idx, txt in enumerate(text):
        if idx % 1000 == 0:
            print(f"----> {idx} <---")
        es.index(index="text",
                 doc_type="test-type",
                 body={"body_text":    txt,
                       "polarity":     text.sentiment.polarity,
                       "subjectivity": text.sentiment.subjectivity})

# create index
while True:
    try:
        print("Indexing Elasticsearch db... (please hold on)")
        index_text()
        print("...done indexing :-)")
        break
    except (
        elasticsearch.exceptions.ConnectionError,
        elasticsearch.exceptions.TransportError
    ):
        print("---> ES connection is down <--")
        time.sleep(5)
