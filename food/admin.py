from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import FoodResource
from .models import Foods


class FoodResourceAdmin(ImportExportModelAdmin):
    resource_classes = [FoodResource]

admin.site.register(Foods, FoodResourceAdmin)
