from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product, Category
from django.http import HttpResponse
from .forms import ProductForm, ProductFormModel
import os
from django.conf import settings
from django.views import View

# Create your views here.
