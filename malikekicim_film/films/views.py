# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *


def index(request):

    return render(request, "index.html")

def publisher(request):
    all_publishers = Publisher.objects.all()

    template = loader.get_template("index.html")
    context = {"publishers": all_publishers}
    return render(request, "publisher.html", context)

def director(request):
    all_director = Director.objects.all()

    template = loader.get_template("index.html")
    context = {"directors":all_director}
    return render(request, "director.html", context)

def film(request):
    all_film = Film.objects.all()

    template = loader.get_template("index.html")
    context = {"films":all_film}
    return render(request, "film.html", context)


def favorite1(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    try:
        selected_film = publisher.film_set.get(pk=request.POST['film'])
    except(KeyError, Film.DoesNotExist):
        return render(request, "publisher.html", {"publisher":publisher})
    else:
        if selected_film.is_favorite:
            selected_film.is_favorite = False
        else:
            selected_film.is_favorite = True
        selected_film.save()
        return render(request, "publisher.html", {"publisher":publisher})


def favorite2(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    try:
        selected_film = publisher.film_set.get(pk=request.POST['film'])
    except(KeyError, Film.DoesNotExist):
        return render(request, "publisher.html", {"publisher":publisher})
    else:
        if selected_film.is_favorite:
            selected_film.is_favorite = False
        else:
            selected_film.is_favorite = True
        selected_film.save()
        return render(request, "publisher.html", {"publisher":publisher})

def favorite3(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    try:
        selected_film = publisher.film_set.get(pk=request.POST['film'])
    except(KeyError, Film.DoesNotExist):
        return render(request, "publisher.html", {"publisher":publisher})
    else:
        if selected_film.is_favorite:
            selected_film.is_favorite = False
        else:
            selected_film.is_favorite = True
        selected_film.save()
        return render(request, "publisher.html", {"publisher":publisher})
