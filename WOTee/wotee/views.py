# -*- coding: utf-8 -*-
# $File: views.py
# $Date: Apr 12, 20:30, 2015.

import os
import hashlib
import base64

import cv2
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import UploadedFile
from django.conf import settings

from .models import Face
# from aotee.quick import generate


# Create your views here.

def index(request):
    context = {'temp': ""}
    return render(request, 'wotee/index.html', context)

def result(request):
    # check communication method
    if request.method == 'POST':
        # check uploaded image
        try:
            imageUpload = request.FILES['image']
        except:
            raise Http404("No image file!")

        # image properties
        imageName, imageExtension = os.path.splitext(os.path.basename(imageUpload.name))
        chunk = imageUpload.read(UploadedFile.DEFAULT_CHUNK_SIZE)
        imageMD5 = hashlib.md5(chunk).hexdigest()
        imagePath = 'upload'

        # try to store in database
        try:
            face = Face(md5=imageMD5, name=imageName, extension=imageExtension, path=imagePath)
            face.save()
            # move file to upload folder
            default_storage.save(face.location(), imageUpload)
        except:
            face = Face.objects.get(md5=imageMD5)

        # generate cartoon face
        # cartoon = generate(settings.MEDIA_ROOT + face.location())
        # cartoonBase64 = base64.encodestring(cv2.imencode('.png', cartoon)[1])
        f = open('/home/tobin/Documents/WOTee/media/result.b64')
        cartoonBase64 = f.read()
        f.close()
        cartoonCode = "data:image/png;base64," + cartoonBase64

        context = {'origin': settings.MEDIA_URL + face.location(), 'result': cartoonCode}
        # return result
        return render(request, 'wotee/result.html', context)
    else:
        return HttpResponse("Hello World!")