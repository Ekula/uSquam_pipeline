from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#q = es.search( index = 'twitter', doc_type ='tweets', body={
#        'query': {
#           'hashtags_list' : 'tudelft',
#            }
#        }
#    )
#print(q)

res = es.search(index="posts", doc_type="blog", body={
    "query": {
        "bool" : {
                "must_not" : {
                    "match" : {"author": "Santa Clause"}
                }
            }
        }
    }
)
print("%d documents found:" % res['hits']['total'])
for doc in res['hits']['hits']:
    print("%s) %s" % (doc['_id'], doc['_source']['author']))