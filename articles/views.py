from django.shortcuts import render, redirect
from .models import DogArticle, CatArticle
from .forms import DogArticleForm, CatArticleForm
from stories.models import Stories
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    dog_articles = DogArticle.objects.all()[0:4]
    cat_articles = CatArticle.objects.all()[0:4]
    stories = Stories.objects.order_by("-hits")[0:1]
    story = Stories.objects.order_by("-hits")[1:3]
    context = {
        "dog_articles" : dog_articles,
        "cat_articles" : cat_articles,
        "stories" : stories,
        "story" : story,
    }
    return render(request,"articles/index.html", context)

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

    context = {
        "dog_article":dog_article
    }

    return render(request, "articles/dog_detail.html", context)



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

    return render(request, "products/forms.html", context) # 유효하지 않을 때나, 제출 안눌렀을 때는 위의 컨텍스트 값을 가져와서 forms.html을 보여줌
    

def dog_delete(request):
    pass

def cat_index(request):
    cat_articles = CatArticle.objects.all()

    cat_article_item = CatArticle.objects.order_by("pk") # pk 순으로 정렬(등록한 것부터)
    paginator = Paginator(cat_article_item, 9) # 정렬을 9개까지 보여줌
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'cat_articles':cat_articles,
        "page_obj": page_obj,
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