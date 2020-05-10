from django import forms
from .models import Comment_in_comment,Comment

class Comment_in_commentForm(forms.ModelForm):
    class Meta:
        model = Comment_in_comment
        fields = ['content']
        labels = {'content':'我来评论'}
        widgets = {'content':forms.Textarea(attrs={'cols':80,'rows':2})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['score','content']
        labels = {'score':'你的评分','content':'输入评论内容'}
        widgets = {'content': forms.Textarea(attrs={'cols': 80, 'rows': 2})}
