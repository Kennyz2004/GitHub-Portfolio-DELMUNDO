from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
  posts = Post.objects.all()
  return render(request,'portfolio/index.html', {'posts':posts})