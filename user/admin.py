from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import User, Activity


class FTUserAdmin(UserAdmin):
    fieldsets = (
        (_('Personal info'),
         {'fields': (
             'id', 'first_name', 'last_name', 'email', 'job_title', 'phone_number', 'profile_picture',
             'username', 'password', 'company',
         )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'phone_number',

            )}
         ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['username', 'job_title', 'is_active', 'company']
    list_filter = []
    readonly_fields = ('id', 'email')

    def job_title(self, obj):
        return obj.job_title


admin.site.register(User, FTUserAdmin)
admin.site.register(Activity)
