from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teachers', include('teachers.urls')),
    path('',views.homepage),
    path('<id>/',views.timetable_is),
    path('after_attendance',views.after_attendance)
]

urlpatterns += staticfiles_urlpatterns()
