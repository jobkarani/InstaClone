from django.shortcuts import render,get_object_or_404
from django.http  import HttpResponse
from .models import Image,Profile, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

# Create your views here.
def index(request):
    posts = Image.objects.all()
    form = CommentForm()
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            commentt = form.save(commit=False)
            commentt.user = request.POST.user
            commentt.save()
            return redirect('index')
            
    return render(request, 'all-temps/index.html',{"posts":posts, "form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    posts = Image.objects.filter(user=current_user)
    profile = Profile.objects.filter(user_id=current_user.id)
    return render(request, 'all-temps/profile.html', {"posts": posts, "profile": profile})
  
@login_required
def comments(request,image_id):
  form = CommentForm()
  image = Image.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.user = request.user
      comment.image = image
      comment.save() 
  return redirect('index') 
 
  
def search_results(request):

    if 'posts' in request.GET and request.GET["posts"]:
        search_term = request.GET.get("posts")
        searched_posts = Image.search_by_name(search_term)
        message = search_term

        return render(request, 'all-temps/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-temps/search.html',{"message":message})

