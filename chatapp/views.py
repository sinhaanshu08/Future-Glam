from django.shortcuts import render
import os

def Chathome(request):
    return render(request, 'chathome.html')
