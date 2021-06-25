from django.shortcuts import render
from django.conf import settings
import requests
import json

def home(request):

	key = settings.AIRQUALITY_API_KEY

	url = "http://api.airvisual.com/v2/city?city=Los Angeles&state=California&country=USA&key=" + key

	payload={}
	headers = {}

	response = requests.request("GET", url, headers=headers, data=payload)
	aqi_data = json.loads(response.text)

	context = {
		'title': 'Home',
		'aqi_index': aqi_data['status']
	}
	return render(request, 'lookout_app/home.html', context)
