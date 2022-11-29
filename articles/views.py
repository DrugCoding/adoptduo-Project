from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    articles = Article.objects.all()

    article_item = Article.objects.order_by("pk") # pk 순으로 정렬(등록한 것부터)
    paginator = Paginator(article_item, 9) # 정렬을 9개까지 보여줌
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'articles':articles,
        "page_obj": page_obj,
    }
    return render(request, "articles/index.html", context) # 템플릿 네임 적어주고, 이쪽으로 context 값을 넘겨줌



def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES) # 사용자가 요청하여 Productform에 담긴 포스트를 productform 변수에 저장

        if article_form.is_valid():
            article = article_form.save(commit=False) # 저장하기 전에 잠깐 멈추기 위해 commit=false사용
            article.user = request.user # product.user와 요청한 user가 같다를 정의 
            article.save() # 위에 요청 받은 폼을 저장, 값을 만들고 저장하는 용도고 값을 보내줄 것이 없으니까 redirect를 사용
            return redirect('articles:index') # url로 이동시켜줄 뿐(app name:url name) 글작성 후 제출하면 index로 이동
    else: 
        article_form = ArticleForm() # post 요청이 아니면(제출 버튼을 안누르면) 빈 폼을 보여줌

    context = {
        "article_form": article_form # 유효하지 않을 때, 사용자의 인풋을 다 받아서, 검증까지 해서 에러메시지를 저장한 product_form(템플릿 내에서 부트스트랩 폼에 사용)
        # post일 때는 post의 product_form이 여기에 해당 되고, 해당 페이지 접속일 (글생성 x)때는 else의 product_form이 들어감
    }

    return render(request, "articles/form.html", context) # 제출에 이슈가 있다면 값을 보내며 다시 폼으로 돌아가기



def detail(request):
    pass

def update(request):
    pass

def delete(request):
    pass

def dog(request):
    return render(request, "articles/dog.html")

def cat(request):
    return render(request, "articles/cat.html")