from django.urls import path
from .views import recipe_list, recipe_page

urlpatterns = [
    path('recipes/list', recipe_list, name='list'),
    path('recipe/<int:pk>', recipe_page, name='recipe'),
]

app_name = 'recipe_book'