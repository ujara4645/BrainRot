from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, MultiSearch, Q, Range

# docker run --rm -p 9200:9200 -p 9300:9300 -e "xpack.security.enabled=false" -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.7.0

################ Setup ########################
client = Elasticsearch("http://localhost:9200")
s = Search().using(client)


################ Search queries ################
# Get first 10 hits for games that are on either PS4 or PS5
# s = s.filter('terms', platforms__keyword=['PlayStation 4', 'PlayStation 5'])
# response = s.execute()

# for hit in s:
#     print(hit.title)


# # Get all hits for games that are in the Adventure and Indie genres
# s = s.query('match', genres='Adventure').query('match', genres='Indie')
# response = s.execute()

# for hit in s.scan():
#     print(hit.title)


# Get first 20 hits for games that are in the Shooter genre and released before 2010
# date_range = Q('range', release_date={'lt': '2020-01-01'})
s = s.query('match', genres='Shooter')
s = s.filter('range', **{'release_date':{'lt': '2020-01-01'}})
response = s.execute()
s = s[10:30]

for hit in s:
    print(hit.release_date)
