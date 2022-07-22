from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_page(request):
    print('Request is accepted')
    context = {
        "username": "Azamat"
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html', {})

def login_page(request):
    return render(request, 'main/login.html', {})
