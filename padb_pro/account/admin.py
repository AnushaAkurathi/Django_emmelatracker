"""from django.contrib import admin
from django .contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_admin', 'is_staff',)
    search_fileds =('email', 'username',)
    readonly_fields = ('date_joined',)

    filter_horizontal= ()
    list_filter=()
    fieldsets = ()

admin.site.register(Account)"""
#from .models import User
#from django.contrib import admin

#admin.site.register(User)



from .models import User
from django.contrib import admin
from .forms import CustomeUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomeUserCreationForm

    fieldsets = (
            *UserAdmin.fieldsets,
            (
                'User roleeee', {
                    'fields':(
                        'is_director',
                        'is_producer'

                        )

                    }
                )

            )


admin.site.register(User, CustomUserAdmin)