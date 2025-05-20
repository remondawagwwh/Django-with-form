from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product, Category
from .forms import ProductFormModel, ProductForm
# Create your views here.
class ProductListClass(View):
    def get(self, request):
        context = {'products': Product.getall()}
        return render(request, 'product/list.html', context)


class ProductDeleteClass(View):
    def get(self, request, id):
        Product.softdelete(id)  # Call on class, passing the id
        return redirect('product_list')

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


def product_update_form(request, id):
    old_product = get_object_or_404(Product, pk=id)

    initial_data = {
        'name': old_product.name,
        'description': old_product.description,
        'price': old_product.price,
        'stock': old_product.stock,
        'sku': old_product.sku,
        'image': old_product.image,
        'category': old_product.category.id
    }

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            old_product.name = form.cleaned_data['name']
            old_product.description = form.cleaned_data['description']
            old_product.price = form.cleaned_data['price']
            old_product.stock = form.cleaned_data['stock']
            old_product.sku = form.cleaned_data['sku']
            if form.cleaned_data['image']:
                old_product.image = form.cleaned_data['image']
            old_product.category = get_object_or_404(Category, pk=form.cleaned_data['category'])
            old_product.save()
            return redirect('product_list')
    else:
        form = ProductForm(initial=initial_data)

    context = {'form': form}
    return render(request, 'product/updateform.html', context)


def product_new_form(request):
    form = ProductForm(data=request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        if form.is_bound and form.is_valid():
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
    if request.method == 'POST':
        form = ProductFormModel(data=request.POST, files=request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductFormModel(instance=product)
    return render(request, 'product/updateform.html', {'form': form})


# def product_update_form(request, id):
#     product = get_object_or_404(Product, id=id)
#
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Get the Category instance first
#             category_id = form.cleaned_data['category']
#             category = Category.objects.get(pk=category_id)
#
#             product.name = form.cleaned_data['name']
#             product.price = form.cleaned_data['price']
#             if form.cleaned_data.get('image'):
#                 product.image = form.cleaned_data['image']
#             product.description = form.cleaned_data['description']
#             product.category = category  # Assign the Category instance
#             product.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm(initial={
#             'name': product.name,
#             'price': product.price,
#             'description': product.description,
#             'category': product.category.id,  # Pass the ID for initial data
#         })
#
#     return render(request, 'product/updateform.html', {'form': form})


def product_list(request):
    return render(request, 'product/list.html', {'products': Product.getall()})
def product_show(request, id):
    return render(request, 'product/details.html', {'product': Product.get_by_id(id)})