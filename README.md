# 9/29

# [Django] CRUD 📝

![](./video/2022-09-29%20CRUD%20%EC%97%B0%EC%8A%B5.gif)

## 🔎 구현한 기술

1. index, create, edit, detail, delete, new HTML 생성 후 urls과 맵핑.
2. 함수정의 방식으로 views.py에서 각 HTML에서 사용할 기능들을 구현
3. DB에 있는 pk 데이터를 통해 id값을 찾고, get을 통해서 데이터를 조작
4. delete의 경우 화면을 다시 보여줄 필요 없으니 redirect를 통해서 render의 과정을 줄임
5. base.html을 설정하여 다른 HTML에게 extends 함
