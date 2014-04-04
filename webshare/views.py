from django.shortcuts import render_to_response
from webshare.models import Usuario, Organizacion, Inversion

# Create your views here.
def home(request):
    return render_to_response('home/index.html')
