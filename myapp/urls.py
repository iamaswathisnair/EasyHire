"""
URL configuration for workersportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views
from .views import CustomPasswordResetView, password_reset_done

urlpatterns = [


     path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    # path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('register/',views.reg1,name='reg'),
    path('login/',views.login,name='log'),
    path('workerlogin/',views.workerlogin,name='login'),

    path('home/',views.home1,name='home'),
    path('workerreg/',views.workerreg,name='workerreg'),
    path('jobposting/',views.jobposting,name='jobposting'),
    path('joblisting/',views.joblisting,name='joblisting'),
    path('delete/<int:id>',views.deleteee,name='delete'),


    path('workerhome/',views.workerhome,name='workerhome'),
    path('choice/',views.choice,name='choice'),
    path('loginchoice/',views.loginchoice,name='loginchoice'),
    
    path('profile/',views.profile1,name='profile'),
    path('update/',views.update,name='update'),
    path('updateprofile/',views.updateprofile,name='updateprofile'),
    path('gallery/',views.gallery,name='gallery'),
    path('workerprofile/',views.workerprofile,name='workerprofile'),
    path('workerupdate/',views.workerupdate,name='workerupdate'),
    path('userjoblisting/',views.userjoblisting,name='userjoblisting'),

    path('search/',views.search,name='seraching'),
    # path('jobbb/',views.jobbb,name='jobbb'),

    path('user_complaints/',views.user_complaints,name='usercomplaints'),
    path('user_feedback/',views.user_feedback,name='userfeedback'),


    path('category_jobs/<str:category>/', views.category_jobs, name='category_jobs'),
    path('worker_booking/<str:workername>/',views.worker_booking,name='worker_booking'),
    path('book_job/',views.book_job,name='book_job'),



    path('userbkinglist/', views.userbkinglist, name='userbkinglist'),
    path('request/', views.request, name='request'),
    path('listworks/<str:name>/', views.listworks, name='listworks'),
    path('deletebooking/<int:id>',views.deletebooking,name='deletebooking'),

    
    path('update_status/<int:workerbooking_id>/', views.update_status, name='update_status'),
]





