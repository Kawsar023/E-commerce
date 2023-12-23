from django.shortcuts import redirect, render, HttpResponse
from adminpanel.models import category,product,product_image
from frontend.models import wishlist,check_out
import sweetify
from django.db.models import Q



def index(request):
    cat = category.objects.all()
    cat_2 = category.objects.filter().order_by('-id')[:6]
    # feature_image = product.objects.prefetch_related('product')
    wish_list = wishlist.objects.all().count()
    return render(request, 'frontend/index.html',{'cat': cat, 'cat_2': cat_2, 'wish_list': wish_list})


def shop(request):
    cat = category.objects.all()
    all_product = product.objects.all()
    wish_list = wishlist.objects.all().count()
    return render(request, 'frontend/shop.html',{'cat': cat,'all_product':all_product, 'wish_list': wish_list})

def shop_1(request,id):
    cat = category.objects.all()
    prod_pic = product.objects.filter(product_category_id = id).prefetch_related('product')
    return render(request, 'frontend/shop.html',{'cat': cat, 'prod_pic': prod_pic})


def show_details(request,id):
    cat = category.objects.all()
    prod = product.objects.filter(id = id).prefetch_related('product')
    # t_id = id
    # prod = product.objects.raw("SELECT * FROM adminpanel_product WHERE id = %s", [t_id])

    return render(request, 'frontend/show_details.html', {'cat': cat, 'prod': prod})

def search(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        if search!= None:
            prod   = product.objects.filter(Q(product_name__icontains = search) | Q (product_new_price__icontains = search))

            return render(request, 'frontend/shop2.html', {'prod': prod})
        else:
            sweetify.success(request, 'No Data Found')
            return render(request, 'frontend/shop2.html')
    
    return render(request, 'frontend/shop2.html')





def add_to_cart(request,product_id,quantity=1):
    # prod = get_object_or_404(product,id = product_id)
    cart = request.session.get('cart',{})
    quantity = int(request.POST.get('quantity',1))
    cart[product_id] = cart.get(product_id,0) + 1
    # quantity = request.POST.get('quantity')
    request.session['cart'] = cart
    return redirect('shop')

def view_cart(request):
    
    cart = request.session.get('cart',{})
    cart_item = [] 

    for product_id,quantity in cart.items():
        products = product.objects.get(id=product_id)
        total_price = sum(item['products'].product_new_price * item['quantity'] for item in cart_item)
        cart_item.append({'products':products,'quantity':quantity,'total_price':total_price})
        
    return render(request,'frontend/cart.html',{'cart_item':cart_item,})

def update_cart(request,id):
    cart = request.session.get('cart',{})

    new_quantity = int(request.POST.get('qtt',1))

    cart[id] = new_quantity

    request.session['cart'] = cart

    return redirect('view_cart')


def delete_cart(request,product_id):
    cart = request.session.get('cart',{})

    # if id in cart:
    #     del cart[id]
    #     request.session['cart'] = cart
    #     request.session.save()
    # return redirect('view_cart')

    pd_id = str(product_id)
    del request.session['cart'][pd_id]
    request.session['cart'] = cart
    # request.session.save()
    return redirect('view_cart')


def chek_out(request):
    if request.session.has_key('abc'):
        cart = request.session.get('cart',{})
        print(cart)
        # cart_P = cart
        # cart_P = cart

        for i in cart:
            check_outs = check_out(
                custom_user_id = request.session.get('abc',id),
                prod_id = i,
                # prodct_qtt = i.value()

            )
            check_outs.save()
            # print(i)
            
            request.session['cart'] = {}

        return redirect('view_cart')
    else:
        return redirect('cusom_login')

def add_to_wish(request,id):
    if request.session.has_key('abc'):
        wish_list = wishlist(
            prd_id = id,
            cust_id = request.session.get('abc',id)
        )
        wish_list.save()
        return redirect('shop')
    else:
        return redirect('cusom_login')


def show_wish(request):
    wish_list = wishlist.objects.all()
    return render(request,'frontend/show_wish.html',{'wish_list':wish_list})

def del_wish(request,id):
    if request.session.has_key('abc'):
        wish_list_del = wishlist.objects.filter(id=id).delete()
        return redirect('show_wish')
    else:
        return redirect('cusom_login')
    


