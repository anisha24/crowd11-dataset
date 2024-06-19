from django import forms
from django.db.models import Count
from videolabel.models import Label

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()

# class MergeLabelsForm(forms.Form):
#     labels_to_merge = forms.ModelMultipleChoiceField(
#         queryset=Label.objects.filter(name__isnull=False).exclude(name='').values_list('name', flat=True).distinct(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True
#     )
#     new_label = forms.CharField(max_length=100, required=True)

class MergeLabelsForm(forms.Form):
    labels_to_merge = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    new_label = forms.CharField(max_length=100, required=True)

    def __init__(self, *args, **kwargs):
        super(MergeLabelsForm, self).__init__(*args, **kwargs)
        
        labels_with_count = Label.objects.filter(name__isnull=False).exclude(name='') \
            .annotate(video_count=Count('videos')).values_list('name', 'video_count') \
            .distinct()

        self.fields['labels_to_merge'].choices = [
            (name, f"{name} ({video_count})") for name, video_count in labels_with_count
        ]