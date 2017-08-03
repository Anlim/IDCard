# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from upload.models import IMG

from imageProcessing import frontPicture,backPicture

def index(request):
    return render(request, 'index.html')


def uploadFrontImg(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
        path = "material/"+img.name
        return HttpResponse(frontPicture(path))
    return render(request, 'uploadimg.html')

def uploadbackImg(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
        path = "material/"+img.name
        data = backPicture(path)
        return HttpResponse(data)
    return render(request, 'uploadimg.html')


