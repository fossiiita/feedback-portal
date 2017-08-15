# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student, Professor, Course, Professor_And_Students, Feedback_Theory, Feedback_Lab, Permissions
# Register your models here.
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Professor_And_Students)
admin.site.register(Feedback_Theory)
admin.site.register(Feedback_Lab)
admin.site.register(Permissions)