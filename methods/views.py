from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'blog/home.html', context)
