from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,profile

# Create your views here.
def index(request):
   posts = Image.objects.all()
   return render(request, 'all-temps/index.html',{'posts':posts})

