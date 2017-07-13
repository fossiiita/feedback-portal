# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from forms import Feedback_Theoryform
# Create your views here.
def home(request):
	return render(request, 'portal/home.html', {})

#def student(request):
#	return render(request, 'portal/student_view.html', {})

def fill(request):
		if request.method == "POST":
			form = Feedback_Theoryform(request.POST)
			if form.is_valid():
				detail = form.save(commit=False)
				detail.user = request.user
				detail.save()
				return HttpResponse("done")
		else:	
			form = Feedback_Theoryform()
			return render(request, 'portal/student_view.html', {"form":form})