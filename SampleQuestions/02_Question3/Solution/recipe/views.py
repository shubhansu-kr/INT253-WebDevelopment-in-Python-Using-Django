from django.shortcuts import render

recipes = [
    {
        'id': 1,
        'title': 'Spaghetti Carbonara',
        'description': 'A classic Italian pasta dish',
        'content': 'Ingredients: Spaghetti, eggs, pancetta, Parmesan cheese, black pepper.',
        'author': 'Chef Luigi',
        'steps': [
            'Boil the spaghetti.',
            'Cook the pancetta until crispy.',
            'Mix eggs and Parmesan cheese in a bowl.',
            'Combine spaghetti, pancetta, and egg mixture.',
            'Season with black pepper and serve.'
        ]
    },
    {
        'id': 2,
        'title': 'Chicken Curry',
        'description': 'A spicy and flavorful dish',
        'content': 'Ingredients: Chicken, curry powder, coconut milk, onions, garlic, ginger.',
        'author': 'Chef Ayesha',
        'steps': [
            'Sauté onions, garlic, and ginger.',
            'Add chicken and cook until browned.',
            'Stir in curry powder.',
            'Pour in coconut milk and simmer.',
            'Serve with rice.'
        ]
    },
    {
        'id': 3,
        'title': 'Chocolate Cake',
        'description': 'A rich and moist chocolate cake',
        'content': 'Ingredients: Flour, sugar, cocoa powder, baking powder, eggs, milk, butter.',
        'author': 'Chef Pierre',
        'steps': [
            'Preheat the oven to 350°F (175°C).',
            'Mix dry ingredients together.',
            'Add wet ingredients and mix until smooth.',
            'Pour batter into a greased baking pan.',
            'Bake for 30-35 minutes.',
            'Let cool before serving.'
        ]
    }
]

user = {
    'name': 'John Doe',
    'email': 'john.doe@example.com'
}

def index(request):
    return render(request, 'index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe:
        return render(request, 'recipe_detail.html', {'recipe': recipe})
    return render(request, '404.html', status=404)

def user_profile(request):
    return render(request, 'user_profile.html', {'user': user, 'recipes': recipes})
