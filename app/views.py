from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course

@login_required
def index(request):
    return render(request, 'app/index.html')

@login_required
def start(request):
    return render(request, 'app/start.html')

@login_required
def graph(request):
    return render(request, 'app/graph.html')

@login_required
def others(request):
    return render(request, 'app/others.html')

@login_required
def search(request):
    return render(request, 'app/search.html')

@login_required
def all_courses(request):
    courses=Course.objects.all()
    return render(request, 'app/all_courses.html',{'courses':courses})

