from django.shortcuts import get_object_or_404,render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


def index(request):
	return render(request, 'mysite/index.html') 
