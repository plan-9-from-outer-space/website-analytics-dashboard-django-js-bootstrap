
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app-index'),
    path('area-chart', views.area_chart, name='app-area-chart'),
    path('bubble-chart', views.bubble_chart, name='app-bubble-chart'),
    path('two-chart-types', views.two_chart_types, name='app-two-chart-types'),
    path('datatables', views.datatables, name='app-datatables'),
]

