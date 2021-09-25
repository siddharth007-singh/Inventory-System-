from django.contrib import admin
from django.urls import path, include
from datawork import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Home, name="Home"),
    path("profile", views.profile, name="profile"),
    path("AddProduct", views.AddProduct, name="AddProduct"),
    path("Products", views.Products, name="Products"),
    path("edit_product/<int:id>", views.edit_product, name="edit_product"),
    path("AddCategory", views.AddCategory, name="AddCategory"),
    path("thickness", views.thickness, name="thickness"),
    path("delete_category/<int:id>", views.delete_category, name="delete_category"),
    path("delete_brand/<int:id>", views.delete_brand, name="delete_brand"),
    path("delete_size/<int:id>", views.delete_size, name="delete_size"),
    path("delete_thickness/<int:id>", views.delete_thickness, name="delete_thickness"),
    path("delete_product/<int:id>", views.delete_product, name="delete_product"),
    path("AddBrand", views.AddBrand, name="AddBrand"),
    path("Addsize", views.Addsize, name="Addsize"),
    path("issue", views.issue, name="issue"),
    path("report", views.report, name="report"),
    path("adduser", views.adduser, name="adduser"),
    path("manageuser", views.manageuser, name="manageuser"),
    path("deleteuser/<int:id>", views.deleteuser, name="deleteuser"),
    path("approveuser/<int:id>", views.approveuser, name="approveuser"),
    path("disapproveuser/<int:id>", views.disapproveuser, name="disapproveuser"),
    path('accounts/', include('allauth.urls')),
    path("errorpage", views.errorpage, name="errorpage"),
    path("serachuser", views.serachuser, name="serachuser"),
    path("delete_order/<int:id>", views.delete_order, name="delete_order"),
    path("order_view/<int:id>", views.order_view, name="order_view"),
    path("add_customer", views.add_customer, name="add_customer"),
    path("delete_customer/<int:id>", views.delete_customer, name="delete_customer"),
    path("customer_view/<int:id>", views.customer_view, name="customer_view"),
    path("searchcon/", views.searchcon, name="searchcon"),
    path("searchpro/", views.searchpro, name="searchpro"),
    path("order/", views.order, name="order"),
    path("load-product/", views.load_pro, name="ajax_load_product"),
    path("load-brand/", views.load_brand, name="ajax_load_brand"),
    path("load-thick/", views.load_thick, name="ajax_load_thick"),
    path("load-size/", views.load_size, name="ajax_load_size"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
