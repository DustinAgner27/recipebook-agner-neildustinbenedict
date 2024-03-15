from django.contrib import admin
from .models import Recipe, RecipeIngredient, Profile, Ingredient
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class RecipeInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeInline,]

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    inlines = [RecipeInline,]

admin.site.register(Recipe, RecipeAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredient, IngredientAdmin)