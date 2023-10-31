from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Document, Q
from elasticsearch_dsl.query import MoreLikeThis
import numbers
import requests
import urllib3
import json

# Tuples ("", 0) or ("", "") are (comparator, values)
# e.g.: playing = ("lt", 1000) or release_date = ("gte", "2020-01-01")
# TODO: change play, ..., reviews to passing in a comparison lambda
def search(title="", rating=("", -1), developers=[], genres=[], summary="", platforms=[],
           plays=("", -1), playing=("", -1), backlogs=("", -1), wishlist=("", -1), lists=("", -1),
           reviews=("", -1), release_date=("", "")):
    # Setup connection to ES cluster
    client = Elasticsearch("http://localhost:9200")
    s = Search(using=client)

    # Organize arguments
    comparison_args = {'rating': rating,
                       'plays': plays,
                       'playing': playing,
                       'backlogs': backlogs,
                       'wishlist': wishlist,
                       'lists': lists,
                       'reviews': reviews,
                       'release_date': release_date}

    match_args = {'title': title,
                  'summary': summary}

    term_args = {'developers': developers,
                 'genres': genres,
                 'platforms': platforms}

    # Loop over comparison arguments, check if it's valid, if it's a date or int, and add to query
    for comp_key in comparison_args.keys():
        comp_val = comparison_args[comp_key]
        if comp_val[0]:
            if isinstance(comp_val[1], numbers.Number) and comp_val[1] > 0:
                s = s.query('range', **{comp_key: {comp_val[0]: comp_val[1]}})
            else:
                s = s.query('range', **{comp_key: {comp_val[0]: comp_val[1]}})

    # Loop over term arguments, check if it's valid, if there's 1 or more than 1, and add to query
    for term_key in term_args.keys():
        term_val = term_args[term_key]

        if term_val:
            if len(term_val) == 1:
                s = s.query('match', **{term_key: term_val[0]})
            else:
                s = s.query('terms', **{term_key + '__keyword': term_val})

    # Loop over match arguments, check if it's valid, and add to query
    for match_key in match_args.keys():
        match_val = match_args[match_key]

        if match_val:
            s = s.query('match', **{match_key: match_val})
        
    # Execute query and get results
    response = s.execute()

    return response


def search_by_id(id):
    client = Elasticsearch("http://localhost:9200")
    results = Document().get(id=id, index='games', using=client)
    return results.to_dict()


def search_more_like_this(id, title='', genres='', summary='', rating=-1):
    client = Elasticsearch("http://localhost:9200")
    s = Search(using=client)
    fields = []

    if title:
        fields.append('title')

    if genres:
        fields.append('genres')

    if summary:
        fields.append('summary')

    if rating > 0:  
        fields.append('rating')

    like_doc = ' '.join([title, summary])
    if genres:
        like_doc += ' '.join(genres)

    fields = ['genres', 'title', 'summary']
    # query = {'more_like_this': {'fields': fields, 'like': {'_index': 'games', '_id': id}}}
    query = {'query': {'more_like_this': {'fields': fields, 'like': {'_index': 'games', '_id': id}}}}
    
    # response = client.search(index='games', body=query)
    response = requests.get('http://localhost:9200/games/_search', params=query, headers={'content-type':'application/json'})
    # response = client.search(index='games', query=query)
    # response = s.query(MoreLikeThis(fields=fields, like={'_index': 'games', '_id': id})).execute()
    # response = s.query(query).execute()

    return response

# hits = search_more_like_this(id='10')['hits']['hits']
# hits = search_more_like_this(id='10').hits
hits = search_more_like_this(id='10')
print('More like this:')
print(hits.text, hits.status_code)
# for hit in hits:
#     print(hit)