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
        results = search.random_search()

    context = {'results': results}
    return render(request, 'results.html', context)


# Used to pass a single result to the template
def result_detail(request, game_id):
    context = search.search_by_id(game_id)
    similar_games = search.search_more_like_this(game_id)
    context['similar'] = similar_games

    return render(request, 'result_details.html', context)

