from django.shortcuts import render, redirect
from .models import Notes
from .form import NotesForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    notes = request.user.user_to.order_by("-created_at") #사용자의 받은쪽지들을 최신순으로 
    to_notes = request.user.user_from.order_by("-created_at") # 사용자의 보낸쪽지들 최신순으로
    context = {
        "notes": notes,
        "to_notes": to_notes
    }

    return render(request, "notes/index.html", context)


def send(request, pk): # 보내는 로직
    to_user = get_user_model().objects.get(pk=pk)
    form = NotesForm(request.POST or None)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.from_user = request.user # 요청자가 작성한 모델폼의 보낸사람을 사용자로
        temp.to_user = to_user # 요청자가 작성한 모델폼의 받은 사람을 선택한 사람으로 정의 
        temp.save()
        messages.success(request, "쪽지 전송 완료.😀")
        return redirect("notes:index")
    context = {
        "form": form,
        "to_user": to_user,
    }
    return render(request, "notes/send.html", context)


def detail(request, pk):
    note = Notes.objects.get(pk=pk)
    notes = request.user.user_to.all() # 사용자의 받은 쪽지들 모두
    to_notes = request.user.user_from.all() # 사용자의 보낸 쪽지들 모두
    if request.user == note.to_user: # 요청사용자가 받는사람이라면
        if not note.read: # 읽지 않았다면
            note.read = True # 읽음 처리하고 
            note.save() # 저장
        context = {
            'note': note,
        }
        return render(request, "notes/detail.html", context)
    elif request.user == note.from_user: # 사용자가 보낸 사람이라면
        context = {
            'note': note,
        }
        return render(request, "notes/detail.html", context)
    else:
        messages.error(request, "잘못 된 경로입니다.")
        return redirect("notes:index")







       