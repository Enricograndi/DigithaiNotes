# Import necessary modules
from django.contrib import admin
from django.urls import path, include

# Define the urlpatterns list
urlpatterns = [
    # URL for Django's admin site
    path('admin/', admin.site.urls),

    # URL for including authentication app's URLs
    path("", include('authentication.urls')),

    # URL for including notes app's URLs
    path("", include('notes.urls')),
]
