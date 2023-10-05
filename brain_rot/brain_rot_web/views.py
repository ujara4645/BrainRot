from django.template import loader
from django.http import HttpResponse
from utilities import search

def index(request):
    template = loader.get_template("brain_rot_web/index.html")
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def results(request):
    
    title = request.GET["title"]
    hits = search.search(title = title).hits
    response = ""
    
    for hit in hits:
        response += (hit.title + "\n")
    
    return HttpResponse(response)
    
