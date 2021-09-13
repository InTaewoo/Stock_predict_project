from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def samsung(request):
    return render(request,'samsung.html')

def sk_hynicx(request):
    return render(request,'sk_hynicx.html')

def hyundai(request):
    return render(request,'hyundai.html')

def lg_chem(request):
    return render(request,'lg_chem.html')

def charts(request):
    return render(request,'charts.html')

