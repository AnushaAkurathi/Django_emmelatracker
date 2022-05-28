from django.contrib import admin
# from .models import Post, Comment
from .models import Announcements, Team, Bonus, Tasks, Worklogs, Attendance, CustomUser

admin.site.register(Team)
admin.site.register(Attendance)
admin.site.register(Announcements)
admin.site.register(Bonus)
admin.site.register(Tasks)
admin.site.register(Worklogs)
admin.site.register(CustomUser)



"""from .models import User
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


admin.site.register(User, CustomUserAdmin)"""