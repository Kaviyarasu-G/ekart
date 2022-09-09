from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views import generic

from .models import UserProfile


class MyView(generic.ListView):
    model = UserProfile
    context_object_name = 'my_favorite_publishers'

    # def get_object(self, queryset=None):
    #     # <view logic>
    #     return HttpResponse('result')