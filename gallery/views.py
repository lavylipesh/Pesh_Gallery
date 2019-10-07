from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})