from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image

def index(request):
    images = Image.objects.all()
    

    return render(request,'index.html',{'images':images})



def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_photos/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_photos/search.html',{"message":message})

def category(request,category_id):
    try:
        category = Category.objects.get(id = category_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/category.html", {"category":category})

