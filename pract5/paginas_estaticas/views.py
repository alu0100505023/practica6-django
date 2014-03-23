#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django import template

def home(request):
	#tmp1=template.loader.get_template("template.html")
	#context=template.Context({"texto": as})
	#return HttpResponse(tmp1.render(context))
	return HttpResponse("<h1>Home</h1>")

def help(request):
	return HttpResponse("<h1>Help</h1>")

def about(request):
	return HttpResponse("<h1>About</h1>")
