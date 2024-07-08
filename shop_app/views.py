from django.shortcuts import render, redirect
from shop_app.models import Product, Review
from django.http import HttpResponse

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

def add_review(request, product_id):
    if request.method == "POST":
        review_author = request.POST.get("review_author")
        review_text = request.POST.get("review_text")
        review_rating = request.POST.get("review_rating")

        try:
            product = Product.objects.get(id = product_id)
        except ValueError:
            return HttpResponse(
                "Wrong value for product",
                status=400
            )
        except Product.DoesNotExist:
            return HttpResponse(
                "This product doesn't exist",
                status=404
            )
        new_review = Review.objects.create(
            product = product,
            author = review_author,
            text = review_text,
            rating = review_rating
        )

        return redirect("product-details", product_id = product.id)












