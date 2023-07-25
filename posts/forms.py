from django import forms
from .models import Post

class PostBaseForm(forms.Form):
    CATEGORY_CHOICES =[
        ('1', '일반'),
        ('2', '계정'),

    ]
    image = forms.ImageField(label='이미지')
    content = forms.CharField(label='내용', widget=forms.Textarea, required=True)
    #category = forms.CharField(label='카테고리',widget=forms.Textarea)

class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

#    CATEGORY_CHOICES =[
#        ('1', '일반'),
#        ('2', '계정'),
#
#    ]
#    image = forms.ImageField(label='이미지')
#    content = forms.CharField(label='내용', widget=forms.Textarea, required=True)
#    #category = forms.CharField(label='카테고리',widget=forms.Textarea)    
#
class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields =['image', 'content']
    def clean_content(self):
        data = self.cleaned_data['content']
        if "비속어" == data:
            raise ValidationError("you have forgotten about fred")
        return data

class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields =['image', 'content']

class PostDetailForm(PostBaseForm):
    pass


    