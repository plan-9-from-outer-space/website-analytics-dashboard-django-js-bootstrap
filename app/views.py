from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request, 'index.html')

def area_chart (request):
    return render (request, 'area_chart.html')

def bubble_chart (request):
    return render (request, 'bubble_chart.html')

def two_chart_types (request):
    return render (request, 'two_chart_types.html')

def datatables (request):
    return render (request, 'datatables.html')

