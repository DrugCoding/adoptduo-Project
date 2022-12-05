from django.shortcuts import render
from .models import Notes
# Create your views here.

def index(request):
    notes = request.user.user_to.order_by("-created_at") # 요청자의 받은 쪽지함 
    to_notes = request.user.user_from.order_by("-created_at") # 요청자의 보낸 쪽지함
    context = {
        "notes": notes,
        "to_notes": to_notes
    }

    return render(request, "notes/index.html", context)


def send(request, pk):
    to_user = Notes.objects.get( pk=pk)
    form = NotesForm(request.POST or None)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.from_user = request.user
        temp.to_user = to_user
        temp.save()
        if to_user.note_notice:
            to_user.notice_note = False
            to_user.save()
        messages.success(request, "쪽지 전송 완료.😀")
        return redirect("meetings:index")
    context = {
        "form": form,
        "to_user": to_user,
    }
    return render(request, "notes/send.html", context)

       