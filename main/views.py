from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def problem(request):
    pass

def login(reqeust):
    if reqeust.method == 'GET':
        return render(reqeust, 'login.html')
    elif reqeust.method == 'POST':
        return HttpResponse(123)

def register(reqeust):
    pass