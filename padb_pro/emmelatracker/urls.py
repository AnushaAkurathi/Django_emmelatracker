from django.urls import path
from .views import homePageView, trackingPageView, loadingPageView, HomeDataView, Announcements, Attendance, Worklogs_V, Worklogs_C, Worklogs_D
from .views import WorklogDV, Worklogs_U
from django.contrib.auth.decorators import login_required

# from .views import HomeDataView
urlpatterns = [
   path('home', homePageView, name='homewithhtml'),
   path('tracking', trackingPageView.as_view(), name='trackingwithhtml'),
   path('loading', loadingPageView.as_view(), name='loadingwithhtml'),
   path('team', HomeDataView.as_view(), name='teamswithhtml'),
   path('attendance', Attendance.as_view(), name ='attendancewithhtml'),
   path('announcements', Announcements.as_view(), name = 'announcements'),
   path('worklogs', Worklogs_V.as_view(), name='worklogswithhtml'),
   path('Worklogs_add_post', login_required(Worklogs_C.as_view()), name='worklogsaddpost'),
   path('worklogs/<int:pk>', WorklogDV.as_view(), name = 'wlarticle-detail'),
   path('logs/edit/<int:pk>', login_required(Worklogs_U.as_view()), name = 'wleditlogs'),
   path('logs/<int:pk>/remove', login_required(Worklogs_D.as_view()), name = 'wldeletelogs'),
   ]
