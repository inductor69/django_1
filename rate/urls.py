from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns=[
    path("",views.index,name="index"),
    path("login/",views.login,name="login"),
    path("prof/",views.prof,name="prof_info"),
    path("course/",views.course,name="course"),
    path("register/",views.register,name='register'),
    path("logout/",views.logout,name="logout"), 
    path('prof/<prof_name>', views.detail,name='detail'),
    path('course/<course_id>', views.course_detail,name='course_detail'),
    path('confirm/',views.confirmation,name='confirm'),
    path('complaints/',views.complaints,name='complaints'),
    path('forum/',views.forum,name='forum'),
    path('myview',views.my_view,name='hello'),
   
]