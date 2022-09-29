from turtle import title
from django.contrib import admin
from .models import Page
# Register your models here.

#configuracion extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('title', 'content')
    list_filter = ('visible', )
    list_display = ('title', 'visible', 'create_at')
    ordering = ('-create_at',)
#configuracion del panel

admin.site.register(Page, PageAdmin)



title = "Panel de Gestion"
subtitle = "Proyecto de Django"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle