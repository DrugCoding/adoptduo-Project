from django.shortcuts import render, redirect
from .models import DogArticle, CatArticle, DogArticleComment, CatArticleComment, CatCategory, DogCategory
from .forms import DogArticleForm, CatArticleForm, DogCommentForm, CatCommentForm
from stories.models import Stories
from volunteers.models import Volunteer
from accounts.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from accounts.models import User

# Create your views here.

def index(request):
    dog_articles = DogArticle.objects.all()[0:5]
    cat_articles = CatArticle.objects.all()[0:5]
    stor = Stories.objects.all()
    storie = stor.annotate(like_count=Count("like"))
    stories = storie.order_by('-like_count')[0:3]
    vol = Volunteer.objects.all()
    user = User.objects.all()
    context = {
        "dog_articles" : dog_articles,
        "cat_articles" : cat_articles,
        "stories" : stories,
        "vol": vol,
        "user": user,
    }
    return render(request,"articles/index.html", context)

def info_declartation(request):
    return render(request, "articles/info_declartation.html")

def info_adopt(request):
    return render(request, "articles/info_adopt.html")

def information(request):
    return render(request,"articles/information.html")

def introduction(request):
    return render(request,"articles/introduction.html")

def dog_index(request):
    dog_articles = DogArticle.objects.all()

    dog_article_item = DogArticle.objects.order_by("pk") # pk 순으로 정렬(등록한 것부터)
    paginator = Paginator(dog_article_item, 9) # 정렬을 9개까지 보여줌
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'dog_articles':dog_articles,
        "page_obj": page_obj,
    }
    return render(request, "articles/dog.html", context) # 템플릿 네임 적어주고, 이쪽으로 context 값을 넘겨줌

@login_required
def dog_create(request):
    if request.method == "POST":
        dog_article_form = DogArticleForm(request.POST, request.FILES) # 사용자가 요청하여 Productform에 담긴 포스트를 productform 변수에 저장

        if dog_article_form.is_valid():
            dog_article = dog_article_form.save(commit=False) # 저장하기 전에 잠깐 멈추기 위해 commit=false사용
            dog_article.user = request.user # product.user와 요청한 user가 같다를 정의 
            dog_article.save() # 위에 요청 받은 폼을 저장, 값을 만들고 저장하는 용도고 값을 보내줄 것이 없으니까 redirect를 사용
            return redirect('articles:dog_index') # url로 이동시켜줄 뿐(app name:url name) 글작성 후 제출하면 index로 이동
    else: 
        dog_article_form = DogArticleForm() # post 요청이 아니면(제출 버튼을 안누르면) 빈 폼을 보여줌

    context = {
        "dog_article_form": dog_article_form # 유효하지 않을 때, 사용자의 인풋을 다 받아서, 검증까지 해서 에러메시지를 저장한 product_form(템플릿 내에서 부트스트랩 폼에 사용)
        # post일 때는 post의 product_form이 여기에 해당 되고, 해당 페이지 접속일 (글생성 x)때는 else의 product_form이 들어감
    }

    return render(request, "articles/form.html", context) # 제출에 이슈가 있다면 값을 보내며 다시 폼으로 돌아가기



def dog_detail(request, dog_article_pk):
    dog_article = DogArticle.objects.get(id=dog_article_pk)
    dog_comment_form = DogCommentForm()

    context = {
        "dog_article":dog_article,
        'dog_comments': dog_article.dogarticlecomment_set.all(), # 도그 게시물의 모든 댓글 출력하기
        "dog_comment_form":dog_comment_form
    }

    return render(request, "articles/dog_detail.html", context)


@login_required
def dog_update(request, dog_article_pk):
    dog_article = DogArticle.objects.get(id=dog_article_pk)

    if request.method == "POST": # 업데이트 제출 버튼 눌렀을 때
        dog_article_form = DogArticleForm(request.POST, request.FILES, instance=dog_article) # 요청된 포스트와 요청 된 파일, 기존에 모델에 있는 것을 넣어 놓은 것을 요청 된 것으로 바꿈

        if dog_article_form.is_valid(): # 위 폼이 유효하다면
            dog_article_form.save() # 저장

            return redirect("articles:dog_detail", dog_article_pk) # 몇번 상품의 디테일 페이지에 보내줄껀지? 
    else:
        dog_article_form = DogArticleForm(instance=dog_article) # 기존 모델에 저장 되어있는 값을 보여줌

    context = {
        "dog_article_form": dog_article_form # 유효하지 않을 때는 요청 받은 product_form, 제출 안눌렀을 때는 바로위의 폼
    }

    return render(request, "articles/form.html", context) # 유효하지 않을 때나, 제출 안눌렀을 때는 위의 컨텍스트 값을 가져와서 forms.html을 보여줌
    


def dog_delete(request, dog_article_pk):

    dog_article = DogArticle.objects.get(id=dog_article_pk)
    dog_article.delete()

    return redirect("articles:dog_index")



def cat_index(request):
    cat_articles = CatArticle.objects.all()
    form = CatArticleForm()

    cat_article_item = CatArticle.objects.order_by("pk") # pk 순으로 정렬(등록한 것부터)
    paginator = Paginator(cat_article_item, 9) # 정렬을 9개까지 보여줌
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'cat_articles':cat_articles,
        "page_obj": page_obj,
        'form':form
    }
    return render(request, "articles/cat.html", context) # 템플릿 네임 적어주고, 이쪽으로 context 값을 넘겨줌



def cat_create(request):
    if request.method == "POST":
        cat_article_form = CatArticleForm(request.POST, request.FILES) # 사용자가 요청하여 Productform에 담긴 포스트를 productform 변수에 저장

        if cat_article_form.is_valid():
            cat_article = cat_article_form.save(commit=False) # 저장하기 전에 잠깐 멈추기 위해 commit=false사용
            cat_article.user = request.user # product.user와 요청한 user가 같다를 정의 
            cat_article.save() # 위에 요청 받은 폼을 저장, 값을 만들고 저장하는 용도고 값을 보내줄 것이 없으니까 redirect를 사용
            return redirect('articles:cat_index') # url로 이동시켜줄 뿐(app name:url name) 글작성 후 제출하면 index로 이동
    else: 
        cat_article_form = CatArticleForm() # post 요청이 아니면(제출 버튼을 안누르면) 빈 폼을 보여줌

    context = {
        "cat_article_form": cat_article_form # 유효하지 않을 때, 사용자의 인풋을 다 받아서, 검증까지 해서 에러메시지를 저장한 product_form(템플릿 내에서 부트스트랩 폼에 사용)
        # post일 때는 post의 product_form이 여기에 해당 되고, 해당 페이지 접속일 (글생성 x)때는 else의 product_form이 들어감
    }

    return render(request, "articles/catform.html", context) # 제출에 이슈가 있다면 값을 보내며 다시 폼으로 돌아가기


def cat_detail(request, cat_article_pk):
    cat_article = CatArticle.objects.get(id=cat_article_pk)
    cat_comment_form = CatCommentForm()

    context = {
        "cat_article":cat_article,
        'cat_comments': cat_article.catarticlecomment_set.all(), # 도그 게시물의 모든 댓글 출력하기
        "cat_comment_form":cat_comment_form
    }

    return render(request, "articles/cat_detail.html", context)


def cat_update(request, cat_article_pk):
    cat_article = CatArticle.objects.get(id=cat_article_pk)

    if request.method == "POST": # 업데이트 제출 버튼 눌렀을 때
        cat_article_form = CatArticleForm(request.POST, request.FILES, instance=cat_article) # 요청된 포스트와 요청 된 파일, 기존에 모델에 있는 것을 넣어 놓은 것을 요청 된 것으로 바꿈

        if cat_article_form.is_valid(): # 위 폼이 유효하다면
            cat_article_form.save() # 저장

            return redirect("articles:cat_detail", cat_article_pk) # 몇번 상품의 디테일 페이지에 보내줄껀지? 
    else:
        cat_article_form = CatArticleForm(instance=cat_article) # 기존 모델에 저장 되어있는 값을 보여줌

    context = {
        "cat_article_form": cat_article_form # 유효하지 않을 때는 요청 받은 product_form, 제출 안눌렀을 때는 바로위의 폼
    }

    return render(request, "articles/catform.html", context) # 유효하지 않을 때나, 제출 안눌렀을 때는 위의 컨텍스트 값을 가져와서 forms.html을 보여줌


def cat_delete(request, cat_article_pk):

    cat_article = CatArticle.objects.get(id=cat_article_pk)
    cat_article.delete()

    return redirect("articles:cat_index")



