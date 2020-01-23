from django.shortcuts import render
from .services import select_all_stuff, select_stuff_by_id


def index(request):
    context = {'stuff':select_all_stuff()}
    return render(request, 'classdb/index.html', context)

def index1(request, id):
    context = {'stuff':select_stuff_by_id(id)}
    return render(request, 'classdb/index1.html', context)
    
# Create your views here.
