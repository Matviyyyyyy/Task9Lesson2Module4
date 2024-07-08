from django.shortcuts import render
from shop_app.models import Product, Review

def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(
        request,
        template_name="shop/products_page.html",
        context=context,
    )

def get_product_by_id(request, product_id):
    product = Product.objects.get(id = product_id)
    reviews = Review.objects.filter(product=product).all()
    context = {
        "product": product,
        "reviews": reviews,
    }
    return  render(
        request,
        template_name="shop/product_details.html",
        context=context,
    )
