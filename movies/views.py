from django.shortcuts import render
from .models import Movie,Comment,Comment_in_comment,Like_status
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .form import Comment_in_commentForm,CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
def movies(request):
    movies = Movie.objects.order_by('date_added')
    top10_movies =Movie.objects.order_by('-date_added')[:10]
    paginator = Paginator(movies, 10)
    page = request.GET.get("page", 1)
    currentPage = int(page)
    try:
        movie_list = paginator.page(currentPage)
    except PageNotAnInteger:
        movie_list = paginator.page(1)
    except EmptyPage:
        movie_list = paginator.page(1)
    context = {'movies':movies,'currentPage':currentPage,'movie_list':movie_list,'paginator':paginator,'top10_movies':top10_movies}
    return render(request,'movies/movies.html',context)

@login_required
def search_movie(request):
    kw = request.POST.get('movie_search')
    movies = Movie.objects.filter(name__contains=kw).order_by('date_added')
    top10_movies = Movie.objects.order_by('-date_added')[:10]
    paginator = Paginator(movies, 10)
    page = request.GET.get("page", 1)
    currentPage = int(page)
    try:
        movie_list = paginator.page(currentPage)
    except PageNotAnInteger:
        movie_list = paginator.page(1)
    except EmptyPage:
        movie_list = paginator.page(1)
    context = {'movies': movies, 'currentPage': currentPage, 'movie_list': movie_list, 'paginator': paginator,
               'top10_movies': top10_movies}
    return render(request, 'movies/movies.html', context)

@login_required
def comment(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    top10_movies =Movie.objects.order_by('-date_added')[:10]
    comments = Comment.objects.filter(movie=movie).order_by('-date_added')
    paginator = Paginator(comments,10)
    page = request.GET.get("page", 1)
    currentPage = int(page)
    try:
        comment_list = paginator.page(currentPage)
    except PageNotAnInteger:
        comment_list = paginator.page(1)
    except EmptyPage:
        comment_list = paginator.page(1)
    form_comment_in_comment = Comment_in_commentForm()
    context = {'movie':movie,'comments':comments,'top10_movies':top10_movies,'form_comment_in_comment':form_comment_in_comment,'comment_list':comment_list,'paginator':paginator}
    return render(request,'movies/comment.html',context)

@login_required
def add_comment(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    top10_movies = Movie.objects.order_by('-date_added')[:10]
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner = request.user
            new_comment.movie = movie
            new_comment.save()
            return HttpResponseRedirect(reverse('movies:comment',args=[movie_id]))
    context = {'movie':movie,'form':form,'top10_movies':top10_movies}
    return render(request,'movies/add_comment.html',context)

@login_required
def ajax_test(request,comment_id):
    comment = Comment.objects.get(id = comment_id)
    comment_in_comment = Comment_in_comment.objects.filter(comment = comment).order_by('date_added')
    data = serializers.serialize("json", comment_in_comment,fields=('content','owner'))
    return HttpResponse(data)

@login_required
def add_comment_in_comment(request,comment_id):
    form = Comment_in_commentForm(request.POST)
    comment = Comment.objects.get(id=comment_id)
    moviename = comment.movie
    movie = Movie.objects.get(name=moviename)
    if form.is_valid():
        new_comment_in_comment = form.save(commit=False)
        new_comment_in_comment.owner = request.user
        new_comment_in_comment.comment = comment
        new_comment_in_comment.save()
        return HttpResponseRedirect(reverse('movies:comment',args=[movie.id]))
    return HttpResponse(None)

@login_required
def user_center(request):
    user = request.user
    comment = Comment.objects.filter(owner=user).order_by('-date_added')
    comment_in_comment = Comment_in_comment.objects.filter(owner=user).order_by('-date_added')
    context = {'comment':comment,'comment_in_comment':comment_in_comment}
    return render(request,'movies/user_center.html',context)

@login_required
def edit_comment(request,comment_id):
    top10_movies = Movie.objects.order_by('-date_added')[:10]
    comment = Comment.objects.get(id=comment_id)
    movie = comment.movie
    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment,data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.owner = request.user
            new_comment.movie = movie
            new_comment.save()
            return HttpResponseRedirect(reverse('movies:user_center'))
    context = {'comment':comment,'movie':movie,'form':form,'top10_movies':top10_movies}
    return render(request,'movies/edit_comment.html',context)

@login_required
def delete_comment(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse('movies:user_center'))

@login_required
def like(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    user = request.user
    like_num = comment.like_num
    try:
        like_status = Like_status.objects.get(owner=user, comment=comment)
    except(BaseException):
        like_status = Like_status.objects.create(owner=user,comment=comment,like_status='不赞')
    if like_status.like_status == '赞':
        Like_status.objects.filter(owner=user,comment=comment).update(like_status='不赞')
        Comment.objects.filter(id=comment_id).update(like_num=like_num - 1)
        like_num -= 1
        LS = '不赞'
    else:
        Like_status.objects.filter(owner=user,comment=comment).update(like_status='赞')
        Comment.objects.filter(id=comment_id).update(like_num=like_num + 1)
        like_num += 1
        LS = '赞'
    data = {}
    data['like_num'] = like_num
    data['like_status'] = LS
    return JsonResponse(data)

@login_required
def refresh(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    user = request.user
    try:
        like_status = Like_status.objects.get(owner=user, comment=comment)
    except(BaseException):
        like_status = Like_status.objects.create(owner=user, comment=comment, like_status='不赞')
    if like_status.like_status == '赞':
        current_status = '赞'
    else:
        current_status = '不赞'
    return HttpResponse(current_status)



