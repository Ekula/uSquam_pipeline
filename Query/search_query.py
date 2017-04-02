from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

q = es.search( index = 'posts', doc_type ='blog', body={
        'query': {
            'awesomeness' : '0.2',
            }
        }
    )
print(q)