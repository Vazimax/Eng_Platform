from django.shortcuts import render

def home(request):


    return render(request,'home.html')

def room(request, pk):


    return render(request,'room.html')
