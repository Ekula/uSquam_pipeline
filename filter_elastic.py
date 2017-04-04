from elasticsearch import Elasticsearch


def filter_elastic(tweets, tag):
    print 'Ignore Tag: ' + tag
    if tag is None or tag == 'None':
        return tweets

    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    es.indices.delete(index='_all', ignore=[400, 404])

    for i in range(0, len(tweets)):
        es.index(index='twitter_final', doc_type='twitter_tweets', id=i, body=tweets[i], refresh=True)

    res = es.search(index="twitter_final", doc_type="twitter_tweets", body={
        "query": {
            "bool": {
                "must_not": {
                    "match": {"hashtags_list": tag}
                }
            }
        }
    })

    results = []
    print("%d documents found:" % res['hits']['total'])
    for doc in res['hits']['hits']:
        results.append(doc['_source'])

    return results
