from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
    path('shop_1/<int:id>', views.shop_1, name='shop_1'),
    path('show_details/<int:id>', views.show_details, name='show_details'),
    path('search', views.search, name = 'search'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('view_cart', views.view_cart, name='view_cart'),
    path('update_cart/<int:id>',views.update_cart,name='update_cart'),
    path('delete_cart/<int:product_id>',views.delete_cart,name='delete_cart'),
    path('add_to_wish/<int:id>',views.add_to_wish,name='add_to_wish'),
    path('show_wish',views.show_wish,name='show_wish'),
    path('del_wish/<int:id>',views.del_wish,name='del_wish'),

]