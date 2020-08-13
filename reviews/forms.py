from django import forms
from.models import Review, Comment
from courses.models import Course

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'course')

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
