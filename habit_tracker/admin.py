
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from habit_tracker.models import User, Habit, Journal


admin.site.register(User, UserAdmin)
admin.site.register(Habit)
admin.site.register(Journal)