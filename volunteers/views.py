from django.shortcuts import render, redirect
from .models import Volunteer, VolunteerComment
from .forms import VolunteerForm, VolunteerCommentForm

# Create your views here.

def index(request):
    v_articles = Volunteer.objects.order_by('-pk')
    context ={'v_articles': v_articles}
    return render(request, 'volunteers/index.html', context)

def create(request):
    if request.method == 'POST':
        v_form = VolunteerForm(request.POST)
        if v_form.is_valid():
            v_form = v_form.save(commit=False)
            v_form.user = request.user
            v_form.save()
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
        'v_comments': v_article.volunteercomment_set.all(),
        "v_comment_form": v_comment_form
    }
    return render(request, "volunteers/detail.html", context)
    
def update(request):
    pass

def delete(request, pk):
    v_article = Volunteer.objects.get(pk=pk)
    v_article.delete()
    return redirect("volunteers:index")

def create_comment(request):
    pass

def delete_comment(request):
    # v_article = Volunteer.objects.get(pk)
    # v_article.delete()
    # return redirect("volunteers:index")
    pass

def bookmark(request):
    pass