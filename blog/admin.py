from django.contrib import admin
from .models import Category,Article




class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at','update_at')
    list_display = ('name', 'create_at')
    search_fields= ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at','update_at')
    search_fields= ('title', 'content', 'user', )
    list_display = ('title','user', 'public','create_at')
    list_filter = ('public', 'user__username')
    
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id= request.user.id

        obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
