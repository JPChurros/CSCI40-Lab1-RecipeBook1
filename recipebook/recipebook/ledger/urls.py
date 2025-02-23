from django.urls import path
from .views import recipe_list, recipeListTemplates

urlpatterns = {
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:num>/', recipeListTemplates, name='recipeListTemplates'), 
}

app_name = "ledger"