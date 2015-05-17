from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#def index(request):
#	return HttpResponse("Hello NYC!")

def index(request):
    from oauth_secret import *
    import urllib2
    import json
    json_string = urllib2.urlopen('https://api.instagram.com/v1/users/self/feed?access_token=' + secret + '&count=500').read()
    data2 = json.loads(json_string)
    data_dict = {}
    data_dict['data'] = data2['data']
    return render(request, 'nycitytasteapp/index.html', data_dict)

