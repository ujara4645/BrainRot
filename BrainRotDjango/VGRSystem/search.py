from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import numbers

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
    
    term_args = {'developers': (developers), 
                 'genres': genres,
                 'platforms': platforms}

    # Loop over comparison arguments, check if it's valid, if it's a date or int, and add to query
    for comp_key in comparison_args.keys():
        comp_val = comparison_args[comp_key]
        if comp_val[0]:
            if isinstance(comp_val[1], numbers.Number) and comp_val[1] > 0:
                s = s.query('range', **{comp_key:{comp_val[0]: comp_val[1]}})
            else:
                s = s.query('range', **{comp_key:{comp_val[0]: comp_val[1]}})

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
    for hit in s.scan():
        print(hit.genres, hit.rating, hit.plays, hit.release_date)

    return response

search(genres=['Adventure'], rating=('gte', 3.5), plays=('lt', 10000), release_date=('gte', '2020-01-01'))


