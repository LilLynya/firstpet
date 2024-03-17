from django import forms
from django.contrib.auth import get_user_model

from workspace.models import Teams, Tasks


class AddGroup(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['team', 'role']


class CreateGroup(forms.ModelForm):
    group = forms.CharField(required=True)
    role = forms.CharField(required=True)
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'input-file'}), required=False)

    class Meta:
        model = Teams
        fields = ['title', 'group', 'bio', 'image', 'role']
        labels = {
            'title': 'Name your group',
            'group': 'Enter id of your group',
            'bio': 'Enter any information about your team',
            'role': 'Enter your role',
            'image': 'Add a photo of Company',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4,
                                         'cols': 40,
                                         }),
        }

    def clean_group(self):
        user_group = self.cleaned_data['group']
        if get_user_model().objects.get(group=user_group).exists():
            raise forms.ValidationError("Sorry, this group already exists")
        else:
            return user_group


class MakeTask(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        group_id = kwargs.pop('group_id', None)
        super(MakeTask, self).__init__(*args, **kwargs)
        query_set = get_user_model().objects.filter(team=group_id)
        choices_from_db = [(obj.role, obj.first_name) for obj in query_set]
        self.fields['to'].choices = choices_from_db

    tasks = forms.CharField(max_length=100000, widget=forms.Textarea(attrs={'cols': 40}))
    to = forms.MultipleChoiceField(required=True)
    # to = forms.CharField(widget=forms.TextInput(attrs={'id': 'carsList', 'type': 'text'}))
    begins = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    ends = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Tasks
        fields = ['tasks', 'to', 'begins', 'ends']
        labels = {
            'tasks': 'Put your task here',
            'to': 'Choose ',
            'begins': 'Begins at:',
            'ends': 'Ends at',
        }