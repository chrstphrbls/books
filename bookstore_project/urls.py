
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #django admin
    path('anything-but-admin/', admin.site.urls),

    #user management
    path('accounts/', include('allauth.urls')),

    #local apps
    path('',include('pages.urls')), #set pages to be the homepage
    path('books/', include('books.urls')), #link a path to the books page 
    path('orders/',include('orders.urls')), #link a path to the orders page
]

