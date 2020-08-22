from django import forms
from.models import Course, Tutor
# from cloudinary.forms import CloudinaryJsFileField


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'logo_url', 'description', 'cost', 'devtype')
    # logo = CloudinaryJsFileField()

    
class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ('first_name', 'last_name', 'image_url', 'summary', 'courses')