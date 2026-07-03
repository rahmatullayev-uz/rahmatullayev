from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "pages/home.html")


def projects(request):
    datas = [
        {
            'title': "AmmoCRM",
            'subtitle': "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo omnis, nam inventore cupiditate distinctio vero fuga veniam repudiandae voluptatem libero id quisquam adipisci nihil velit eos! Odit ipsam ea maiores!",
            'demo': "https://t.me/telegram",
            'github': "https://github.com/rahmatullayev_dev",
            'image': None
        },
        {
            'title': "Kino Bot",
            'subtitle': "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo omnis, nam inventore cupiditate distinctio vero fuga veniam repudiandae voluptatem libero id quisquam adipisci nihil velit eos! Odit ipsam ea maiores!",
            'demo': "https://t.me/telegram",
            'github': "https://github.com/rahmatullayev_dev",
            'image': None
        },
        {
            'title': "OLX Clone",
            'subtitle': "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nemo omnis, nam inventore cupiditate distinctio vero fuga veniam repudiandae voluptatem libero id quisquam adipisci nihil velit eos! Odit ipsam ea maiores!",
            'demo': "https://t.me/telegram",
            'github': "https://github.com/rahmatullayev_dev",
            'image': None
        },
    ]
    context = {
        'project_list': datas
    }
    return render(request, "pages/projects.html", context)


def blog(request):
    return render(request, "pages/blog.html")


def contact(request):
    return render(request, "pages/contact.html")