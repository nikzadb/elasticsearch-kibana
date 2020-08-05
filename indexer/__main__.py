from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(hosts=[{"host":'elasticsearch'}]) # what should I put here?

actions = [
    {
    '_index' : 'test',
    '_type' : 'content',
    '_id' : str(item['id']),
    '_source' : item,
    }
for item in [{'id': 1, 'foo': 'bar'}, {'id': 2, 'foo': 'spam'}]
]

# create index
print("Indexing Elasticsearch db... (please hold on)")
bulk(es, actions)
print("...done indexing :-)")