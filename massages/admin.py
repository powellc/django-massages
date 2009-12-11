from massages.models import Massage, Rate, RateList
from django.contrib import admin
'''
class VendorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display  = ['name', 'town','public', 'created', 'updated']
    list_filter   = ['town', 'public', 'markets']
    ordering = ['-created']
    search_fields = ['name', 'description']
    date_hierarchy='created'
'''    
admin.site.register(Massage)
admin.site.register(Rate)
admin.site.register(RateList)
