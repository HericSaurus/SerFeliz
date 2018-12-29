from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts' : posts}
    return render(request, 'blogapp/post_list.html',stuff_for_frontend)