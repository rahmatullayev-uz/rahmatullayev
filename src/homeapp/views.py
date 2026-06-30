from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pages/home.html")


def projects(request):
    return render(request, "pages/projects.html")


def blog(request):
    return render(request, "pages/blog.html")


def contact(request):
    return render(request, "pages/contact.html")