#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import posts
import datetime


"""def home(request):
    return HttpResponse("hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
"""

def home(request):
	Mfp='hi'
	G='sup'
	date='18th September 2011'
	body='dc'
	return render(request,'index.html',{
        'title' : Mfp,
        'author' : G,
        'date' : date,
        'body' : body,
    	})
