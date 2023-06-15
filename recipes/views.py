# recipes/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.models import User
# recipes/views.py


from django.shortcuts import render, get_object_or_404
from .models import Recipe
from django.core.paginator import Paginator

from .models import Recipe, ChatMessage
# recipes/views.py

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    youtube_link = None
    ingredients_list = recipe.ingredients.split('\n')
    description_steps = recipe.description.split('\n')
    if recipe.youtube_links:
        video_id = recipe.youtube_links.split('=')[-1]
        youtube_link = f"https://www.youtube.com/embed/{video_id}"
    if recipe.youtube_links=='https://www.youtube.com/':
        youtube_link=False

    context = {
        'recipe': recipe,
        'user': request.user,
        'youtube_link': youtube_link,
        'ingredients_list': ingredients_list,
        'description_steps': description_steps,
    }
    print(recipe.ingredients.split("\r"))
    return render(request, 'recipes/recipe_details.html', context)

@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.likes += 1
    recipe.save()

    response_data = {
        'liked': True,
        'likes_count': recipe.likes
    }
    return JsonResponse(response_data)

@login_required
def send_chat_message(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        message_body = request.POST.get('message')
        if message_body:
            ChatMessage.objects.create(sender=request.user, recipe=recipe, body=message_body)
    return HttpResponseRedirect(reverse('recipes:recipe_detail', args=[recipe.pk]))


@login_required
def recipe_list(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(recipe_name__icontains=query)

    paginator = Paginator(recipes, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'recipes': page_obj
    }
    return render(request, 'recipes/recipe_list.html', context)
@login_required
def user_recipes(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.filter(user=request.user)

    if query:
        recipes = recipes.filter(recipe_name__icontains=query)

    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/user_recipes.html', context)
@login_required
def user_recipe_list(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.all()  # Filter recipes by the current user

    if query:
        recipes = recipes.filter(recipe_name__icontains=query)

    paginator = Paginator(recipes, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'recipes': page_obj
    }
    return render(request, 'recipes/user_recipe_list.html', context)

@login_required
# recipes/views.py
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipes:user_recipe_list')  # Redirect to a success page or recipe list
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/create_recipe.html', {'form': form})
@login_required
def chat_with_user(request, user_id):
    # Retrieve the user based on the user_id
    user = get_object_or_404(User, pk=user_id)

    # Perform any necessary chat-related actions

    return render(request, 'recipes/chat.html', {'user': user})
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_list')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'recipes/contact.html', {'form': form})


def home(request):
    return render(request, 'recipes/home.html')
