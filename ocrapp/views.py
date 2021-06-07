import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from easyocr.detection import test_net
from numpy.core.getlimits import MachArLike
from .form import ImageForm
from .models import Image
import os
# Create your views here.

import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

from googletrans import Translator

trans = Translator()

# v = "media/images/surf.jpeg"
# image_path = os.path.join(path, '', v)
# image_path = r'C:/Users/Mahim/Desktop/minor/ocr front/projects/ocr/media/images/surf.jpeg'
# print("mahim")
# print(image_path)
# reader = easyocr.Reader(['en'], gpu=True)
# result = reader.readtext(image_path)
# print(result)
# abc = result
# xyz = ''
# for i in range(0, len(result)):
#     xyz = xyz + result[i][1] + ' '


def home(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            # obj prints caption
            # code for ocr
            path = r'C:/Users/Mahim/Desktop/minor/ocr front/projects/ocr'
            rel_path = obj.image.url
            print("mahim")
            print(obj.language)
            # v = "/media/images/surf.jpeg"
            image_path = os.path.join(path, '', rel_path[1:])
            print("mahim")
            print(obj.translate)
            reader = easyocr.Reader([obj.language], gpu=True)
            result = reader.readtext(image_path)
            print(result)
            abc = result
            xyz = ''
            for i in range(0, len(result)):
                xyz = xyz + result[i][1] + ' '
            print(xyz)
            transRes = trans.translate(xyz, dest=obj.translate).text
            print(transRes)
            return render(request, "home.html", {"obj": obj, "result": xyz, "transRes": transRes})
    else:
        form = ImageForm()
    img = Image.objects.all()
    # print(img)
    # print(obj.image.url)
    # image_path = 'C:\media\images\surf_5fcSUSw.jpeg'
    # reader = easyocr.Reader(['en'], gpu=True)
    # result = reader.readtext(image_path)
    # print(result)
    # abc = result
    # xyz = ''
    # for i in range(0, len(result)):
    #     xyz = xyz + result[i][1] + ' '
    return render(request, 'home.html', {"img": img, "form": form})


def aboutocr(request):
    return render(request, 'aboutocr.html')
