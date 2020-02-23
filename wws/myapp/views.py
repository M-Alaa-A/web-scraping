from django.shortcuts import render
from bs4 import BeautifulSoup

def home(request):
    return render(request, 'base.htm')
def newsearch(request):
    search = request.POST.get('searchofinput')
    stuff_for_frontend = {
        'search':search,
        } 
    return render(request, 'myapp/newsearch.htm', stuff_for_frontend)  #you must put 'search' first before search