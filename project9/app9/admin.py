from django.contrib import admin
from .models import Employee, Publication, Article
# Register your models here.


class CustumAdminEmployee(admin.ModelAdmin):
    list_display = ('name', 'age', 'position')
    # fields = ('name','age')
    # exclude = ('age',)
    search_fields = ('name',)
    # list_editable = ('age',)
    list_filter = ('position',)
    list_per_page = 40
    list_display_links = ('name', 'position')


admin.site.register(Employee, CustumAdminEmployee)
admin.site.register(Publication)
admin.site.register(Article)
