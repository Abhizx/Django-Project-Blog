from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
import random

# Create your views here.

def home(request):
    b = len(Post.objects.all())
    # print(b)
    a = random.randint(3,b-1)
    # print(a)
    post = Post.objects.first()
    post2 = Post.objects.reverse()[1]
    post3 = Post.objects.reverse()[a]
    # print(post)
    context = {'post':post, 'post2':post2, 'post3':post3}
    return render(request, 'home/home.html', context)
    # return HttpResponse("Hello, Home here!")

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST['content']
        # print(name, email, phone, content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has beent sent')

    return render(request, 'home/contact.html')

def privacy(request):
    return render(request, 'home/privacypolicy.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please redefine query")

    params = {'allPosts':allPosts, 'query':query}
    return render(request, 'home/search.html', params)
    # return HttpResponse("This is search")