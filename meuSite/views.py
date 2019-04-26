from django.shortcuts import render

# Create your views here.
def index(request): #Request = Requisição de alguma coisa
    return render(request, 'index.html')

    
def sobre(request):
    return render(request, 'sobre.html')