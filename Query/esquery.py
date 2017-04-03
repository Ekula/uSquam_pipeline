import requests
import json

def search(uri, term):
    """Simple Elasticsearch Query"""
    query = json.dumps({
        "query": {
            "match": {
                "hashtags_list": term
            }
        }
    })
    response = requests.get(uri, data=query)
    results = json.loads(response.text)
    return results

def format_results(results):
    """Print results nicely:
    doc_id) content
    """
    data = [doc for doc in results['hits']['hits']]
    for doc in data:
        print("%s) %s" % (doc['_id'], doc['_source']['hashtags_list']))

def create_doc(uri, doc_data={}):
    """Create new document."""
    query = json.dumps(doc_data)
    response = requests.post(uri, data=query)
    print(response)
    

if __name__ == '__main__':
    uri_search = 'http://localhost:9200/twitter/_search'
    uri_create = 'http://localhost:9200/twitter'

    results = search(uri_search, "TUDelft")
    print(results)
    format_results(results)

    #create_doc(uri_create, {"content": "The fox!"})
    #results = search(uri_search, "fox")
    #format_results(results)