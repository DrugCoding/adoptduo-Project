# 😻입양해듀오😻

> 배포주소: http://adoptduo-env.eba-mwfvzn6n.ap-northeast-2.elasticbeanstalk.com/
> 
> 반려동물들의 무료,분양 입양을 위한 커뮤니티 사이트 

- `개발 기간` : **2022/11/23 ~ 2022/12/14**
- [기획서](https://www.notion.so/b5cd1dea198f4b8e8ea5bb972e7a275f)

## 목차

- [Contributors](https://www.notion.so/5938324146a442e2a5658433d114145c)
- [기술 스택](https://github.com/sunbongE/PARA#-%EA%B8%B0%EC%88%A0-%EC%8A%A4%ED%83%9D)
- [**Role**](https://www.notion.so/5938324146a442e2a5658433d114145c)
- [**주요 기능**](https://www.notion.so/5938324146a442e2a5658433d114145c)
- [페이지 구성 상세](https://www.notion.so/5938324146a442e2a5658433d114145c)
  - [main.html](https://github.com/sunbongE/PARA#mainhtml)
  - [Accounts App](https://github.com/sunbongE/PARA#accounts-app)
    - [accounts/signup.html](https://github.com/sunbongE/PARA#accountssignuphtml)
    - [accounts/login.html](https://github.com/sunbongE/PARA#accountsloginhtml)
    - [accounts/index.html](https://github.com/sunbongE/PARA#accountsindexhtml)
    - [accounts/detail.html](https://github.com/sunbongE/PARA#accountsdetailhtml)
    - [채널톡 API](https://github.com/sunbongE/PARA#%EC%B1%84%EB%84%90%ED%86%A1-api)
  - [Products App](https://github.com/sunbongE/PARA#products-app)
    - [products/index.html](https://github.com/sunbongE/PARA#productsindexhtml)
    - [products/detail.html](https://github.com/sunbongE/PARA#productsdetailhtml)
  - [Cart App](https://github.com/sunbongE/PARA#cart-app)
    - [cart/detail.html](https://github.com/sunbongE/PARA#cartdetailhtml)
  - [Reviews App](https://github.com/sunbongE/PARA#reviews-app)
    - [reviews/detail.html](https://github.com/sunbongE/PARA#reviewsdetailhtml)
    - [taggit](https://github.com/sunbongE/PARA#taggit)
  - [Navbar](https://github.com/sunbongE/PARA#navbar)
    - [Profile](https://github.com/sunbongE/PARA#profile)
    - [매장 찾기](https://github.com/sunbongE/PARA#%EB%A7%A4%EC%9E%A5-%EC%B0%BE%EA%B8%B0)
    - [searched.html](https://github.com/sunbongE/PARA#searchedhtml)
    - [bestseller.html](https://github.com/sunbongE/PARA#bestsellerhtml)
    - [category.html](https://github.com/sunbongE/PARA#categoryhtml)
  - [모바일 화면](https://github.com/sunbongE/PARA#%EB%AA%A8%EB%B0%94%EC%9D%BC-%ED%99%94%EB%A9%B4)
- [후기](https://github.com/sunbongE/PARA#%ED%9B%84%EA%B8%B0)

## **Contributors**

서민수

[TocDX - Overview](https://github.com/TocDX/)

이종은

[leejongeun2 - Overview](https://github.com/leejongeun2)

이주현

[rrwe23 - Overview](https://github.com/rrwe23)

이동희

[kklee0930 - Overview](https://github.com/kklee0930)

김교민

[kyominkim1074 - Overview](https://github.com/kyominkim1074)

현지수

[hjs721 - Overview](https://github.com/hjs721)

이현성

[DrugCoding - Overview](https://github.com/DrugCoding)

## ⚙️ 기술 스택

[https://camo.githubusercontent.com/eb9413689227f409afd6165229fbf16997dc36373cb98b1146e00fbe8e7a7515/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a71756572792d3037363941443f7374796c653d666f722d7468652d6261646765266c6f676f3d6a7175657279266c6f676f436f6c6f723d7768697465](https://camo.githubusercontent.com/eb9413689227f409afd6165229fbf16997dc36373cb98b1146e00fbe8e7a7515/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a71756572792d3037363941443f7374796c653d666f722d7468652d6261646765266c6f676f3d6a7175657279266c6f676f436f6c6f723d7768697465)

[https://camo.githubusercontent.com/0bd3e302b95d01634f16c7337e721f82fab79aa760aad4a991118d1291fe7329/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6373732d3135373242363f7374796c653d666f722d7468652d6261646765266c6f676f3d43737333266c6f676f436f6c6f723d7768697465](https://camo.githubusercontent.com/0bd3e302b95d01634f16c7337e721f82fab79aa760aad4a991118d1291fe7329/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6373732d3135373242363f7374796c653d666f722d7468652d6261646765266c6f676f3d43737333266c6f676f436f6c6f723d7768697465)

[https://camo.githubusercontent.com/b310667470594171440f9b80f624787ea58555296d88af177788509b0d73a40b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d2532333037343035652e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d7768697465](https://camo.githubusercontent.com/b310667470594171440f9b80f624787ea58555296d88af177788509b0d73a40b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d2532333037343035652e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d7768697465)

[https://camo.githubusercontent.com/e6f0ce6b8ea91992107c852e6b014c1bebfdf8edf67f74e1390394e6d2175b5e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f626f6f7473747261702d3739353242333f7374796c653d666f722d7468652d6261646765266c6f676f3d626f6f747374726170266c6f676f436f6c6f723d7768697465](https://camo.githubusercontent.com/e6f0ce6b8ea91992107c852e6b014c1bebfdf8edf67f74e1390394e6d2175b5e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f626f6f7473747261702d3739353242333f7374796c653d666f722d7468652d6261646765266c6f676f3d626f6f747374726170266c6f676f436f6c6f723d7768697465)

[https://camo.githubusercontent.com/a5e1ddccdf420052ea5f249bf3d43e2dbb1508d4cace7d93936bbb4a7021267d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465](https://camo.githubusercontent.com/a5e1ddccdf420052ea5f249bf3d43e2dbb1508d4cace7d93936bbb4a7021267d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465)

[https://camo.githubusercontent.com/d2e026b8e28bcd20528799e47f958d2a8129f251a29f17613f02e6da213857a3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a6176617363726970742d4637444631453f7374796c653d666f722d7468652d6261646765266c6f676f3d4a617661536372697074266c6f676f436f6c6f723d626c61636b](https://camo.githubusercontent.com/d2e026b8e28bcd20528799e47f958d2a8129f251a29f17613f02e6da213857a3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a6176617363726970742d4637444631453f7374796c653d666f722d7468652d6261646765266c6f676f3d4a617661536372697074266c6f676f436f6c6f723d626c61636b)

[https://camo.githubusercontent.com/fc9ff8bc1cfcfa39ec16f40144c45020eab49f2acb25e93804a915668d64fdc5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f68746d6c352d4533344632363f7374796c653d666f722d7468652d6261646765266c6f676f3d48746d6c35266c6f676f436f6c6f723d7768697465](https://camo.githubusercontent.com/fc9ff8bc1cfcfa39ec16f40144c45020eab49f2acb25e93804a915668d64fdc5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f68746d6c352d4533344632363f7374796c653d666f722d7468652d6261646765266c6f676f3d48746d6c35266c6f676f436f6c6f723d7768697465)

[https://camo.githubusercontent.com/32efbd6e3da90d5ed88b31634adb3b068d706e3882900bdbccaae25866e1ef74/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d677265656e](https://camo.githubusercontent.com/32efbd6e3da90d5ed88b31634adb3b068d706e3882900bdbccaae25866e1ef74/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d677265656e)

[https://camo.githubusercontent.com/d295ea394da88d43d21e31a52fd4b09f37d35cbccfb3500fdf2bf7c530458e3e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f616d617a6f6e6177732d3233324633453f7374796c653d666f722d7468652d6261646765266c6f676f3d616d617a6f6e617773266c6f676f436f6c6f723d79656c6c6f77](https://camo.githubusercontent.com/d295ea394da88d43d21e31a52fd4b09f37d35cbccfb3500fdf2bf7c530458e3e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f616d617a6f6e6177732d3233324633453f7374796c653d666f722d7468652d6261646765266c6f676f3d616d617a6f6e617773266c6f676f436f6c6f723d79656c6c6f77)

[https://camo.githubusercontent.com/a9a95986631c3d4945a63d42d2864e3918a834d672d907e174a29f743a1bc3f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d676974266c6f676f436f6c6f723d7768697465](https://camo.githubusercontent.com/a9a95986631c3d4945a63d42d2864e3918a834d672d907e174a29f743a1bc3f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d676974266c6f676f436f6c6f723d7768697465)

## Role

| 이름  | 역할        |
| --- | --------- |
| 이주현 | 팀장(FE)    |
| 서민수 | 프론트엔드(FE) |
| 이동희 | 프론트엔드(FE) |
| 현지수 | 프론트엔드(FE) |
| 김교민 | 백엔드(BE)   |
| 이현성 | 백엔드(BE)   |
| 이종은 | 백엔드(BE)   |

## 주요 기능

- 게시글 검색 : 입력된 키워드, 단어가 포함된 게시물을 모아서 보여주는 기능입니다.
- 즐겨찾기한 게시글 출력 : 북마크한 게시글을 출력합니다.
- 팔로우 및 언팔로우 : 이용자 팔로우 및 팔로우 취소 기능을 제공합니다.
- 게시글에 댓글 작성 : 게시글에 대한 댓글 작성 및 삭제 기능을 제공합니다.
- 게시글 즐겨찾기 : 게시글 북마크 및 북마크 취소 기능을 제공합니다.
- 쪽지 보내기 및 팔로우 : 이용자에게 개인 메시지 및 팔로우 기능을 제공합니다.
- 위치 서비스 제공 : 지도 api를 활용하여 입양위치를 표시하는 기능을 제공합니다.
- 쪽지함 기능  : 보낸 메시지 및 받은 메시지를 일괄확인 가능한 쪽지함 기능을 제공합니다.

## **📂 페이지 구성 상세**

![main.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\main.gif)

### main.html

- 이미지 글들을 잘 보여주기 위해 **카드 레이아웃**, **hover**활용
- 봉사자를 희망한 사람들에 **프로필**들을 띄워준다
- 각 페이지로 갈 수 있게 버튼

### Accounts App

![녹화_2022_12_12_15_35_47_325.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\sighup.gif)

**accounts/signup.html**

- 회원 가입 폼 작성 후, 가입하기 **버튼 클릭 시 회원가입 완료**
- 

![녹화_2022_12_12_15_37_13_296.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\login.gif)

**accounts/login.html**

- **로그인 폼과, signup.html로** 이동하는 버튼이 있다
- 

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\profile.png)

**accounts/detail.html**

- 로그인한 유저 **자신의 프로필**
  
  - 수정하기 버튼 출력 > 수정 폼
  - 팔로우/팔로잉 개수, 북마크 한 글 목록

- **다른 유저의 프로필**
  
  - 팔로우/언팔로우 버튼 구현
  
  - 쪽지함 구현
    
    ![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\profile_bookmark.png)
    
    ![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\profile_follow.png)

**채널톡 API**

- **채널톡 API를 사용하여 입양해듀오 챗봇 생성**

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\chat.png)

### Articles App

![녹화_2022_12_12_15_52_20_224.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\introduction.gif)

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\introdunction_link.png)

**articles/introduction.html**

**홈페이지 소개**

- **홈페이지 소개로 컨텐츠 길이가 긴 만큼 심심하지 않게 페이드업으로 애니메이션 추가**
- **마지막에는 링크를 통해 각 페이지로 이동할 수 있는 버튼**

![녹화_2022_12_12_15_55_30_417.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\information.gif)

![녹화_2022_12_12_15_55_36_34.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\information2.gif)

![녹화_2022_12_12_15_55_41_355.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\information3.gif)

**articles/information.html**

**반려동물을 위한 정보** 

- **해외이동봉사, 입양절차, 학대신고 등에 필요한 정보들을 모았다.**
- **url을 분리해 이동하게 하였고 hover 효과**

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\dog_index.gif)

![녹화_2022_12_12_16_03_16_563.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\dog_index.png)

**articles/dog_index.html**

**강아지 무료분양, 입양 페이지**

- **강아지 품종에 따라 카테고리 분류**

![녹화_2022_12_12_16_05_07_953.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\dog_detail.gif)

**articles/dog_detail.html**

**강아지 디테일**

- **디테일에서 위치정보와 작성자 팝업으로 프로필,메세지보내기 바로가기 구현**
- **즐겨찾기 기능과 댓글 구현**

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\create_form.png)

**articles/dog_create.html**

**강아지 작성 폼**

- **내 위치를 기반해 지도 생성**
- **카테고리 분류 폼**

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\cat_index.gif)

![녹화_2022_12_12_16_19_29_181.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\cat_index.png)

**articles/cat_index.html**

**고양이 무료분양, 입양 페이지**

- **고양이 품종에 따라 카테고리 분류**

![녹화_2022_12_12_16_20_13_521.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\cat_detail.gif)

**articles/cat_detail.html**

고양이 **디테일**

- **디테일에서 위치정보와 작성자 팝업으로 프로필,메세지보내기 바로가기 구현**
- **즐겨찾기 기능과 댓글 구현**

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\create_form.png)

**articles/cat_create.html**

고양이 **작성 폼**

- **내 위치를 기반해 지도 생성**
- **카테고리 분류 폼**

### Stories App

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\stories_index.png)

**stories/index.html**

 **스토리 인덱스 페이지**

- **반려동물 자랑 글, 입,분양 후기 등 자유게시판 형식**

![녹화_2022_12_12_16_27_52_959.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\stories_detail.gif)

**stories/detail.html**

 **스토리 디테일 페이지**

- **심플한 디테일, 댓글, 좋아요 구현**

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\stories_form.png)

**stories/create.html**

 **스토리 글 작성 폼**

- **간단한 글 작성과 이미지를 첨부해도되고 안해도 됨**

### Volrunteers App

![녹화_2022_12_12_16_31_38_758.gif](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\volunteer_index.gif)

**volunteers/index.html**

**봉사자 인덱스 페이지**

- **상단에는 봉사를 지원한 유저들의 프로필을 지나가게 함**

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\volunteer_form.png)

**volunteers/create.html**

**봉사자 글 작성 폼**

- **작성 폼에는 해외이동, 국내 봉사를 위한 출발지역, 도착지역과 이동날짜를 작성할 수 있다**

![](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\volunteers_detail.png)

**volunteers/detail.html**

- **봉사자 세부 정보가 노출**

- **수정, 삭제, 댓글 작성이 가능**

- **댓글 작성은 비동기 처리**

### Note App

![Untitled](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\mailbox.png)

**note/index.html**

**쪽지함 인덱스**

- **작성 폼에는 해외이동, 국내 봉사를 위한 출발지역, 도착지역과 이동날짜를 작성할 수 있다**

![](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\mail_send.png)

**note/create.html**

**쪽지함 글 작성 폼**

- **쪽지를 보낼 수 있는 폼**

![](C:\Users\이주현\Desktop\My%20Full%20Stack\pair%20project\Final%20project%203\assets\images\mail_detail.png)

**note/detail.html**

- **보낸/받은 메일의 디테일**

***

## 🎉후기

- `이주현`
  
  프로젝트를 진행하면서 실력부족으로 인해 벽에 부딪힐 때도 많았지만 팀원들의 캐리로 무사히 진행 할 수 있었습니다! 다들 잘하면서 실력을 숨기고 있었던 거였고 덕분에 많이 배울 수 있었어요 무엇보다 편안한 분위기에서 진행되어서 즐기듯이 프로젝트에 임할 수 있었어요 우리 팀원들 다들 고생했어~~

- `서민수`
  
  프론트를 지향해서 프론트 작업을 주로 했지만 하면서 느낀건 결국 백엔드의 실력도 어느정도 갖추어야한다고 뼈저리게 느꼈다.
  백에서 다룬 로직들을 html에서 보여주기 위한 로직처리도 중요했다.
  또 반응형 프론트를 구성하고 싶었지만 아직 실력이 부족하여 반응형을 구현하지 못하였지만 다른사람들의 디스플레이를 봤을 때 
  화면이 틀어지는 일이 많아서 반응형이 왜 필요한지, 반응형으로 왜 만들어야하는지를 깨달았다
   이번 프로젝트에서는 깃부터 시작해서 코드까지 정말 오류가 났을 때 도움이 필요할 때면 누구든 나서서 같이 고민해주고 해결해주는 팀원들 때문에 파이널프로젝트를 잘 마칠수 있었던 것 같다. 정말 좋은 사람들과 좋은 시간을 보낼 수 있었으며 이 계기로 좀 더 내 자신이 성장할 수 있었던것 같다.

- `이동희`
  
  프론트 담당이었지만, 개발에 있어서 프론트나 백 한 분야만 공부한다는 것은 어불성설임을 깨달았어요. 결국 세부적인 기능과 시스템을 이해하며 개발을 하기 위해서는 두 분야 모두 잘하는 풀스택 개발자가 되는게 베스트지만, 아직 그러한 개발자가 되기에는 한없이 부족함을 느낄 수 있었어요. 힘들었지만 이번 경험을 토대로 미래에 어떤 개발자가 되어야 할지에 대한 고찰을 할 수 있어서 뿌듯했어요. 커밋 푸시하면서 충돌이 많이 나서 애먹기도 했는데, 프로젝트를 진행할 때 커밋-푸시 메뉴얼이 조금 빈약했지 않나 싶어요. 원활한 협업을 위한 규칙, 메뉴얼도 굉장히 중요함을 깨달았어요. 밤늦게 머리 긁으면서 "이게 왜?" 하는 순간이 많았지만 지나고 보니 그 또한 저를 한단계 더 성장시켜준 기회였고, 즐거운 추억의 일부로 자리잡게 될 것 같아요! 4주간 우리 입양해듀오 팀원들 너무 고생 많으고 함께할 수 있어서 기뻤습니다! 실력과 인성 모두 겸비한 좋은 팀원들 만나서 즐거웠습니다!

- `현지수`
  
  프로젝트 첫 참여라 걱정을 많이 했는데 혼자서 헤맬 때마다 팀원분들이 많이 도와주셔서 무사히 마무리할 수 있었습니다. 프로젝트 기획부터 깃 활용까지 팀업 활동에 대한 실습을 처음 참여해본 과정이라 의미가 깊었고, 프론트를 꾸미면서 부트스트랩을 이렇게 많이 사용해 본 경험이 없었어서 이번 프로젝트를 통해 많이 배울 수 있었어요. 늘 새벽까지 모여서 작업하던 열정 넘치는 모습이 오래 기억에 남을 것 같습니다. 입양해듀오 팀원들 3주간 정말 감사했습니다! 고생 많으셨어요.

- `김교민`
  
  프로젝트를 진행하는 동안 각자 맡은 파트를 진행하면서 어려웠던 부분도 있었지만 서로서로 캐리해 주면서 동시에 부족한 부분을 배워가며 프로젝트를 완성시켰습니다! 그리고 처음 계획을 세웠을 때부터 좋은 분위기를 유지해서 재미있게 작업을 진행할 수 있었습니다. 우리 입양해듀오팀 모두 고생 많았고 부족한 걸 배울 수 있었던 좋은 계기가 되었읍니다!

- `이종은`
  
  좋은 팀원 분들과 프로젝트를 하여 해보지 않았던 여러 기능들을 도전해볼 수 있었고, 기능이 구현되는 것을 경험할 때 자신감이 생겨 또 다른 프로젝트를 해보고 싶은 마음이 들었습니다. 
  특히 지도나 공유하기 , 채널톡 기능을 구현할 때 API 사용법에 대해서 숙지할 수 있게 되었고, API를 다른 기능에도 이용해보고 싶다는 생각이 들었습니다. 
  또, 따뜻한 팀원 분들을 만나 서로 도와주며 협업의 필요성과 중요성을 알았고 감사했습니다.

- `이현성`
  
  다시 한번 프로젝트는 꼭 필요한 과정이라고 느꼈습니다.
  실무에서 많이 쓰는 github 협업도 경험해보고,
  모르는데 막연하게 알고 있다고 생각한 부분을 정확히 알 수 있었고,
  아는 것은 직접하며 다시 한 번 배우는 시간이었습니다.
  팀 내 분위기도 좋아서 즐겁게 배우는 시간이었습니다.
  정말 작은 것 조금 틀려서 몇 시간 고민 끝에 해결했을 때의 기분이 좋았지만
  아직 사소한 것 하나 모른다는 것에 화도 났습니다
  프로젝트는 내가 알고 있는 것이 무엇인지 정확하게 알게 해주고
  더 공부해야겠다는 생각을 하게 해주는 좋은 경험이었습니다.