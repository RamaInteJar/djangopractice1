from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me': "No I am live from first_app!"}    
    return render(request, 'first_app/index.html', context=my_dict)

# Create your views here.
