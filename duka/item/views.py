from django.shortcuts import render

from django.db.models import Q

from .models import Item, Category
# Create your views here.
def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
        
    if category_id:
        items = items.filter(category_id=category_id)
        
    return render(request, "item/items.html", {
        "items": items,
        "categories": categories,
        "category_id": int(category_id)
    })