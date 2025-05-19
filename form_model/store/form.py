from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from store.forms import ProductForm

class ProductListView(View):
    def get(self, request):
        products = Product.objects.filter(is_active=True)
        return render(request, 'dashboard/product_list.html', {'products': products})

class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'dashboard/product_form.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        return render(request, 'dashboard/product_form.html', {'form': form})

class ProductUpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'dashboard/product_form.html', {'form': form})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        return render(request, 'dashboard/product_form.html', {'form': form})

class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'dashboard/product_confirm_delete.html', {'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('product-list')
