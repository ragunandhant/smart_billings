from django.shortcuts import render
from food.models import Category, Item
from user.models import userProfile
def index(request):
    categories = Category.objects.all()
    category_items = {}
    for category in categories:
        items = Item.objects.filter(category=category)
        category_items[category.name] = items
    context={'categories': categories, 'category_items': category_items}
    if request.user.is_authenticated:
        user = userProfile.objects.get(user=request.user)
        context['user'] = user
        print(user.user.username,user.wallet_amount)
    return render(request, 'index.html', context)

