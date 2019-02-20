from django.shortcuts import render_to_response,render
from py2neo import *

def home(request): 
    context={}
    context['course_list']=[]
    graph = Graph("http://localhost:7474", username="zzq", password='zam123456')
    data = graph.run('match (c:Course) return c')
    for item in data:
        context['course_list'].append(item['c']['name'])
    return render_to_response('app/index.html',context)