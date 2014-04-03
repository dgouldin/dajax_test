from django.shortcuts import render

import json
from dajaxice.decorators import dajaxice_register

def index(request):
    return render(request, 'index.html')

@dajaxice_register
def sayhello(request):
    return json.dumps({'message':'Hello World'})
