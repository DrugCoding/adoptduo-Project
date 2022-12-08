from django.shortcuts import render, redirect
from .models import Volunteer, VolunteerComment
from .forms import VolunteerForm, VolunteerCommentForm
from accounts.models import User
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    user = User.objects.all()
    v_articles = Volunteer.objects.order_by('-pk')
    vv_articles = Volunteer.objects.order_by('pk')
    context ={
        'v_articles': v_articles,
        'vv_articles': vv_articles,
        'user':user,
        }
    return render(request, 'volunteers/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        v_form = VolunteerForm(request.POST)
        if v_form.is_valid():
            v_article = v_form.save(commit=False)
            v_article.user = request.user
            v_article.save()
            return redirect('volunteers:index')
    else:
        v_form = VolunteerForm()
    context = {
        'v_form': v_form
    }
    return render(request, 'volunteers/create.html', context)

def detail(request, pk):
    v_article = Volunteer.objects.get(pk=pk)
    v_comment_form = VolunteerCommentForm()
    context = {
        "v_article": v_article,
        "v_comments": v_article.volunteercomment_set.all(),
        "v_comment_form": v_comment_form,
    }
    return render(request, "volunteers/detail.html", context)

@login_required    
def update(request, pk):
    v_article = Volunteer.objects.get(pk=pk)
    if request.method == "POST":
        v_form = VolunteerForm(request.POST, instance=v_article)
        if v_form.is_valid():
            v_form.save()
            return redirect("volunteers:detail", v_article.pk)
    else:
        v_form = VolunteerForm(instance=v_article)
    context = {
        "v_form": v_form,
    }
    return render(request, "volunteers/update.html", context)

def delete(request, pk):
    v_article = Volunteer.objects.get(pk=pk)
    v_article.delete()
    return redirect("volunteers:index")

def comment_create(request, pk):
    v_article = Volunteer.objects.get(pk=pk)
    v_comment_form = VolunteerCommentForm(request.POST)
    if v_comment_form.is_valid():
        v_comment = v_comment_form.save(commit=False)
        v_comment.article = v_article # 게시글은 입력 받은 댓글의 게시글
        v_comment.user = request.user # 로그인한 유저가 댓글작성자(커멘트의 유저)임!
        v_comment.save()
        context = {
            'v_content': v_comment.content,
            'v_userName': v_comment.user.username,
            'v_pk': v_comment.pk,
        }
        return JsonResponse(context)

def comment_delete(request, pk, c_pk):
    v_comment = VolunteerComment.objects.get(pk=c_pk)
    v_comment.delete()
    context = {
        '1': 1
    }
    return JsonResponse(context)

def bookmark(request, pk):
    v_article = Volunteer.objects.get(pk=pk)
    if request.user in v_article.bookmarks.all(): 
        v_article.bookmarks.remove(request.user)
        is_bookmarked = False
    else:
        v_article.bookmarks.add(request.user)
        is_bookmarked = True
    context = {
        'isbookmarked': is_bookmarked,
        'bookmarkcount': v_article.bookmarks.count()
        }
    return JsonResponse(context)