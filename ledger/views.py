from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required

def recipe_list(request):
    context = { 'recipe_list': Recipe.objects.all() }
    return render(request, 'recipe_list.html', context)

@login_required
def recipe_page(request, pk):
    context = { 'recipe' : Recipe.objects.get(pk=pk) }
    return render(request, 'recipe_page.html', context)