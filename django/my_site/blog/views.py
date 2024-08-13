from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request,"index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "all-posts.html",{
    "all_posts": all_posts
    })

def post_datail(request, slug):
    indentified_post= get_object_or_404(Post, slug=slug)
    return render(request, "post-detail.html" ,{
        "post": indentified_post,
        "post_tags": indentified_post.tags.all()
    })
