from django.shortcuts import render
from forms import *
from models import *

# Create your views here.
def login(request):
    # return render(request, 'ChangeDetection')

    context = {}


    if request.method == 'GET':
        form = UploadImageForm()
        context['form'] = form
        return render(request, 'ChangeDetection', context)

    if request.method == 'POST':
        images = photo()
        
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['photo1']:
                images.image1 = form.cleaned_data['photo1']
            if form.cleaned_data['photo2']:
                images.image2 = form.cleaned_data['photo2']
            images.save()

        context['images'] = images
        context['form'] = form
        return render(request, 'ChangeDetection', context)


