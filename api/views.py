from django.http import HttpResponse
import datetime
import json
import pokelocator_api
import fake_pokelocator
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

def get_poke(request):

    location = request.POST.get('location', "911 Washington Ave, Saint Louis, MO")
    direction = request.POST.get('direction', False)
    print location
    result = pokelocator_api.main(location=location, direction=direction)
#    result = fake_pokelocator.get_fake_pokemon_result(location, 5)
    
    return HttpResponse(json.dumps({
        "status": "success",
        "data": result,
        "location": location
    }, default=json_custom_parser), content_type='application/json', status=200)
    
    
def load_frontend(request):
    return TemplateResponse(request, 'index.html', context={
        "GMAPS_API_KEY": os.environ.get('GMAPS_API_KEY', "Invalid")
    })

