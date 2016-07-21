from django.http import HttpResponse
import datetime
import json
import pokelocator_api
from django.template.response import TemplateResponse
import os

import time
import random

def json_custom_parser(obj):
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)


def get_fake_pokemon_result(location):
    loc_parts = location.split(',')
    lat = float(loc_parts[0].strip()) + (random.random() * 0.002) - 0.001
    lon = float(loc_parts[1].strip()) + (random.random() * 0.002) - 0.001
    i = random.randint(1,151)
    return [{"id":i,"name":"foo","latitude":lat,"longitude":lon,"time_left":100,"distance":10,"direction":"N"}]

def get_poke(request):

    location = request.POST.get('location', "911 Washington Ave, Saint Louis, MO")
    direction = request.POST.get('direction', False)
    result = pokelocator_api.main(location=location, direction=direction)
    #result = get_fake_pokemon_result(location)
    
    return HttpResponse(json.dumps({
        "status": "success",
        "data": result,
        "location": location
    }, default=json_custom_parser), content_type='application/json', status=200)
    
    
def load_frontend(request):
    return TemplateResponse(request, 'index.html', context={
        "GMAPS_API_KEY": os.environ.get('GMAPS_API_KEY', "Invalid")
    })

