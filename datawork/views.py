from django.core.files import base
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q  
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
def errorpage(r):
    return render(r, "404page.html")


@login_required
def Home(r):
    id = Customer().id
    return render(r, "index.html",{
        "product": Product.objects.all().count(),
        "users": User.objects.all().count(),
        "pro": Product.objects.all()[:5],
        "order": Order.objects.all().count(),
        "credits": Order.objects.filter(pay_method = "Credit").count(),
    })


def AddProduct(r):
    if r.user.is_staff or r.user.is_superuser:
        forms = productForm(r.POST or None, r.FILES or None)
        if r.method=="POST":
            if forms.is_valid():
                p = Product()
                p.name = r.POST.get("name")
                p.brand = Brand(r.POST.get("brand"))
                p.quantity = r.POST.get("quantity")
                p.image = r.FILES.get("image")
                p.product_size = Size(r.POST.get("product_size"))
                p.price = r.POST.get("price")
                p.category = Category(r.POST.get("category"))
                p.product_thickness = Thickness(r.POST.get("product_thickness"))
                p.save()
                messages.success(r, 'Form submission successful')
                return redirect(AddProduct)
        return render(r, "AddProduct.html",{
            "cat": Category.objects.all(),
            "brand": Brand.objects.all(),
            "size": Size.objects.all(),
            "thick": Thickness.objects.all(),
        })
    else:
        return redirect(errorpage)


def Products(r):
    return render(r, "Products.html",{
        "product": Product.objects.all(),
        "order_product": OrderProduct.objects.all()
    })


def delete_product(r,id):
    get_id = Product.objects.get(id = id)
    get_id.delete()
    messages.error(r, 'Document deleted.')
    return redirect(Products)


def edit_product(r,id):
    get_id = Product.objects.get(id=id)
    editform = productForm(r.POST or None, r.FILES or None, instance=get_id)
    if r.method == "POST":
        if editform.is_valid():
            editform.save()
            return redirect(Products)
    return render(r,"edit_product.html", {"edit_form": editform})


@login_required
def AddCategory(r):
    if r.user.is_staff or r.user.is_superuser:
        forms = categoryForms(r.POST or None)
        if r.method =="POST":
            if forms.is_valid():
                c = Category()
                c.cat_name = r.POST.get('cat_name')
                c.cat_desc = r.POST.get('cat_desc')
                c.save()
                forms.save()
                messages.success(r, 'Form submission successful')
                return redirect(AddCategory)
        return render(r, "AddCategory.html",{
            "form": forms,
            "cat": Category.objects.all(),
        })
    else:
        return redirect(errorpage)


@login_required
def delete_category(r, id):
    get_id = Category.objects.get(id = id)
    get_id.delete()
    messages.error(r, 'Document deleted.')
    return redirect(AddCategory)


def edit_category(r):
    pass


def AddBrand(r):
    forms = brandfForms(r.POST or None)
    if r.method=="POST":
        if forms.is_valid():
            b = Brand()
            b.brand_name = r.POST.get('brand_name')
            b.brand_desc = r.POST.get('brand_desc')
            b.save()
            messages.success(r, 'Form submission successful')
            return redirect(AddBrand)
    return render(r, "AddBrand.html",{
        "brand": Brand.objects.all()
    })


def delete_brand(r,id):
    get_id = Brand.objects.get(id=id)
    get_id.delete()
    messages.error(r, 'Document deleted.')
    return redirect(AddBrand)


def edit_brand(r):
    pass


def Addsize(r):
    if r.user.is_staff or r.user.is_superuser:
        forms = sizeForms(r.POST or None)
        if r.method=="POST":
            if forms.is_valid():
                s = Size()
                s.size_name = r.POST.get('size_name')
                s.save()
                messages.success(r, 'Form submission successful')
                return redirect(Addsize)
        return render(r, "Addsize.html",{
            "size": Size.objects.all()
        })
    else:
        return redirect(errorpage)

def delete_size(r,id):
    get_id = Size.objects.get(id=id)
    get_id.delete()
    messages.error(r, 'Document deleted.')
    return redirect(Addsize)



def edit_size(r):
    pass


def thickness(r):
    forms = thicknessForms(r.POST or None)
    if r.method=="POST":
        if forms.is_valid():
            t = Thickness()
            t.thickness_name = r.POST.get("thickness_name")
            t.save()
            messages.success(r, 'Form submission successful')
            return redirect(thickness)
    return render(r, "thickness.html",{
        "thick": Thickness.objects.all()
    })


def delete_thickness(r,id):
    get_id = Thickness.objects.get(id=id)
    get_id.delete()
    messages.error(r, 'Document deleted.')
    return redirect(thickness)


def edit_thickness(r):
    pass


