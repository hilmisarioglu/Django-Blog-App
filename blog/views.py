from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'blog/home.html') 

def login(request):
    return render(request,'blog/login.html') 

def post_detail(request):
    return render(request,'blog/post_detail.html') 

def post(request):
    return render(request,'blog/post.html') 

def register(request):
    return render(request,'blog/register.html') 