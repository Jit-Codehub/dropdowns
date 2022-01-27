from django.contrib import admin
from django.urls import path
from dropdowns import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('data/',views.data, name='data'),
    path('states/',views.load_states, name='load_states'),
    path('districts/',views.load_districts, name='load_districts'),
    path('cities/',views.load_cities, name='load_cities'),
    path('save/',views.save_data, name='save_data'),
]
