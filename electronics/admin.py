from django.contrib import admin
from django.contrib.auth.admin import UserAdmin,UserCreationForm

from .forms import SignupForm
from .models import CustomUser, Product, Category, Cart


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = SignupForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)