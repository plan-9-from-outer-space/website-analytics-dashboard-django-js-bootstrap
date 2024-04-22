from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from random import randint
from api.models import TotalViewsModel, MostWatchedVideos
from app.models import Movies, Ratings, Stars
import csv

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
    query_set = MostWatchedVideos.objects.all()  # not yet used
    return JsonResponse({
        "data": [
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Python Basic Tutorial", "16-11-2023", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
            ["Django Basic Tutorial", "16-11-2022", "72935"],
        ]
    })

def movies (request):
    movies = Movies.objects.all()[:50]
    # data = { "labels": [], "data": [] }
    data = []
    for item in movies:
        data.append([str(item.id), item.title, str(item.year)])
    # print(data)
    return JsonResponse({ "data": data })

# movie = models.ForeignKey(Movies, models.DO_NOTHING)
# rating = models.FloatField()
# votes = models.IntegerField()

def movies_with_ratings (request):
    query_set = (Ratings.objects.all().values(
        "rating", "votes", "movie_id", "movie__title", "movie__year")
        # Add filters (all filters must occur before slicing)
        # See "https://docs.djangoproject.com/en/5.0/ref/models/querysets/"
        .filter(movie__year__gt=2000)
        # query_set = query_set.order_by('movie__year')
        [:100]
    )
    # print(query_set)
    data = []
    for item in query_set:
        data.append([
            # Syntax for foreign key selects
            str(item['movie_id']), item['movie__title'], str(item['movie__year']),
            str(item['rating']), str(item['votes'])
        ])
    return JsonResponse({ "data": data })

def export (request):   # to a csv file
    response = HttpResponse(
        content_type = 'text/csv',
        headers = {'Content-Disposition': 'attachment; filename="movies_export.csv"'}
    )
    query_set = (Ratings.objects.all().values(
        "rating", "votes", "movie_id", "movie__title", "movie__year")
        .filter(movie__year__gt=2000)
        [:100]
    )
    # Save the data to a CSV file
    writer = csv.writer(response)
    for item in query_set:
        writer.writerow([
            str(item['movie_id']), item['movie__title'], str(item['movie__year']),
            str(item['rating']), str(item['votes'])
        ])
    # Return the response (should probably return true or False)
    return response

