from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def recipe_list(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def recipeListTemplates(request, num=1):
    if num == 1:
        number = '1'
        ctx = {
            "recipes": [
                "Tomato - 3 pieces",
                "Onion - 1 piece",
                "Pork - 1 kilo",
                "Water - 1 liter",
                "Sinigang Mix - 1 packet",
            ]
        }
    elif num == 2:
        number = '2'
        ctx = {
            "recipes": [
                "garlic - 1 head",
                "onion - 1 piece",
                "vinegar - 1/2 cup",
                "water - 1 cup",
                "salt - 1 tablespoon",
                "whole black peppers - 1 tablespoon",
                "pork - 1 kilo",
            ]
        }
    else:
        number = 'ERROR'
    context = {"number": number, **ctx}
    return render(request, 'recipeListTemplate.html', context)
# Create your views here.
