from django.shortcuts import render_to_response
from webshare.models import Usuario, Organizacion, Inversion

# Create your views here.
def index(request):
    return render_to_response('layouts/index.html')

def master(request):
    return render_to_response('layouts/master.html')
