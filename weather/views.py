# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.shortcuts import render
from .models import City

# Create your views here.

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=450ccb44bf951d091d75ae77946a0c26'
	
	cities = City.objects.all()
	cities_weather = []
	
	for city in cities:
		res = requests.get(url.format(city)).json()
		city_weather = {
			"city":city,
			"temp":res['main']['temp'] - 273,
			"desc":res['weather'][0]['description'],
			"icon":res['weather'][0]['icon']
		}
		cities_weather.append(city_weather)

	print(cities_weather);
	
	
	context = {'cities_weather': cities_weather}
	return render(request, 'weather.html', context)
