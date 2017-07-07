from django.shortcuts import render

# Create your views here.

def home(request):
    """Homepage."""
    page = {
        'title': 'Home'
    }

    context = {
        'page': page,
        'title': 'Akim',
    }
    return render(request, 'main/home.html', context)
