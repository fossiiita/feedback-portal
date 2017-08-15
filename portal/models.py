# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.
class Student(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	semester = models.IntegerField()

	def __str__(self):
		return self.user.username

class Professor(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	dean_or_director = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

class Course(models.Model):
	name = models.CharField(max_length=200)
	code = models.CharField(max_length=100)
	assigned_to_professor = models.ManyToManyField(Professor)
	students_of_course = models.ManyToManyField(Student)
	is_course_lab = models.BooleanField(default=False)

	def __str__(self):
		return self.name
class Professor_And_Students(models.Model):
	course_name = models.ForeignKey(Course)
	professor = models.ForeignKey(Professor)
	students = models.ManyToManyField(Student)

	def __str__(self):
		return self.course_name.name + ' - ' + self.professor.user.username

class Feedback_Theory(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	student = models.ForeignKey(Professor_And_Students)
	mcq_1 = models.IntegerField()
	mcq_2 = models.IntegerField()
	mcq_3 = models.IntegerField()
	textual_question_1 = models.CharField(max_length=500)
	textual_question_2 = models.CharField(max_length=500)
	feedback_given_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.student.course_name.name + ' - ' + self.student.professor.user.username

class Feedback_Lab(models.Model):
	student = models.ForeignKey(Professor_And_Students)
	mcq_1 = models.IntegerField()
	mcq_2 = models.IntegerField()
	mcq_3 = models.IntegerField()
	textual_question_1 = models.CharField(max_length=500)
	textual_question_2 = models.CharField(max_length=600)
	feedback_given_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.student.course_name.name + ' - ' + self.student.professor.user.username

class Permissions(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	dean_or_director = models.BooleanField(default=False)

	class Meta:
		permissions = (("can_view_superview", "can view superview"),
			("can_view_normalview", "can view normalview"),
			)
	def __str__(self):
		return self.user.username					