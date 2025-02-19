from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def contacts(request):
    return render(request, "contacts.html")


def product(request, pk):
    product_x = get_object_or_404(Product, pk=pk)
    context = {"product_x": product_x}
    return render(request, "product.html", context)

