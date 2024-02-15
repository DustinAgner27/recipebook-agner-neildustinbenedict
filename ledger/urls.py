from django.urls import path
from .views import recipe_list, recipe_page1, recipe_page2

urlpatterns = [
    path('recipes/list', recipe_list, name='list'),
    path('recipe/1', recipe_page1, name='recipe1'),
    path('recipe/2', recipe_page2, name='recipe2')
]

app_name = 'recipe_book'