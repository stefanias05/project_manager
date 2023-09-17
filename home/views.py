

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    html_template = loader.get_template('home/index.html')
    context = {
    }
    return HttpResponse(html_template.render(context, request))