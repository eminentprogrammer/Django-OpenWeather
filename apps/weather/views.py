from django.shortcuts import render
from ..utils.get_weather import search_city
from django.http import JsonResponse



def homepage(request):
    site = "homepage"
    city = request.GET.get("city")
    print(city)
    if city is not None:
        response = search_city(city)
    return render(request, 'homepage.html', locals())