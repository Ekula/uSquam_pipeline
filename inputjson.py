import json
from elasticsearch import Elasticsearch

#implement a function
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
with open('json_tweet_results.json') as json_data:
    d = json.load(json_data)
    #print(d)
           
es.index(index = 'twitter',doc_type = 'tweets', id =1, body = d)
q = es.get(index = 'twitter',doc_type = 'tweets', id =1)
print(q)