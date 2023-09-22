from elasticsearch import Elasticsearch


# docker run --rm -p 9200:9200 -p 9300:9300 -e "xpack.security.enabled=false" -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.7.0

# Some setup stuff
es = Elasticsearch("http://localhost:9200")
es.indices.refresh(index="games")


# Some example queries
body = {
    "query": {   
        "terms": {
            "genres": ["Adventure"]
        }
    }
}

# body = {
#     "query": {
#         "range": { 
#             "release_date": {
#                 "gte":"2012-12-01", 
#                 "lte":"2012-12-31",
#             }
#         }
#     }
# }

# body = {
#     "query": {
#         "bool": {
#             "must": [
#                 {
#                     "match": {
#                             "developers": "Naughty Dog"
#                     }
#                 },
#                 { 
#                     "range": {
#                         "rating": {
#                             "gte": 3
#                         }
#                     }
#                 }
#             ]
#         }
#     }
# }


# Execute the search (you might get a deprecation warning about the body parameter but it works)
resp = es.search(index="games", body=body)

# Printing results
print(resp)
print(resp.body.keys())
print(resp.body['hits']['hits'])

