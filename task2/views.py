from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def func_template(request):
    return render(request, 'func_template.html')


def class_template(request):
    return render(request, 'class_template.html')
