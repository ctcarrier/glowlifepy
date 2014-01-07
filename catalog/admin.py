from catalog.models import Trick, TrickCategory
from django.contrib import admin

class TrickAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description']}),
        (None, {'fields': ['trick_category']}),
    ]


admin.site.register(Trick, TrickAdmin)
admin.site.register(TrickCategory)