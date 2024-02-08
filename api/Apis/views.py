from django.shortcuts import render

def home(request):

    contenido = {'titulo':'welcome'}
    template = 'home.html'
    return render(template,contenido)