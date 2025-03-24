from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def articles_list(request):
    return render(request, 'articles/articles_list.html')