from django.contrib import admin
from cms.extensions import PageExtensionAdmin

from .models import CategoryExtension

class CategoryExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(CategoryExtension, CategoryExtensionAdmin)
