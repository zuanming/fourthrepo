from django import forms
from .models import Question, Answer
from courses.models import Course

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'content','course')

    
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content',)