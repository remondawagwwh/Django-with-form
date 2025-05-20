from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListClass.as_view(), name='product_list'),
    path('add/', views.product_new_form, name='product_new_form'),  # باستخدام Form عادي
    path('add-model/', views.product_new_form_model, name='product_new_form_model'),  # باستخدام ModelForm
    path('update/<int:id>/', views.product_update_form, name='product_update_form'),  # باستخدام Form عادي
    path('update-model/<int:id>/', views.product_update_form_model, name='product_update_form_model'),  # باستخدام ModelForm
    path('delete/<int:id>/', views.ProductDeleteClass.as_view(), name='product_delete'),
    #path('details/<int:id>/', views.product_show, name='product_details'),
]
