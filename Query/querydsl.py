from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

response = es.search(
    index="twitter",
    body={
      "query": {
        "bool": {
          "must": [{"match": {"hashtags_list": "tu delft"}}],
          #"must_not": [{"match": {"description": "beta"}}]
          #"filter": [{"term": {"category": "search"}}]
        }
      },
#      "aggs" : {
#        "per_tag": {
#          "terms": {"field": "tags"},
#          "aggs": {
#            "max_lines": {"max": {"field": "lines"}}
#          }
#        }
#      }
    }
)

for hit in response['hits']['hits']:
    print(hit['_score'], hit['_source']['hashtags_list'])
#
#for tag in response['aggregations']['per_tag']['buckets']:
#    print(tag['key'], tag['max_lines']['value'])