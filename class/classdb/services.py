from .models import Stuff

def select_all_stuff():
    stuff = Stuff.objects.all()
    return stuff


def select_stuff_by_id(id):
    stuff = Stuff.objects.filter(id=id).first()
    return stuff