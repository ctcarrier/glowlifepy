from catalog.models import Trick, TrickCategory
from django.contrib import admin

class TrickAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


admin.site.register(Trick, TrickAdmin)
admin.site.register(TrickCategory)