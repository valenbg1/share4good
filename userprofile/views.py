from django.shortcuts import render
from userprofile.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from userprofile.models import *
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RoleElectionForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            
            if role == 'user':
                return HttpResponseRedirect('/register_user')
            else:
                return HttpResponseRedirect('/register_org')
    else:
        form = RoleElectionForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
@csrf_protect
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = Usuario(
                nombre = form.cleaned_data['nombre'],
                apellidos = form.cleaned_data['apellidos'],
                telefono = form.cleaned_data['telefono'],
                web = form.cleaned_data['web'],
                descripcion = form.cleaned_data['descripcion'])
            user.save()
                
            user_User = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'])
                
            user_aux = UserProfile(
                user=user_User,
                is_usuario=user)
            user_aux.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = UserRegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
    
@csrf_protect
def register_org(request):
    if request.method == 'POST':
        form = OrganRegistrationForm(request.POST)
        if form.is_valid():
            org = Organizacion(
                nombre = form.cleaned_data['nombre'],
                telefono = form.cleaned_data['telefono'],
                web = form.cleaned_data['web'],
                descripcion = form.cleaned_data['descripcion'],
                direccionfis = form.cleaned_data['direccion_fis'])
            org.save()
                
            user_User = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'])
                
            user_aux = UserProfile(
                user=user_User,
                is_organiz=org)
            user_aux.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = OrganRegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
    
@login_required
def new_inversion(request):
    if request.method == 'POST':
        form = NewInversionForm(request.POST)
        if form.is_valid():
            presupuesto = form.cleaned_data['presupuesto']
            descripcion = form.cleaned_data['descripcion']
            
            userProf = UserProfile.objects.get(user=request.user)
            
            inv = Inversion(org = userProf.is_organiz, presupuesto = presupuesto, descripcion = descripcion)
            inv.save()
            
            return HttpResponseRedirect('/home')
    else:
        form = NewInversionForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
@login_required
def home(request):
    userProf = UserProfile.objects.get(user=request.user)
    
    if userProf.is_usuario is not None:
        return render_to_response(
        'home.html',
        { 'user': request.user }
        )
    else:
        try:
            orgInv = Inversion.objects.filter(org=(userProf.is_organiz_id))
        except Inversion.DoesNotExist:
            orgInv = None
    
        return render_to_response(
        'home-org.html',
        { 'user': request.user,
          'inversion_list': orgInv}
        )
