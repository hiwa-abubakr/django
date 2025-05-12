from django.shortcuts import render

def home(request):
  context={}
  return render(request,"myapp/home.html",context)

def about(request):
    return render(request, "myapp/about.html")

def classes(request):
    return render(request, "myapp/classes.html")