from django.urls import path
from shop_app import views

urlpatterns = [
    path("", views.product_list, name = "products_list"),
    path("<int:product_id>/", views.get_product_by_id, name = "product-details"),
    path("add-review/<int:product_id>", views.add_review, name = "add-review"),
]