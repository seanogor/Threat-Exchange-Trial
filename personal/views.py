from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,"personal/home.html")


def index1(request):
	return HttpResponse("<h2>HEY!!!</h2>")



def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html',{'content':['If you would like to contact me, please email me.','seanogor@gmail.com']})


