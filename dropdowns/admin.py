from django.contrib import admin
from .models import *

class AllDataAdmin(admin.ModelAdmin):
	list_display = ['country','state','district','city']

class StateAdmin(admin.ModelAdmin):
	list_display = ['name','country']

class DistrictAdmin(admin.ModelAdmin):
	list_display = ['name','state']

class CityAdmin(admin.ModelAdmin):
	list_display = ['name','district']

admin.site.register(Country)
admin.site.register(State, StateAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(AllData, AllDataAdmin)
