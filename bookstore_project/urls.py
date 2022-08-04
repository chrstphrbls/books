# bookstore_project/urls.py

from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #django admin
    path('admin/', admin.site.urls),

    #user management
    path('accounts/', include('allauth.urls')),

    #local apps
    path('',include('pages.urls')), #set pages to be the homepage
    path('books/', include('books.urls')),#link a path to the books page 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #define the upload path and url

