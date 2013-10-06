from django.core import urlresolvers
from django.shortcuts import render
from django.http import HttpResponse

def root(request):
    r = '''
    <a href="''' + urlresolvers.reverse('admin:index') + '''">admin</a><br>
    <a href="''' + urlresolvers.reverse('lameform.views.graph') + '''">graph</a><br>
    '''
    return HttpResponse(r)


def graph(request):
    return render(request, 'lameform/graph.html')
