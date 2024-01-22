from django.shortcuts import render


posts = [
    {
        'author': 'User1',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '22.01.2024'
    },
    {
        'author': 'User2',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '22.01.2024'
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)