from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

# TODO: change play, ..., reviews to passing in a comparison lambda
def search(title="", rating=0, developers=[], genres=[], summary="", platforms=[], 
           plays=0, playing=0, backlogs=0, wishlist=0, lists=0, reviews=0, release_date=""):
    client = Elasticsearch("http://localhost:9200")
    s = Search(using=client)
    s = s.filter('match', developers=["Naughty Dog"])    
    response = s.execute()

    for hit in s.scan():
        print(hit.genres)

    return response

search(genres=["Adventure"])


