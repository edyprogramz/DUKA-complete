from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from item.models import Item
# Create your views here.
@login_required
def index(request):
    items = Item.objects.filter(is_sold=False, created_by=request.user)
    
    return render(request, "dashboard/index.html", {
        "items": items
    })