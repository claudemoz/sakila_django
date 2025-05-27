from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Country, City, Film, Actor
from datetime import datetime
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

def country_list(request):
    countries = Country.objects.all()
    h = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'country_list.html', {'countries': countries, 'hours': h})

def cities_by_country(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    cities = City.objects.filter(country=country)
    return render(request, 'cities_by_country.html', {'country': country, 'cities': cities})

def film_list(request):
    query = request.GET.get('q', '')
    if query:
        films = Film.objects.filter(
            Q(title__icontains=query) | 
            Q(actors__first_name__icontains=query) | 
            Q(actors__last_name__icontains=query)
        ).distinct()
    else:
        films = Film.objects.all()
    return render(request, 'film_list.html', {'films': films, 'query': query})

def film_detail(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    context = {
        'film': film,
    }
    return render(request, 'film_detail.html', context)

def actor_list(request):
    query = request.GET.get('q')
    if query:
        actors = Actor.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    else:
        actors = Actor.objects.all()
    return render(request, 'actor_list.html', {'actors': actors, 'query': query})



