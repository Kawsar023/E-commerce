from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth.models import User
from adminpanel.models import User, cuostomer, category, product, product_image
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
# from adminpanel.models import category
from django.contrib import messages
import sweetify
from django.views.generic import ListView,CreateView,DeleteView,UpdateView

def index(request):
    if request.user.is_authenticated:
        
        # category = Category.objects.all()

        # context = {
        #     'category' : category,

        # }

        return render(request, 'adminpanel/index.html')
    
    else:
        return redirect('login')

def registration(request):
    if request.method == 'POST':
        username  = request.POST.get('user_name')
        email      = request.POST.get('email')
        password   = request.POST.get('password_1')
        conf_password = request.POST.get('password_2')

        if password != conf_password:
            return redirect('reg')
        else:
            user_reg = User.objects.create_user(username,email,password)
            user_reg.save()
            return redirect('login')
    return render(request, 'adminpanel/registration.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password  = request.POST.get('password')

        user   = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('admin')
        else:
            return redirect('login')
    return render(request, 'adminpanel/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def index(request):
    if request.user.is_authenticated:
        
        
        return render(request, 'adminpanel/index.html')
    else:
        return redirect('login')

# def reg_user(request):  
#     if request.method == 'POST':
#         first_name = request.POST.get('f_name')
#         last_name  = request.POST.get('l_name')
#         user_name  = request.POST.get('u_name')
#         email      = request.POST.get('email')
#         password   = request.POST.get('pass_1')
#         conf_password = request.POST.get('pass_2')

#         if password != conf_password:
#             return redirect('register')
#         else:
#             user_reg = User.objects.create_superuser(user_name,email,password)
#             user_reg.first_name = first_name
#             user_reg.last_name  = last_name
#             user_reg.save()
#             return redirect('login')
        
#     return render(request, 'adminpanel/register.html')

# def login_user(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         password  = request.POST.get('password')

#         user   = authenticate(username = user_name, password = password)
#         if user is not None:
#             login(request,user)
#             return redirect('admin')
#         else:
#             return redirect('login')
        
#     return render (request, 'adminpanel/login.html')


# def logoutUser(request):
#     logout(request)
#     return redirect('login')


def change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            old_pass = request.POST.get('old_pass')
            new_pass = request.POST.get('new_pass')
            confirm_pass = request.POST.get('confirm_pass')

            xyz = User.objects.get(id = request.user.id)
            # print(xyz)

            # if xyz.check_password(old_pass) and new_pass == confirm_pass:
            #     print("i am in")
            #     xyz.set_password(new_pass)
            #     xyz.save()
            #     update_session_auth_hash(request, xyz)
            #     return redirect('logoutUser')
            # else:
            #     # return redirect('change_pass')
            #     return HttpResponse("Wrong")
            if xyz.check_password(old_pass) and new_pass == confirm_pass:
                xyz.set_password(new_pass)
                xyz.save()
                update_session_auth_hash(request, xyz)
                return redirect('logoutUser')
            else:
                return redirect('change_pass')


        return render(request, 'adminpanel/change_pass.html')
    
    else:
        return redirect('login')



def customer_signup(request):

    if request.method == "POST":

        username = request.POST.get('user_name')
        f_name = request.POST.get('first_name')
        mobile = request.POST.get('mobile_number')
        password = request.POST.get('password')

        custom_user = cuostomer(
            username = username,
            first_name  = f_name,
            mobile_number  = mobile,
            password = make_password(password),
            
        )
        custom_user.save()
        return redirect('custo_login')
    
    return render (request, 'customer/signup.html')

def customer_login(request):

    if request.method == "POST":
        # x = request.POST.get('user_name')
        # y  = request.POST.get('password')
        x = request.POST['user_name']
        y  = request.POST['password']

        abc   = cuostomer.get_customer_by_username(x)

        if abc:
            psw = check_password(y, abc.password)

            if psw:
                request.session['abcd'] = abc.id
                return redirect ('customer_admin')
            else:
                return redirect('custo_login')

    return render (request, 'customer/login.html')
    

def customer_index(request):
    if request.session.has_key('abcd'):
        return render (request, 'customer/admin_dashboard.html')
    else:
        return redirect('custo_login')
    

def logoutcustomer(request):
    # request.session.clear()
    try:
        del request.session['abcd']
    except:
        pass
    return redirect('custo_login')




def category_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            category_name = request.POST.get('category_name')
            category_image = request.FILES['feature_image']

            cat_save = category(
                category_name = category_name,
                category_image  = category_image

            )
            cat_save.save()
            sweetify.success(request, 'Category has been Saved')
        return render (request, 'category/Add_category.html')
    else:
        return redirect('login')
    

def show_category(request):
    if request.user.is_authenticated:
        category_show = category.objects.all()
        return render(request,'category/Show_category.html', {'category_show': category_show})
    else:
        return redirect('login')
    

def category_edit(request,id):
    if request.user.is_authenticated:
       category_edit = category.objects.filter(id=id)
       return render(request,'category/category_edit.html',{'category_edit' : category_edit})
    
    else:
     return redirect('show_category')
    

def category_update(request, id):
    if request.method =="POST" and request.FILES: 
        a = request.POST.get('category_name')
        b = request.FILES['category_image']

        xyz = category.objects.filter(id=id)
        xyz = category(
            id = id,
            category_name           = a,
            category_image           = b,

            
        ).save()
        # xyz.save()
        return redirect('show_category')
    
def delete_category(request,id):
    del_category = category.objects.filter(id=id).delete()
    return redirect ('show_category')


def product_add(request):
    if request.user.is_authenticated:
        all_cat = category.objects.all()
        # if request.method == "POST" and request.FILES['product_image']:
        if request.method == "POST" and request.FILES:

            product_cat            = request.POST.get('product_cat')
            product_name           = request.POST.get('product_name')
            product_new_price      = request.POST.get('product_new_price')
            product_old_price      = request.POST.get('product_old_price')
            product_description    = request.POST.get('product_description')
            
            prod_image          = request.FILES.getlist('product_image')

            product_save = product(

                product_category_id = product_cat,
                product_name        = product_name,
                product_new_price   = product_new_price,
                product_old_price   = product_old_price,
                product_description = product_description,
                
                
            )
            product_save.save()

            product_id = product_save.id
            for i in prod_image:
                product_img = product_image(
                    product_image_all = i,
                    product_table_id  = product_id
                )
                product_img.save()
                sweetify.success(request, 'Product has been Saved')

        return render(request,'product/Add_product.html', {'all_cat': all_cat})
    else:
        return redirect('login')
    

def product_show(request):
    if request.user.is_authenticated:
        product_show = product.objects.prefetch_related('product')
        return render(request,'product/Show_product.html', {'product_show': product_show})
    else:
        return redirect('login')

def product_details(request,id):
    if request.user.is_authenticated:
        product_show = product.objects.filter(id=id).prefetch_related('product')
        return render(request,'product/product_details.html', {'product_show': product_show})
    else:
        return redirect('login')




    













# def create_category(request):

#     if request.user.is_authenticated:
#         # if request.method == 'POST' and request.FILES['about_pic']:
#             name  = request.POST.get('name')
#             # about_desc_1 = request.POST.get('description_1')
#             # about_desc_2 = request.POST.get('description_2')
#             # about_pic    = request.FILES['about_pic']

#             Category_save = Category(

#                 name         = name,
#                 # about_description_1 = about_desc_1,
#                 # about_description_2 = about_desc_2,
#                 # about_pic           = about_pic
                
#                 )
#             Category_save.save()
#             messages.success(request,"Successfully Inserted")
#             return redirect('create_category')
#     return render (request, 'adminpanel/create_category.html')
        
    # else:
    #    return redirect('login')