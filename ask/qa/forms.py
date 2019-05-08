from django import forms
from qa.models import Question, Answer

class AskForm (forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)

	def clean():
		pass

	def save():
		question = Question(**self.cleaned_data)
		question.save()
		return question

class AnswerForm (forms.Form):
	question = forms.IntegerField(widget=forms.HiddenInput)
	text = forms.CharField(widget=forms.Textarea)

	def clean():
		pass

	def save():
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer

