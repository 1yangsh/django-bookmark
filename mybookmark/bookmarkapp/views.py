from django.shortcuts import render

from django.views.generic import ListView, DetailView
from bookmarkapp.models import Bookmark


class BookmarkLV(ListView):
    # url + "_list.html"
    model = Bookmark


class BookmarkDV(DetailView):
    # url + "_detail.html"
    model = Bookmark
