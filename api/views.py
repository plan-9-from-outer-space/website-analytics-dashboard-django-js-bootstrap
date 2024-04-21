from django.shortcuts import render
from django.http import JsonResponse
from random import randint
from api.models import TotalViewsModel

# Create your views here.

# labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"];
# data = [65, 59, 80, 81, 56, 55, 40];

def total_views (request):
    query_set = TotalViewsModel.objects.all()
    query_data = { "labels": [], "data": [] }
    for item in query_set:
        query_data["labels"].append(item.label)
        query_data["data"].append(item.views)
    # print(query_data)
    return JsonResponse(query_data)

def datatable (request):
    return JsonResponse({
        "data": [
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Python Basic Tutorial", "16-11-2023", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
        ]
    })

