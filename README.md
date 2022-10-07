# 9/29

# [Django] CRUD 📝

![](./video/2022-09-29%20CRUD%20%EC%97%B0%EC%8A%B5.gif)

## 🔎 구현한 기술

1. index, create, edit, detail, delete, new HTML 생성 후 urls과 맵핑.
2. 함수정의 방식으로 views.py에서 각 HTML에서 사용할 기능들을 구현
3. DB에 있는 pk 데이터를 통해 id값을 찾고, get을 통해서 데이터를 조작
4. delete의 경우 화면을 다시 보여줄 필요 없으니 redirect를 통해서 render의 과정을 줄임
5. base.html을 설정하여 다른 HTML에게 extends 함

# 10/1

![](./video/2022-10-01%20Design.gif)

## 🔎 구현한 기술

1. bootstrap으로 grid 설정
2. 사용자 id(pk)값을 position:relative와 absolute를 통해 몇번째로 작성했는지 구현
3. 사용자 편의성을 위해 box 전체를 링크태그로 설정

## 👨‍💻 다음에 구현해야 하는 것

1. 작성 후 작성완료 페이지를 안보여주고 바로 redirect를 통해서 사용자 방명록 페이지로 보이게끔 하기
2. 수정과 삭제 기능을 구현할까 고민중
3. 메인 페이지를 구현해야 함
4. 마우스 hover효과 추가와 각 글들에게 그림자 효과 (큰 테두리는 없앨까 고민중)
5. 글이 일정글 이상 많아지면 페이지 처리
6. 며칠전에 적었는지 시간 보여주기 (구현 고민중, 구현한다면 수정기능을 없애야 할수도)

# 10/2

## 🔎 구현한 기술

1. Static 파일을 하나 만들어서 Django와 CSS를 연결 / {% load static %} 을 사용하고 Setting에서 설정해줘야 CSS적용이 된다는 점을 깨달음
2. creat.html에 placeholder와 디자인적인 요소들 추가.
3. 마우스 호버시 글들이 커지게 끔 효과 삽입

## 👨‍💻 다음에 구현해야 하는 것

1. placeholder에 focus시 글자가 사라지게끔 구현
2. 기본적인 디자인적인 요소들 추가

# 10/3

![](./video/2022-10-03.gif)

## 🔎 구현한 기술

1. 404.html을 만들어서 찾을 수 없는 페이지를 보여주게끔 설계 (setting.py에서 DEBUG를 False로 변경) + 아직은 디버그를 확인하기 위해 다시 True로 변경
2. 상대방이 나에게 방명록을 작성해주면 코인이 생기게끔 구현 Post.objects.all()을 활용해 저장된 데이터에 따른 코인숫자
3. 디자인적인 요소들 추가 (button 호버, font삽입 등)

## 👨‍💻 다음에 구현해야 하는 것

1. 회원가입, 로그인 기능 추가
2. 로그인시 00의 방명록으로 보이게끔
3. main페이지 꾸미기
4. 글을 작성하면 코인을 2개 주고 방명록이 등록되면 1개씩 주는 것으로 구현해야 함
5. 상점 페이지에서 구입할 수 있게 끔 html 만들기
6. 작성완료 안보여주고 바로 방명록으로 이동시키기

# 10/4

![](./video/2022-10-04.gif)

## 🔎 구현한 기술

1. store.html을 만들고 a링크 url 설정
2. 기존 DB들을 삭제하고 생성시간을 기록할 수 있는 DB테이블을 생성해서 objects.all()을 활용해 작성시간을 보여주게끔 구현 (날짜 데이터 ui가 맘에 들지 않아 수정할 예정)
3. DB 테이블 추가하는 과정에서 시간이 꽤 걸렸다. 결국 테이블을 다 삭제하고 새로 migrate 했다. DB설계를 잘 해야함을 깨달았다.

## 👨‍💻 다음에 구현해야 하는 것

1. html단에서 required를 삭제하면 csrf 위험이 있으므로 서버단에서도 관리할 수 있도록 수정하기
2. datetime.now() 를 활용하거나 데이터 테이블에 저장된 내용을 활용해 사용자 친화적으로 만들기

# 10/5

## 🔎 구현한 기술

![](./video/2022-10-05.gif)

1. models.py에서 **from django.core.validators import MaxLengthValidator, MinLengthValidator** 설정, 제목과 내용에 유효성 검사 함수 추가
2. main 페이지에 크리스마스 트리 이미지 추가(다른 이미지로 대체 예정)
3. redirect를 이용해 사용자가 create.html에서 글을 작성하면 index페이지로 이동하게끔 설정
4. 메인페이지에서 리스트 버튼을 누르면 옆에서 offcanvas 효과 삽입
5. offcanvas에서 상세 정보와 내용 삽입

## 👨‍💻 다음에 구현해야 하는 것

1. 핸드폰, 노트북 등 다양한 viewport에 맞는 프론트 보여주게끔 설정.
2. 최악의 상황을 고려해서 코드를 짤 것.
3. base.html이 조금 단조로워 보여서 꾸미기
4. offcanvas의 디자인 꾸미기

# 10/6

![](./video/2022-10-06.gif)
![](./video/2022-10-06-2.gif)

## 🔎 구현한 기술

https://docs.djangoproject.com/en/4.1/ref/templates/builtins/

1. admin 추가 (python manage.py createsuperuser) admin.py에 from .models import Post를 추가하고 admin.site.register(Post)를 추가 / 어드민에서 게시글을 확인 및 조작 가능
2. 작성한 글의 시간을 Django공식 문서를 참고해서 2022-10-06 목요일 14:30 과 같이 조금 더 사용자가 보기 좋게 끔 구현
3. 각 링크와 버튼의 클릭 범위 확대(버튼에 a태그를 걸었던게 아니라 버튼안에 a태그가 있어서 클릭이 어려웠음)
4. base.html에 포스팅갯수를 카운트하기 위해 각 함수에 동일한 로직 삽입(화면이 이동해도 동일하게 보이게끔)

## 👨‍💻 다음에 구현해야 하는 것

1. 사용자의 이름이 시작점에 위치할 수 있도록(지금은 중앙정렬된 상태, div가 꼬인 것 같음)
2. detail 페이지 꾸미기
