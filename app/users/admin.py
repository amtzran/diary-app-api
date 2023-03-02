from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['name', 'username', 'is_active', 'is_verified', 'is_staff', 'is_superuser', 'is_deleted',
                    'last_login', 'created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('name', 'first_name', 'username', 'password',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_verified',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'is_deleted',
                    'user_permissions',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login', 'created_at', 'updated_at',)}),
    )
    readonly_fields = ['last_login', 'created_at', 'updated_at']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'first_name',
                'username',
                'password1',
                'password2',
                'is_verified',
                'is_active',
                'is_staff',
                'is_superuser',
                'is_deleted',
            )
        }),
    )


admin.site.register(User, UserAdmin)
