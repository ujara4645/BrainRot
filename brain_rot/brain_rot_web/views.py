import json
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render 
from utilities import search

def index(request):
    template = loader.get_template("brain_rot_web/index.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def results(request):
    
    template = loader.get_template("brain_rot_web/results.html")
    title = request.GET["title"]
    hits = search.search(title = title).hits
    results = {}
    
    for hit in hits:
        results[hit.title] = {'Title': hit.title,
                               'Rating': hit.rating, 
                               'Plays': hit.plays, 
                               'Release Date': hit.release_date}
        
    context = {'results': results}
        
    return render(request, 'brain_rot_web/results.html', context)
    
