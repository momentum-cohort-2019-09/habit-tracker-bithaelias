"""congif URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from habit_tracker import views

urlpatterns = [
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.home_habits, name='home'),
    path('habit_tracker/new/', views.create_habit, name='create_habit'),
    path('habit_tracker/<int:pk>/create_a_journal/',views.create_a_journal, name='create_a_journal'),
    path('habit_tracker/<int:pk>/habit_details', views.habit_details, name='habit_details'), 
    path('admin/', admin.site.urls),
]
