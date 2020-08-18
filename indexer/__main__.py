import elasticsearch
from elasticsearch import Elasticsearch, helpers
from textblob import TextBlob
import pandas as pd
import time
import os, uuid
import json


# es = Elasticsearch(hosts=[{"host":'elasticsearch'}]) # what should I put here?
elastic = Elasticsearch(hosts="http://elastic:changeme@elasticsearch:9200/")


def get_data_from_db():
    df = pd.read_csv('data/BBC-News-Train.csv', sep=',', usecols=['Text'])
    # text = df.Text.apply(lambda body_text: TextBlob(body_text))
    return df.to_dict(orient="records")

def bulk_json_data_generator(_index, doc_type):
    """ generator to push bulk data from a file into an Elasticsearch index """
    json_list = get_data_from_db()
    for doc in json_list:
        yield {
                "_index": _index,
                "_type": doc_type,
                "_id": uuid.uuid4(),
                "_source": json.dumps(doc, default=int)
        }


def index_bulk_text():
    try:
        return helpers.bulk(elastic, bulk_json_data_generator(
                        _index="media_text2", doc_type="text2"
                )
        )
    except Exception as e:
        print("\ERROR, ", e)
    return

def search_text(search_term):
    # http: // localhost:9200 / media_text / _search?q = Text:programme
    pass

# create index
while True:
    try:
        print("Indexing Elasticsearch db... (please hold on)")
        index_bulk_text()
        print("...done indexing :-)")
        break
    except (
        elasticsearch.exceptions.ConnectionError,
        elasticsearch.exceptions.TransportError
    ):
        print("---> ES connection is down <--")
        time.sleep(5)
