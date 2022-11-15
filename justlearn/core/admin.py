from django.contrib import admin

from .models import Chat, Lesson, Message, Student, Teacher, User

# Register your models here.
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Lesson)
