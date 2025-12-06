from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
    
    path('Index/' , views.index),
    path('Contactus/' , views.Contactus,name="Contactus"),
    path('aboutus/' , views.aboutus,name="aboutus"),
    path('login/' , views.login,name="login"),
    #path('Product/' , views.Product,name="Product"),
    path('Promotion/' , views.Promotion,name="Promotion"),

    path('',views.OganiIndex,name = "OganiIndex"),
    path('OganiShopGrid/',views.OganiShopGrid,name="OganiShopGrid"),
    path('OganiBlogDetails/',views.OganiBlogDetails,name="OganiBlogDetails"),
    path('Blog/',views.Blog,name="Blog"),
    path('CheckOut/',views.CheckOut,name="CheckOut"),
    path('Contact/',views.Contact,name="Contact"),
    path('ShopDetails/<int:pk>/',views.ShopDetails,name="ShopDetails"),
    path('ShopingCart/',views.ShopingCart,name="ShopingCart"),


    path('create/', views.create_book, name='create_book'),
    path('book_list/', views.book_list, name='book_list'),
    path('update/<int:book_id>/', views.update_book, name='update_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),

    path('item_list/', views.item_list, name='item_list'),
    path('create_item/', views.create_item, name='create_item'),

    path('update_item/<int:pk>/', views.update_item, name='update_item'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),


# Ogani ---------------------------------
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout_view/', views.checkout_view, name='checkout_view'),

    path('billing_add/', views.billing_add, name='billing_add'),
# Billing Page
    path('billing_list/', views.billing_list, name='billing_list'),
]