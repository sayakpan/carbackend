from django.contrib import admin
from cars.models import Car
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.    

class CarResource(resources.ModelResource):
    class Meta:
        model = Car
        exclude = ('id',)

@admin.register(Car)
class CarAdmin(ImportExportModelAdmin):
    list_display = ('id', 'brand', 'model', 'year', 'fuel_type', 'price', 'status')
    search_fields = ('brand', 'model')
    list_filter = ('year', 'fuel_type', 'status')
    ordering = ('-id',)
    list_per_page = 20