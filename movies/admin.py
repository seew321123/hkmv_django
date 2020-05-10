from django.contrib import admin
from movies.models import Movie,Comment,Comment_in_comment,Like_status
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Comment_in_comment)
admin.site.register(Like_status)