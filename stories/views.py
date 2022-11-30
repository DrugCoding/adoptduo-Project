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
        "comment_form": comment_form,
        "comments": stories.storycomment_set.all(),
    }
    stories.hits +=1
    stories.save()
    return render(request, "stories/detail.html", context)

@login_required
def update(request, pk):
    stories = get_object_or_404(Stories, pk=pk)
    if request.user == stories.user:
        if request.method == "POST":
            stories_form = StoriesForm(request.POST, request.FILES, instance=stories)
            if stories_form.is_valid():
                stories_form.save()
                return redirect("stories:detail", stories.pk)
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

@login_required
def comment_create(request, pk):
    stories = get_object_or_404(Stories, pk=pk)
    comment_form = Stories_CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.stories = stories
        comment.user = request.user
        comment.save()
    return redirect('stories:detail', stories.pk)

@login_required
def comment_delete(request, pk, storycomment_pk):
    comment = StoryComment.objects.get(pk=storycomment_pk)
    if request.user == comment.user:
        comment.delete()
        return redirect("stories:detail", pk)
    
@login_required
def likes(request, stories_pk):
    stories=get_object_or_404(Stories, pk=stories_pk)
    if request.user in stories.like.all():
        stories.like.remove(request.user)
    else:
        stories.like.add(request.user)
    return redirect("stories:detail", stories_pk)