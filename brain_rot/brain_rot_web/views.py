import string
import random
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from utilities import search

# Renders the index page
def index(request):
    context = {}
    return render(request, 'index.html', context)


# Renders the survey page
def survey(request):
    # template = loader.get_template("brain_rot_web/index.html")
    context = {}
    return render(request, 'survey.html', context)


# Renders the results page according to query parameters
def results(request):
    # Check if query is from the submit or random button
    results = {}
    if request.GET["query"] == 'form':

        # Get summary and rating from the form
        summary = request.GET["desc"]
        rating = ('gte', float(request.GET["rating"]))
        genres = request.GET["genres"].split(' ')[:-1]
        platforms = request.GET["platforms"].split(' ')[:-1]

        # Execute search
        results = search.search(summary=summary, rating=rating, genres=genres, platforms=platforms)
    
    elif request.GET["query"] == 'random':

        # Genrate 5 random characters, do a search based on each char, 
        # and save the first result of each search into the results to be displayed
        # rand_str = random.choices(string.ascii_lowercase, k=5)
        rand_ids = [random.randint(0, 15000) for _ in range(5)]

        hits = []
        # for c in rand_str:
        #     hits.append(search.search(summary=c)[0])
        for i in rand_ids:
            hits.append(search.search_by_id(i))

        for hit in hits:
            results[hit['Title']] = hit['Title']
            results[hit['Rating']] = hit['Rating']
            results[hit['Plays']] = hit['Plays']
            results[hit['Release Date']] = hit['Release Date']
            results[hit['Summary']] = hit['Summary']
            results[hit['Id']] = hit['Id']

    # Create a dictionary of results to be passed to the template
    # (this is done because Django templates can't handle the ES response object)

    # for hit in hits:
    #     results[hit.title] = {'Title': hit.title,
    #                           'Rating': hit.rating,
    #                           'Plays': hit.plays,
    #                           'Release Date': hit.release_date,
    #                           'Summary': hit.summary,
    #                           'Id': hit.meta.id}

    context = {'results': results}
    return render(request, 'results.html', context)


# Used to pass a single result to the template
def result_detail(request, game_id):
    context = search.search_by_id(game_id)
    similar_games = search.search_more_like_this(game_id)
    context['similar'] = similar_games

    return render(request, 'result_details.html', context)

