from django.shortcuts import render, get_object_or_404
from forms import *
from models import *
from mimetypes import  guess_type
from django.http import HttpResponse, Http404
import time


# Create your views here.

global_context = {}

def upload(request):
    # return render(request, 'ChangeDetection')

    context = {}
    if request.method == 'GET':
        form = UploadImageForm()
        context['form'] = form
        return render(request, 'ChangeDetection', context)

    if request.method == 'POST':
        images = photo()
        all_photo = photo.objects.all()
        for temp in all_photo:
            temp.delete()
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['photo1']:
                images.image1 = form.cleaned_data['photo1']
            if form.cleaned_data['photo2']:
                images.image2 = form.cleaned_data['photo2']
            images.save()

        context['images'] = images
        context['form'] = form
        context['value'] = "changed"
        time.sleep(2)
        return render(request, 'ChangeDetection', context)


def upload1(request):
    # return render(request, 'ChangeDetection')

    context = {}
    if request.method == 'GET':
        form = UploadImageForm()
        context['form'] = form
        return render(request, 'ChangeDetection', context)

    if request.method == 'POST':

        images = photo()
        all_photo = photo.objects.all()
        for temp in all_photo:
            temp.delete()
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['photo1']:
                images.image1 = form.cleaned_data['photo1']
            if form.cleaned_data['photo2']:
                images.image2 = form.cleaned_data['photo2']
            images.save()

        context['images'] = images
        context['form'] = form
        context['value'] = "unchanged"
        time.sleep(2)
        return render(request, 'ChangeDetection1', context)

def get_picture(request, id):
    target_photo = photo.objects.all()
    if len(target_photo)==0:
        raise Http404
    target_photo = target_photo[0]
    if id == '1':
        if not target_photo.image1:
            raise Http404
    if id == '2':
        if not target_photo.image2:
            raise Http404

    content_type = guess_type(target_photo.image1.name)
    if id == '1':
        return HttpResponse(target_photo.image1, content_type=content_type)
    if id == '2':
        return HttpResponse(target_photo.image2, content_type=content_type)
    raise Http404


def compare(request):
    print global_context
    context = global_context
    context['value'] = "changed"
    print context['value']

    return render(request, 'ChangeDetection', context)

def index1(request):
    context = {}
    form = UploadImageForm()
    context['form'] = form
    return render(request, 'ChangeDetection1', context)


def index(request):
    context = {}
    form = UploadImageForm()
    context['form'] = form
    return render(request, 'ChangeDetection', context)