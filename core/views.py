from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ConsultaForm
from .models import Profile, Consulta

# Create your views here.
@login_required
def pagina_inicial(request):
    redirect('accounts/login')

@login_required
def inicio(request):
    profile = get_object_or_404(Profile, usuario=request.user)
    if profile.is_paciente():
        consultas = Consulta.objects.filter(paciente=profile)
    else:
        consultas = Consulta.objects.filter(medico=profile)

    return render(request, 'inicio.html', locals())

@login_required
def cadastrar_consulta(request):
    profile = get_object_or_404(Profile, usuario=request.user)
    title = 'Cadastrar Nova Consulta'
    form = ConsultaForm(request.POST or None, profile=profile)
    if form.is_valid():
        resultado = form.save()
        print(resultado)
        return redirect('/inicio')
    return render(request, 'form_base.html', locals())

@login_required
def consultas_agendadas(request):
    profile = get_object_or_404(Profile, usuario=request.user)
    title = 'Cadastrar Nova Consulta'
    form = ConsultaForm()
    return render(request, 'form_base.html', locals())