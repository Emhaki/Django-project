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

## 🔎 구현한 기술

1. 404.html을 만들어서 찾을 수 없는 페이지를 보여주게끔 설계 (setting.py에서 DEBUG를 False로 변경)
