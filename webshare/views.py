from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    return render_to_response('layouts/index.html')

def about(request):
    return render_to_response('layouts/about.html')

def asociaciones(request):
    return render_to_response('layouts/asociaciones.html')

def investigadores(request):
    return render_to_response('layouts/investigadores.html')

def empresa(request):
    return render_to_response('layouts/empresa.html')

def ingenieros(request):
    return render_to_response('layouts/ingenieros.html')

def ong(request):
    return render_to_response('layouts/ong.html')

def cienmil(request):
    return render_to_response('layouts/cienmil.html')
