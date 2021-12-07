from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,profile

# Create your views here.
def index(request):
   posts = Image.objects.all()
   return render(request, 'all-temps/index.html',{'posts':posts})

def search_results(request):

    if 'posts' in request.GET and request.GET["posts"]:
        search_term = request.GET.get("posts")
        searched_posts = Image.search_by_name(search_term)
        message = search_term

        return render(request, 'all-temps/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-temps/search.html',{"message":message})

