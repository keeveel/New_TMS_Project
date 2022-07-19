from django.shortcuts import render


# Create your views here.
def index_page(request):
    print('Request is accepted')
    context = {
        "username": "Azamat"
    }
    return render(request, 'main/index.html', context)


def login_page(request):
    return render(request, 'main/login.html', {})
