from django.urls import path
from . import views

urlpatterns = [
    path('total-views', views.total_views, name="api-total-views"),
    path('datatable', views.datatable, name="api-datatable"),
    path('movies', views.movies, name="api-movies"),
    path('movies-with-ratings', views.movies_with_ratings, name="api-movies-with-ratings"),
    path('export', views.export, name="api-export"),
]

