"""from django import forms
from .models import Worklogs
  
  
# creating a form
class SampleForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = Worklogs
  
        # specify fields to be used
        fields = [
            "task_id",
            "details_of_execution",
        ]"""



from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomeUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"