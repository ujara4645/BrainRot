import json
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render 
from utilities import search

def index(request):
    # template = loader.get_template("brain_rot_web/index.html")
    context = {}
    return render(request, 'index.html', context)

def survey(request):
    # template = loader.get_template("brain_rot_web/index.html")
    context = {}
    return render(request, 'survey.html', context)

def results(request):
    
    # template = loader.get_template("brain_rot_web/results.html")
    summary = request.GET["desc"]
    rating = ('gte', float(request.GET["rating"]))
    hits = search.search(summary=summary, rating=rating).hits
    results = {}
    
    for hit in hits:
        results[hit.title] = {'Title': hit.title,
                               'Rating': hit.rating, 
                               'Plays': hit.plays, 
                               'Release Date': hit.release_date,
                               'Summary': hit.summary}
        
    context = {'results': results}
        
    return render(request, 'results.html', context)
    
