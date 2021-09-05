from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    view_count = request.session.get('view-count', 0) + 1
    request.session['view-count'] = view_count
    if view_count > 4:
        del(request.session['view-count'])
    response = HttpResponse("view count=" + str(view_count))
    response.set_cookie('dj4e_cookie', '44ae4524', max_age=1000)
    return response
