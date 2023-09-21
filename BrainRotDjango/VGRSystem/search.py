from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

def search(genres):
    client = Elasticsearch("http://localhost:9200")
    s = Search(using=client)
    s = s.filter('match', genres="First person shooter")    
    response = s.execute()

    for hit in s:
        print(hit.genres)

    return response

search("action")


