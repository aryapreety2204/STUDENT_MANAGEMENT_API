from django.urls import path
from . views import*
from Home.views import*
from django.conf import settings
from django.conf.urls.static import static
from .api import*

urlpatterns = [
    path('', index),
    path("signin/",sign_in),
    path('signup/',signup),
    path("register/",create_user),
    path('courses/',courses),
    path('dashboard/',dashboard),
    path('viewstudents/',viewstudents,name='viewstudents'),
    path('profile/',profile),
    # path("dashboard/",add_user),
    path("addCourses/",add_courses),
    path("delete/<int:pk>/",delete_course, name="delete"),
    path("update/<int:uid>/",update,name="update"),
    path("update_courses/",update_course_view),
    path("addStudent/",add_student , name='add_student'),
    
    # Api Urls
    
    path('api/user',CreateUSerApi.as_view()),
    path('api/get',itemList.as_view()),
    path('api/course',CreateCourseApi.as_view()),
    path('student/course',CreateStudentApi.as_view()),
    path('api/update/<int:pk>/',CourseUpdateApi.as_view()),
    path('api/delete/<int:pk>/',CourseDeleteApi.as_view()),
    path('student/update/<int:pk>',StudentUpdateApi.as_view()),
    path('student/delete/<int:pk>/',StudentDeleteApi.as_view()),
    
    
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)