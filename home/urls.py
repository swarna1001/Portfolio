from django.contrib import admin
from django.urls import path, include
from home import views



# Django admin header customization

admin.site.site_header = "Developer Swarna"
admin.site.site_title = "Welcome to Swarna's Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('writings', views.writings, name='writings'),

]
