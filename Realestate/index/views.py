from django.shortcuts import render
from index.models import Locations

# Create your views here.

def index(request):
    # dest1=Destination()
    # dest1.name='guntur'
    # dest1.desc='very famous city'
    # dest1.img='/static/images/destination_1.jpg'
    # dest1.price=10000
    # dest2 = Destination()
    # dest2.name = 'chennai'
    # dest2.img = '/static/images/destination_2.jpg'
    # dest2.desc = 'very famous city'
    # dest2.price = 10000
    #
    # dest3 = Destination()
    # dest3.name = 'bang'
    # dest3.desc = 'very famous city'
    # dest3.price = 10000
    # dest3.img = '/static/images/destination_3.jpg'
    # dest4 = Destination()
    # dest4.name = 'goa'
    # dest4.desc = 'very famous city'
    # dest4.img = '/static/images/destination_4.jpg'
    # dest4.price = 10000
    # dest5 = Destination()
    # dest5.name = 'pedaparimi'
    # dest5.desc = 'Ravali city'
    # dest5.price = 1000000000
    # dest5.img = '/static/images/destination_5.jpg'
    # dests=[dest1,dest2,dest3,dest4,dest5]
    # return render(request,'index.html',{'dests':dests})

    dest=Locations.objects.all()
    return render(request,'index.html')
