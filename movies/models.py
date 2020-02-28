from django.db import models
from django.contrib.auth.models import User
from django.core import serializers

class Movie(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    detail = models.TextField()
    img_url = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    star = models.CharField(max_length=50)
    imdb_score = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Comment(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    score = models.CharField(max_length=50,choices=(('1','1分'),('2','2分'),('3','3分'),('4','4分'),('5','5分'),('6','6分'),('7','7分'),('8','8分'),('9','9分'),('10','10分')))
    content = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    like_num = models.IntegerField(default='0')

class Comment_in_comment(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    content = models.TextField()
    owner = models.CharField(max_length=50)

class Like_status(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    like_status = models.CharField(max_length=50,choices=(('1','赞'),('2','不赞')),default="不赞")
    owner = models.ForeignKey(User,on_delete=models.CASCADE)



