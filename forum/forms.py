from django import forms
from .models import Question, Answer
from courses.models import Course
from django.db.models import Q

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'content','course')

    
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content',)


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    course = forms.ModelChoiceField(queryset=Course.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['course'].empty_label = "All Courses"