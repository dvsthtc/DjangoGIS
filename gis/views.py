from django.shortcuts import render
from django.http import HttpResponse
from gis.models import Articles

# Create your views here.
def home(request):
    #return HttpResponse("Hello world")
    #return render(request, 'gis/base.html')
    articles = Articles.object.all()
    contex = {
        'articles': articles
    }
    return render(request, 'gis/base.html', context)

def about(request):
    return render(request, 'gis/about.html')