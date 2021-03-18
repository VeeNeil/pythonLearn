from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request,'hello/index.html')
def about(request):
    return render (request,'hello/profile/about.html' )
def article(request):
    return render (request, 'hello/article.html')