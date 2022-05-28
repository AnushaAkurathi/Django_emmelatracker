from django.urls import path
from .views import Sampleview, display, Ann_cv 

urlpatterns = [
    path('pagedemo', Sampleview, name = 'sample'),
    path('announcements', display.as_view(), name= 'disp'),
    path('add_post', Ann_cv.as_view(), name = 'addpost'),
    # path('attendance', attendance.as_view(), name = 'attendance'),
    ]
