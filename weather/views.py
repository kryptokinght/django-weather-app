# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.shortcuts import render

# Create your views here.

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=450ccb44bf951d091d75ae77946a0c26'
	city = 'Kolkata'
	res = requests.get(url.format(city)).json()
	city_weather = {
		"city":city,
		"temp":res['main']['temp'] - 273,
		"desc":res['weather'][0]['description'],
		"icon":res['weather'][0]['icon']
	}
	context = {'city_weather': city_weather}
	print (city_weather)
	return render(request, 'weather.html', context)
