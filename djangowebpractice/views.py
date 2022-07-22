from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def home(request):

    # doc_home=open("C:/Users/giova/Documents/GitHub/djangowebpractice/djangowebpractice/templates/home.html")

    # plt= Template(doc_home.read())

    # doc_home.close()

    # doc_home = loader.get_template('home.html')

    # ctx = Context()

    # doc_file = doc_home.render()

    return render(request, "home.html")

def cursoDjango(request):

    return render(request, "pages/courses.html")