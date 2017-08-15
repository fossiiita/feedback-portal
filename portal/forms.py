from django import forms
from models import Feedback_Theory

class Feedback_Theoryform(forms.ModelForm):

	class Meta:
		model = Feedback_Theory
		exclude = ['feedback_given_at','user']