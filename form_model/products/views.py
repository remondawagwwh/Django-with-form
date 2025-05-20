from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Category
from .forms import ProductFormModel, ProductForm
from django.http import HttpResponse
# Create your views here.
class ProductListClass(View):
    def get(self, request):
        context = {'products': Product.getall()}
        return render(request, 'product/list.html', context)

class ProductDeleteClass(View):
    def get(self, request, id):
        Product.objects.filter(id=id).delete()
        return Product.go_to_Products_List()

class ProductUpdate(View):
    def get(self, request, id):
        context = {'form': ProductFormModel(instance=Product.get_by_id(id))}
        return render(request, 'product/updateform.html', context)

    def post(self, request, id):
        form = ProductFormModel(data=request.POST, files=request.FILES, instance=Product.get_by_id(id))
        if form.is_bound and form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            return render(request, 'product/updateform.html', {'form': form, 'msg': form.errors})

def product_new_form_model(request):
    context = {'form': ProductFormModel()}
    if request.method == 'POST':
        form = ProductFormModel(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            context['form'] = form
            context['msg'] = form.errors
    return render(request, 'product/newform.html', context)

def product_new_form(request):
    form = ProductForm(data=request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        if(form.is_bound and form.is_valid()):
            Product.Add(
                Pname=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
                Pimage=form.cleaned_data['image'],
                sku=form.cleaned_data['sku'],
                catid=form.cleaned_data['category']
            )
            return redirect('product_list')
    return render(request, 'product/newform.html', {'form': form})
def product_update_form_model(request, id):
    product = Product.get_by_id(id)
    form = ProductFormModel(request.POST , request.FILES , instance=product)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'product/updateform.html', {'form': form})


def product_list(request):
    return render(request, 'product/list.html', {'products': Product.getall()})
def product_show(request, id):
    return render(request, 'product/details.html', {'product': Product.get_by_id(id)})