from django.shortcuts import render
from django.http import HttpResponse

from .models import Pet

# Create your views here.
def home(request):
    #return HttpResponse("<p> home view </p")
    pets = Pet.objects.all()
    

def pet_detail(request,pet_id):
    return HttpResponse(f"<p> pet_detail viewwith {pet_id} </p>")