def dog_comment_create(request, dog_article_pk):

    dog_article = DogArticle.objects.get(pk=dog_article_pk)
    dog_comment_form = DogCommentForm(request.POST)
    if dog_comment_form.is_valid():
        dog_comment = dog_comment_form.save(commit=False)
        dog_comment.dogarticle = dog_article # 게시글은 입력 받은 댓글의 게시글
        dog_comment.user = request.user # 로그인한 유저가 댓글작성자(커멘트의 유저)임!
        dog_comment.save()
        context = {
            'dog_content': dog_comment.content,
            'dog_userName': dog_comment.user.username,
            'dog_pk':dog_comment.pk,
        }
        return JsonResponse(context)


def cat_comment_create(request, cat_article_pk):
    cat_article = CatArticle.objects.get(pk=cat_article_pk)
    cat_comment_form = CatCommentForm(request.POST)
    if cat_comment_form.is_valid():
        cat_comment = cat_comment_form.save(commit=False)
        cat_comment.catarticle = cat_article
        cat_comment.user = request.user
        cat_comment.save()
        context = {
            'cat_content': cat_comment.content,
            'cat_userName': cat_comment.user.username,
            'cat_pk':cat_comment.pk,
        }
        
    return JsonResponse(context)



def dog_comments_delete(request, dog_article_pk, dog_comment_pk):
    dog_comment = DogArticleComment.objects.get(pk=dog_comment_pk)
    dog_comment.delete()
    context = {
        '1': 1
    }
    return JsonResponse(context)




def cat_comments_delete(request, cat_article_pk, cat_comment_pk):
    cat_comment = CatArticleComment.objects.get(pk=cat_comment_pk)
    cat_comment.delete()
    context = {
        '1': 1
    }
    return JsonResponse(context)


def dog_bookmark(request, dog_article_pk):
    dog_article = DogArticle.objects.get(pk=dog_article_pk)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in dog_article.bookmarks.all(): 
        # 좋아요 삭제하고
        dog_article.bookmarks.remove(request.user)
        is_bookmarked = False
    else:
        # 좋아요 추가하고 
        dog_article.bookmarks.add(request.user)
        is_bookmarked = True 
    context = {
        'isbookmarked' : is_bookmarked,
        'bookmarkcount': dog_article.bookmarks.count()
    }
    return JsonResponse(context)
    # 상세 페이지로 redirect



def cat_bookmark(request, cat_article_pk):
    cat_article = CatArticle.objects.get(pk=cat_article_pk)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in cat_article.bookmarks.all(): 
        # 좋아요 삭제하고
        cat_article.bookmarks.remove(request.user)
        is_bookmarked = False
    else:
        # 좋아요 추가하고 
        cat_article.bookmarks.add(request.user)
        is_bookmarked = True 
    context = {
        'isbookmarked' : is_bookmarked,
        'bookmarkcount': cat_article.bookmarks.count()
    }
    return JsonResponse(context)
    # 상세 페이지로 redirect



def cat_category(request, cat_category_pk):
    category = CatCategory.objects.get(pk=cat_category_pk)
    category_articles = (
        CatArticle.objects.filter(cat_breed=category)
    )
    context = {
        "category": category, 
        "category_articles": category_articles
        }
    return render(request, "articles/cat.html", context)



def dog_category(request, dog_category_pk):
    category = DogCategory.objects.get(pk=dog_category_pk)
    category_articles = (
        DogArticle.objects.filter(dog_breed=category)
    )
    context = {
        "category": category, 
        "category_articles": category_articles
        }
    return render(request, "articles/dog.html", context) 
    



# 검색
def search(request):
    query = None
    dogs = None
    cats = None
    stories = None
    if 'searchs' in request.GET:
        query = request.GET.get('searchs')
        dogs = DogArticle.objects.all().filter(
            Q(breed__icontains=query)
        )
        cats = CatArticle.objects.all().filter(
            Q(breed__icontains=query)
        )
        stories = Stories.objects.all().filter(
            Q(breed__icontains=query)|
            Q(content__icontains=query)
        )
        # # 조회수 최다 강아지 분양글
        # most_dog = DogArticle.objects.order_by('-hits')[:4]
        # # 조회수 최다 고양이 분양글
        # most_cat = CatArticle.objects.order_by('-hits')[:4]
        # # 좋아요 최다 잡담글
        # most_like = Stories.objects.order_by('-hits')[:4]
    context = {
        'query': query,
        'dogs': dogs,
        'cats': cats,
        'stories': stories,
    #     'most_dog': most_dog,
    #     'most_cat': most_cat,
    #     'most_like': most_like
    }
    return render(request, 'articles/search.html', context)

