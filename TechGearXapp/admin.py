from django.contrib import admin

# Register your models here.
from TechGearXapp.models import Post, Cart


class PostAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.author:
            return True
        return False


admin.site.register(Post, PostAdmin)


class CartAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.author:
            return True
        return False


admin.site.register(Cart, CartAdmin)