
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/store/', include(('store_api.urls', 'api-store'), namespace='api-store'))
]
