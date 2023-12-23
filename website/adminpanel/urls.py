from django.urls import path
from adminpanel import views

urlpatterns = [
    path('dashboard', views.index, name='admin'),
    path('reg', views.registration, name='reg'),
    path('login', views.login_user, name='login'),
    path('logout',views.logoutUser, name='logoutUser'),
    path('change_pass',views.change_pass, name='change_pass'),
    path('customer_signup',views.customer_signup, name='customer_signup'),
    path('custo_login',views.customer_login, name='custo_login'),
    path('custo_logout',views.logoutcustomer, name='custo_logout'),
    path('customer_admin',views.customer_index, name='customer_admin'),
    # path('create_category',views.create_category, name='create_category'),


    #Category urls

    path('category_add',views.category_add, name='category_add'),
    path('show_category',views.show_category, name='show_category'),
    path('category_edit/<int:id>', views.category_edit, name= 'category_edit'),
    # path('category_update/<int:id>', views.category_update, name= 'category_update'),
    path('delete_category/<int:id>',views.delete_category, name= 'delete_category'),

    #Product Urls

    path('product_add',views.product_add, name='product_add'),
    path('product_show',views.product_show, name='product_show'),
    path('product_details/<int:id>',views.product_details, name='product_details'),
    

    
]