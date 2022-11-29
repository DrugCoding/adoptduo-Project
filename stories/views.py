from django.shortcuts import render, get_object_or_404, redirect
from .models import Stories, StoryComment
from .forms import StoriesForm, Stories_CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    stories = Stories.objects.order_by("-pk")
    context = {
        "stories": stories,
    }
    return render(request, "stories/index.html", context)

@login_required
def create(request):
    if request.method == "POST":
        form = StoriesForm(request.POST, request.FILES)
        if form.is_valid():
            stories = form.save(commit=False)
            stories.user = request.user
            stories.save()
            return redirect("stories:index")
    else:
        form = StoriesForm()
    context = {
        "form": form
    }
    return render(request, "stories/create.html", context)

def detail(request, pk):
    stories = get_object_or_404(Stories, pk=pk)
    comment_form = Stories_CommentForm()
    context = {
        "stories": stories,
        "comments": stories.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "stories/detail.html", context)

@login_required
def update(request, pk):
    stories = get_object_or_404(Stories, pk=pk)
    if request.method == "POST":
        stories_form = StoriesForm(request.POST, request.FILES)
        if stories_form.is_valid():
            stories_form.save()
            return redirect("stories:detail", pk)
    else:
        stories_form = StoriesForm(instance=stories)
    context = {
        "stories_form": stories_form,
    }
    return render(request, "stories/update.html", context)

@login_required
def delete(request, pk):
    Stories.objects.get(pk=pk).delete()
    return redirect("stories:index")