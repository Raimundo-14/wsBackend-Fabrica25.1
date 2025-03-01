from django.shortcuts import render, redirect, get_object_or_404
from .models import Frase
import requests

def home(request):
    url = 'https://api.adviceslip.com/advice'
    advice = None
    advice_id = None

    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        advice_id = data['slip']['id']
        advice_text = data['slip']['advice']
        advice = f'ID: {advice_id} - Advice: {advice_text}'

    except requests.exceptions.RequestException as e:
        advice = f'Erro ao acessar a API: {e}'

    if request.method == 'POST':
        texto = request.POST.get('texto')  
        frase = Frase(texto=texto, advice_id=advice_id, advice_text=advice_text)
        frase.save()
        return redirect('home') 

    context = {
        'advice': advice,
        'frases': Frase.objects.all()  
    }

    return render(request, 'appfrase/home.html', context)

def listar_frases(request):
    frases = Frase.objects.all()
    context = {'frases': frases}
    return render(request, 'appfrase/listar.html', context)

def editar_frase(request, pk):
    frase = get_object_or_404(Frase, pk=pk)

    if request.method == 'POST':
        frase.texto = request.POST.get('texto')
        frase.save()
        return redirect('listar_frases')

    context = {
        'frase': frase
    }
    return render(request, 'appfrase/editar.html', context)

def deletar_frase(request, pk):
    frase = get_object_or_404(Frase, pk=pk)
    frase.delete()
    return redirect('listar_frases')

