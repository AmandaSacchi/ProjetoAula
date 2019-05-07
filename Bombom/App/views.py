from django.shortcuts import render
from App.models import Crush
# Create your views here.
def index(request):
    crush = Crush.objects.all() #VAI RETORNAR TODOS OS NOSSO CRUSHES
    contexto = {
        'crush' : crush
        }
    return render(request, 'index.html', contexto)