def issue(r):
    if r.user.is_staff or r.user.is_superuser:
        forms = OrderForms(r.POST or None)
        if r.method=="POST":
            order = Order.objects.filter(ordered=False)
            if order.exists():
                print("already order exist")
            else:
                order, created = Order.objects.get_or_create(
                    c_id = Customer(r.POST.get("c_id")),
                    discount_price = r.POST.get("discount_price"),
                    pay_method = r.POST.get("pay_method"),
                )
                for p in r.POST.getlist("item[]"):
                    orderPro, created = OrderProduct.objects.get_or_create(item = Product(p), qty=1)
                    order.items.add(orderPro)
                    order.ordered = True
                    order.save()
                return redirect(issue)
        return render(r, "issue.html",{
            "pro": Product.objects.all(), 
            "customer": Customer.objects.all(),
            "order": Order.objects.all(),
        })
    else:
        return redirect(errorpage)


@login_required
def searchcon(r):
    if r.method == "GET":
        search_data = r.GET.get('search')
        return render(r, "issue.html",{
            "order": Order.objects.filter(c_id__contact=search_data),
        })
    else:
        return redirect(issue)


@login_required
def searchpro(r):
    if r.method == "GET":
        search_data = r.GET.get('search')
        return render(r, "Products.html",{
            "order_product": OrderProduct.objects.filter(item__name = search_data),
        })
    else:
        return redirect(issue)


def report(r):
    if r.method == "GET":
        q1 = r.GET.get("q1")
        q2 = r.GET.get("q2")
        return render(r, "Report.html",{
            "se":Order.objects.filter(start_date__range=[q1, q2])
        })

def profile(r):
    return render(r, "Profile.html")


def adduser(r):
    forms = userForms(r.POST or None)
    if r.method=="POST":
        if forms.is_valid():
            u = User()
            u.username = r.POST.get("username")
            u.email = r.POST.get("email")
            u.password = r.POST.get("password")
            u.save()
            messages.success(r, 'Your Data is adde Successfully')
    return render(r, "adduser.html")


def manageuser(r):
    return render(r, "manageuser.html",{
        "userdetails": User.objects.all()
    })


def deleteuser(r,id):
    get_id = User.objects.get(id=id)
    get_id.delete()
    return redirect(manageuser)


def approveuser(r,id):
    leave = User.objects.get(id=id)
    leave.is_staff=True
    leave.save()
    return redirect(manageuser)


def disapproveuser(r,id):
    leave = User.objects.get(id=id)
    leave.is_staff=False
    leave.save()
    return redirect(manageuser)


# text for autofill
@login_required
def serachuser(r):
    if r.method == "GET":
        search_data = r.GET.get('txtSearch')

        data = {
            "pro": Product.objects.filter(name__icontains=search_data),
        }
        return render(r, "issue.html", data)
    else:
        return redirect(issue)


@login_required
def delete_order(r, id):
    get_id = Order.objects.get(id=id)
    get_id.delete()
    return redirect(issue)

@login_required
def order_view(r, id):
    return render(r, "order_view.html",{
        "orders": Order.objects.filter(id = id),
        "ordering": Order.objects.get(id = id, ordered=True)
    })


def add_customer(r):
    forms = CustomerForms(r.POST or None)
    if r.method=="POST":
        if forms.is_valid():
            c = Customer()
            c.name = r.POST.get("name")
            c.contact = r.POST.get("contact")
            c.address = r.POST.get("address")
            c.save()
            return redirect(add_customer)
    return render(r, "customer.html",{
        "customer": Customer.objects.all()
    })

@login_required
def delete_customer(r, id):
    get_id = Customer.objects.get(id=id)
    get_id.delete()
    return redirect(add_customer) 

@login_required
def customer_view(r, id):
    return render(r, "customer.html")


def order(r):
    forms = OrderForms(r.POST or None)
    if r.method == "POST":
        order = Order.objects.filter(ordered=False)
        if order.exists():
            print("already order exist")
        else:
            order, created = Order.objects.get_or_create(
                c_id = Customer(r.POST.get("c_id")),
                discount_price = r.POST.get("discount_price"),
                pay_method = r.POST.get("pay_method"),
            )
        
            for p in r.POST.getlist("item[]"):
                orderPro, created = OrderProduct.objects.get_or_create(item = Product(p), qty=1)
                order.items.add(orderPro)
                order.ordered = True
                order.save()
            return redirect(issue)
    return render(r, "Order.html",{
        "pro": Product.objects.all(), 
        "cat": Category.objects.all(),
        "brand": Brand.objects.all(),
        "size": Size.objects.all(),
        "thick": Thickness.objects.all(), 
        "customer": Customer.objects.all(),
    })


def load_brand(r):
    cat_id = r.GET.get("category")
    return render(r, "brand_dropdown.html",{
        "brand": Brand.objects.filter(brand_cxategory = cat_id)
    })

def load_thick(r):
    brand_id = r.GET.get("brand")
    return render(r, "thick_dropdown.html",{
        "Thick": Thickness.objects.filter(thick_brand = brand_id)
    })

def load_size(r):
    thick_id = r.GET.get("thickness")
    return render(r, "size_dropdown.html",{
        "size": Size.objects.filter(size_thick = thick_id)
    })

def load_pro(r):
    size_id = r.GET.get("size")
    return render(r, "couses_dropdown.html",{
        "pro": Product.objects.filter(product_size = size_id)
    })