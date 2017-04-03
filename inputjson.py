import json
import requests
from elasticsearch import Elasticsearch

#implement a function
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
with open('json_tweet_results.json') as json_data:
    d = json.load(json_data)
    print(d)
           
es.index(index = 'twitter',doc_type = 'tweets', id =1, body = d)
q = es.get(index = 'twitter',doc_type = 'tweets', id =1)
print(q)


def create_doc(uri, doc_data={}):
    """Create new document."""
    query = json.dumps(doc_data)
    response = requests.post(uri, data=query)
    print(response)
    
if __name__ == '__main__':
    uri_create = 'http://localhost:9200/twitter'
    create_doc(uri_create, {"content": "The fox!"})
    
    #results = search(uri_search, "fox")
    #format_results(results)