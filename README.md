# 9/29

# [Django] CRUD ๐

![](./video/2022-09-29%20CRUD%20%EC%97%B0%EC%8A%B5.gif)

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. index, create, edit, detail, delete, new HTML ์์ฑ ํ urls๊ณผ ๋งตํ.
2. ํจ์์ ์ ๋ฐฉ์์ผ๋ก views.py์์ ๊ฐ HTML์์ ์ฌ์ฉํ  ๊ธฐ๋ฅ๋ค์ ๊ตฌํ
3. DB์ ์๋ pk ๋ฐ์ดํฐ๋ฅผ ํตํด id๊ฐ์ ์ฐพ๊ณ , get์ ํตํด์ ๋ฐ์ดํฐ๋ฅผ ์กฐ์
4. delete์ ๊ฒฝ์ฐ ํ๋ฉด์ ๋ค์ ๋ณด์ฌ์ค ํ์ ์์ผ๋ redirect๋ฅผ ํตํด์ render์ ๊ณผ์ ์ ์ค์
5. base.html์ ์ค์ ํ์ฌ ๋ค๋ฅธ HTML์๊ฒ extends ํจ

# 10/1

![](./video/2022-10-01%20Design.gif)

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. bootstrap์ผ๋ก grid ์ค์ 
2. ์ฌ์ฉ์ id(pk)๊ฐ์ position:relative์ absolute๋ฅผ ํตํด ๋ช๋ฒ์งธ๋ก ์์ฑํ๋์ง ๊ตฌํ
3. ์ฌ์ฉ์ ํธ์์ฑ์ ์ํด box ์ ์ฒด๋ฅผ ๋งํฌํ๊ทธ๋ก ์ค์ 

## ๐จโ๐ป ๋ค์์ ๊ตฌํํด์ผ ํ๋ ๊ฒ

1. ์์ฑ ํ ์์ฑ์๋ฃ ํ์ด์ง๋ฅผ ์๋ณด์ฌ์ฃผ๊ณ  ๋ฐ๋ก redirect๋ฅผ ํตํด์ ์ฌ์ฉ์ ๋ฐฉ๋ช๋ก ํ์ด์ง๋ก ๋ณด์ด๊ฒ๋ ํ๊ธฐ
2. ์์ ๊ณผ ์ญ์  ๊ธฐ๋ฅ์ ๊ตฌํํ ๊น ๊ณ ๋ฏผ์ค
3. ๋ฉ์ธ ํ์ด์ง๋ฅผ ๊ตฌํํด์ผ ํจ
4. ๋ง์ฐ์ค hoverํจ๊ณผ ์ถ๊ฐ์ ๊ฐ ๊ธ๋ค์๊ฒ ๊ทธ๋ฆผ์ ํจ๊ณผ (ํฐ ํ๋๋ฆฌ๋ ์์จ๊น ๊ณ ๋ฏผ์ค)
5. ๊ธ์ด ์ผ์ ๊ธ ์ด์ ๋ง์์ง๋ฉด ํ์ด์ง ์ฒ๋ฆฌ
6. ๋ฉฐ์น ์ ์ ์ ์๋์ง ์๊ฐ ๋ณด์ฌ์ฃผ๊ธฐ (๊ตฌํ ๊ณ ๋ฏผ์ค, ๊ตฌํํ๋ค๋ฉด ์์ ๊ธฐ๋ฅ์ ์์ ์ผ ํ ์๋)

# 10/2

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. Static ํ์ผ์ ํ๋ ๋ง๋ค์ด์ Django์ CSS๋ฅผ ์ฐ๊ฒฐ / {% load static %} ์ ์ฌ์ฉํ๊ณ  Setting์์ ์ค์ ํด์ค์ผ CSS์ ์ฉ์ด ๋๋ค๋ ์ ์ ๊นจ๋ฌ์
2. creat.html์ placeholder์ ๋์์ธ์ ์ธ ์์๋ค ์ถ๊ฐ.
3. ๋ง์ฐ์ค ํธ๋ฒ์ ๊ธ๋ค์ด ์ปค์ง๊ฒ ๋ ํจ๊ณผ ์ฝ์

## ๐จโ๐ป ๋ค์์ ๊ตฌํํด์ผ ํ๋ ๊ฒ

1. placeholder์ focus์ ๊ธ์๊ฐ ์ฌ๋ผ์ง๊ฒ๋ ๊ตฌํ
2. ๊ธฐ๋ณธ์ ์ธ ๋์์ธ์ ์ธ ์์๋ค ์ถ๊ฐ

# 10/3

![](./video/2022-10-03.gif)

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. 404.html์ ๋ง๋ค์ด์ ์ฐพ์ ์ ์๋ ํ์ด์ง๋ฅผ ๋ณด์ฌ์ฃผ๊ฒ๋ ์ค๊ณ (setting.py์์ DEBUG๋ฅผ False๋ก ๋ณ๊ฒฝ) + ์์ง์ ๋๋ฒ๊ทธ๋ฅผ ํ์ธํ๊ธฐ ์ํด ๋ค์ True๋ก ๋ณ๊ฒฝ
2. ์๋๋ฐฉ์ด ๋์๊ฒ ๋ฐฉ๋ช๋ก์ ์์ฑํด์ฃผ๋ฉด ์ฝ์ธ์ด ์๊ธฐ๊ฒ๋ ๊ตฌํ Post.objects.all()์ ํ์ฉํด ์ ์ฅ๋ ๋ฐ์ดํฐ์ ๋ฐ๋ฅธ ์ฝ์ธ์ซ์
3. ๋์์ธ์ ์ธ ์์๋ค ์ถ๊ฐ (button ํธ๋ฒ, font์ฝ์ ๋ฑ)

## ๐จโ๐ป ๋ค์์ ๊ตฌํํด์ผ ํ๋ ๊ฒ

1. ํ์๊ฐ์, ๋ก๊ทธ์ธ ๊ธฐ๋ฅ ์ถ๊ฐ
2. ๋ก๊ทธ์ธ์ 00์ ๋ฐฉ๋ช๋ก์ผ๋ก ๋ณด์ด๊ฒ๋
3. mainํ์ด์ง ๊พธ๋ฏธ๊ธฐ
4. ๊ธ์ ์์ฑํ๋ฉด ์ฝ์ธ์ 2๊ฐ ์ฃผ๊ณ  ๋ฐฉ๋ช๋ก์ด ๋ฑ๋ก๋๋ฉด 1๊ฐ์ฉ ์ฃผ๋ ๊ฒ์ผ๋ก ๊ตฌํํด์ผ ํจ
5. ์์  ํ์ด์ง์์ ๊ตฌ์ํ  ์ ์๊ฒ ๋ html ๋ง๋ค๊ธฐ
6. ์์ฑ์๋ฃ ์๋ณด์ฌ์ฃผ๊ณ  ๋ฐ๋ก ๋ฐฉ๋ช๋ก์ผ๋ก ์ด๋์ํค๊ธฐ

# 10/4

![](./video/2022-10-04.gif)

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. store.html์ ๋ง๋ค๊ณ  a๋งํฌ url ์ค์ 
2. ๊ธฐ์กด DB๋ค์ ์ญ์ ํ๊ณ  ์์ฑ์๊ฐ์ ๊ธฐ๋กํ  ์ ์๋ DBํ์ด๋ธ์ ์์ฑํด์ objects.all()์ ํ์ฉํด ์์ฑ์๊ฐ์ ๋ณด์ฌ์ฃผ๊ฒ๋ ๊ตฌํ (๋ ์ง ๋ฐ์ดํฐ ui๊ฐ ๋ง์ ๋ค์ง ์์ ์์ ํ  ์์ )
3. DB ํ์ด๋ธ ์ถ๊ฐํ๋ ๊ณผ์ ์์ ์๊ฐ์ด ๊ฝค ๊ฑธ๋ ธ๋ค. ๊ฒฐ๊ตญ ํ์ด๋ธ์ ๋ค ์ญ์ ํ๊ณ  ์๋ก migrate ํ๋ค. DB์ค๊ณ๋ฅผ ์ ํด์ผํจ์ ๊นจ๋ฌ์๋ค.

## ๐จโ๐ป ๋ค์์ ๊ตฌํํด์ผ ํ๋ ๊ฒ

1. html๋จ์์ required๋ฅผ ์ญ์ ํ๋ฉด csrf ์ํ์ด ์์ผ๋ฏ๋ก ์๋ฒ๋จ์์๋ ๊ด๋ฆฌํ  ์ ์๋๋ก ์์ ํ๊ธฐ
2. datetime.now() ๋ฅผ ํ์ฉํ๊ฑฐ๋ ๋ฐ์ดํฐ ํ์ด๋ธ์ ์ ์ฅ๋ ๋ด์ฉ์ ํ์ฉํด ์ฌ์ฉ์ ์นํ์ ์ผ๋ก ๋ง๋ค๊ธฐ

# 10/5

## ๐ ๊ตฌํํ ๊ธฐ์ 

![](./video/2022-10-05.gif)

1. models.py์์ **from django.core.validators import MaxLengthValidator, MinLengthValidator** ์ค์ , ์ ๋ชฉ๊ณผ ๋ด์ฉ์ ์ ํจ์ฑ ๊ฒ์ฌ ํจ์ ์ถ๊ฐ
2. main ํ์ด์ง์ ํฌ๋ฆฌ์ค๋ง์ค ํธ๋ฆฌ ์ด๋ฏธ์ง ์ถ๊ฐ(๋ค๋ฅธ ์ด๋ฏธ์ง๋ก ๋์ฒด ์์ )
3. redirect๋ฅผ ์ด์ฉํด ์ฌ์ฉ์๊ฐ create.html์์ ๊ธ์ ์์ฑํ๋ฉด indexํ์ด์ง๋ก ์ด๋ํ๊ฒ๋ ์ค์ 
4. ๋ฉ์ธํ์ด์ง์์ ๋ฆฌ์คํธ ๋ฒํผ์ ๋๋ฅด๋ฉด ์์์ offcanvas ํจ๊ณผ ์ฝ์
5. offcanvas์์ ์์ธ ์ ๋ณด์ ๋ด์ฉ ์ฝ์

## ๐จโ๐ป ๋ค์์ ๊ตฌํํด์ผ ํ๋ ๊ฒ

1. ํธ๋ํฐ, ๋ธํธ๋ถ ๋ฑ ๋ค์ํ viewport์ ๋ง๋ ํ๋ก ํธ ๋ณด์ฌ์ฃผ๊ฒ๋ ์ค์ .
2. ์ต์์ ์ํฉ์ ๊ณ ๋ คํด์ ์ฝ๋๋ฅผ ์งค ๊ฒ.
3. base.html์ด ์กฐ๊ธ ๋จ์กฐ๋ก์ ๋ณด์ฌ์ ๊พธ๋ฏธ๊ธฐ
4. offcanvas์ ๋์์ธ ๊พธ๋ฏธ๊ธฐ

# 10/6

![](./video/2022-10-06.gif)
![](./video/2022-10-06-2.gif)

## ๐ ๊ตฌํํ ๊ธฐ์ 

https://docs.djangoproject.com/en/4.1/ref/templates/builtins/

1. admin ์ถ๊ฐ (python manage.py createsuperuser) admin.py์ from .models import Post๋ฅผ ์ถ๊ฐํ๊ณ  admin.site.register(Post)๋ฅผ ์ถ๊ฐ / ์ด๋๋ฏผ์์ ๊ฒ์๊ธ์ ํ์ธ ๋ฐ ์กฐ์ ๊ฐ๋ฅ
2. ์์ฑํ ๊ธ์ ์๊ฐ์ Django๊ณต์ ๋ฌธ์๋ฅผ ์ฐธ๊ณ ํด์ 2022-10-06 ๋ชฉ์์ผ 14:30 ๊ณผ ๊ฐ์ด ์กฐ๊ธ ๋ ์ฌ์ฉ์๊ฐ ๋ณด๊ธฐ ์ข๊ฒ ๋ ๊ตฌํ
3. ๊ฐ ๋งํฌ์ ๋ฒํผ์ ํด๋ฆญ ๋ฒ์ ํ๋(๋ฒํผ์ aํ๊ทธ๋ฅผ ๊ฑธ์๋๊ฒ ์๋๋ผ ๋ฒํผ์์ aํ๊ทธ๊ฐ ์์ด์ ํด๋ฆญ์ด ์ด๋ ค์ ์)
4. base.html์ ํฌ์คํ๊ฐฏ์๋ฅผ ์นด์ดํธํ๊ธฐ ์ํด ๊ฐ ํจ์์ ๋์ผํ ๋ก์ง ์ฝ์(ํ๋ฉด์ด ์ด๋ํด๋ ๋์ผํ๊ฒ ๋ณด์ด๊ฒ๋)

## ๐จโ๐ป ๋ค์์ ๊ตฌํํด์ผ ํ๋ ๊ฒ

1. ์ฌ์ฉ์์ ์ด๋ฆ์ด ์์์ ์ ์์นํ  ์ ์๋๋ก(์ง๊ธ์ ์ค์์ ๋ ฌ๋ ์ํ, div๊ฐ ๊ผฌ์ธ ๊ฒ ๊ฐ์)
2. detail ํ์ด์ง ๊พธ๋ฏธ๊ธฐ

# 10/7

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. date: date:"o-m-d D" ํ์์ผ๋ก ์์ฑ ์๊ฐ์ ๊ฐ์์ฑ ์๊ฒ ๊ตฌํ
2. timesince๋ฅผ ์ด์ฉํด์ ๋ช์๊ฐ ์ ์ ์์ฑํ๋์ง ๋ณด์ฌ์ค๊น ํ์ง๋ง, ์๋น์ค ์ทจ์ง์ ๋ง์ง ์๋ ๊ฒ ๊ฐ์์ ๊ตฌํํ๋ค๊ฐ ์ญ์ 
3. ์ธ๋ถ ๋ฌด๋ฃ ํฐํธ๋ฅผ ๋ค์ด๋ฐ์์ css ํ์ผ์ ํฐํธ ์ฝ์

## ๐จโ๐ป ๋ค์์ ๊ตฌํํด์ผ ํ๋ ๊ฒ

1. ๋ค์ํ view ํฌํธ์ ๋ฐ๋ฅธ ํ๋ฉด ๊ตฌํ์ ์๊ฐํด๋ณผ ๊ฒ
2. csrf ํ ํฐ ์ถ๊ฐํ๊ธฐ
3. if post์ get์ ํตํด์ ์๋ฒ์์๋ ์์ ์ฑ์๊ฒ ๊ตฌํํ๊ธฐ

# 10/8

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. creat.html์ csrf ํ ํฐ ์ถ๊ฐ.
2. views.py์์๋ if๋ฌธ์ ํตํด post์ get์ ์ฒ๋ฆฌํ๋๋ก ์ฝ๋์์ฑ
3. ๋์์ธ์ ์ธ ์์ ์ถ๊ฐ
4. ์นด๋ ๋ฉ์์ง๊ฐ ์ผ์  ๊ธธ์ด ์ด์ ๋ง์์ง๋ฉด ...์ผ๋ก ๋ณด์ด๊ฒ๋ truncatewords:50 ์ผ๋ก ์ค์ 
5. detail.html์์๋ ๋ด์ฉ ๊ธ์ด ๋ง์์ง๋ฉด ์ ํด์ง box๋ณด๋ค ๋์น์ง ์๊ฒ overflow: auto;๋ก ์ฒ๋ฆฌ

## ๐จโ๐ป ๋ค์์ ๊ตฌํํด์ผ ํ๋ ๊ฒ

1. ํ์๊ฐ์ ๊ธฐ๋ฅ
2. ๋ก๊ทธ์ธ ๊ธฐ๋ฅ
3. ๋ก๊ทธ์ธ์ ๋ฐ๋ฅธ ๋ฐ์ดํฐ๋ฒ ์ด์ค ์ฌ์ค์ 

# 10/9

## ๐ ๊ตฌํํ ๊ธฐ์ 

![](./video/2022-10-09.gif)

1. CSS ํ์ผ์ด ์๊พธ ์ค์๊ฐ ์ ์ฉ์ด ๋์ง ์์์ ๊ตฌ๊ธ๋งํด์ ์ฐพ์ ์ฝ๋ css๋งํฌ์ / href="{% static 'css/style.css' %}?{% now 'U'%}" ๋ด์ฉ์ ์ถ๊ฐ. {% now 'U'%}๋ฅผ ๋ฃ์ผ๋ฉด ํ์ผ ๋ก๋ ํ๋ผ๋ฏธํฐ๋ก ๋งค ์ด๋ง๋ค Unix Timestamp๋ฅผ ์๋์ ์ผ๋ก ์์ฑํ๋ค๊ณ  ํ๋ค. ๋ฐ๋ผ์ ํ์ผ ๋ก๋ ํ๊ทธ๋ฅผ ๋ถ์ฌ์ฃผ๋ฉด, ์ค์  ์น ์ฌ์ดํธ ์์์๋ ์์ฒด์ ์ผ๋ก ์์ฑํ ํ๋ผ๋ฏธํฐ๋ฅผ ์ฌ์ฉํด ํ์ผ์ ์ฐพ๊ฒ ๋๋ค.

2. ๋์์ธ์  ์์ : **box-shadow: 0px -4px 4px #74aa7b inset;** ๋ฅผ ์ถ๊ฐํด์ ๋ฒํผ์ ์์ฒด์  ์์๋ฅผ ์ถ๊ฐ. box์ color๋ณด๋ค box-shadow์ ์์ ์ด๋ก๊ฒ ํ๋ฉด ์์ฒด์ ์ธ ํจ๊ณผ๊ฐ ๋์จ๋ค.

3. ์์ ์์ ๊ตฌ๋งคํ๊ธฐ ๋ฒํผ ํด๋ฆญ์ ๋ชจ๋ฌ ์์ฑ, ๋ชจ๋ฌ์ id๊ฐ๊ณผ data-target์ ์ผ์น์์ผ์ ์ํ๋ ๋ด์ฉ์ ์ถ๋ ฅํ  ์ ์๊ฒ๋ ์ค๊ณ

## ๐จโ๐ป ๋ค์์ ๊ตฌํํด์ผ ํ๋ ๊ฒ

1. ์์ ์์ ๋ฌผํ์ ๊ตฌ๋งค์ ์ฝ์ธ์ด ์ค์ด๋ค๊ฒ๋ ๊ตฌํ
2. ๋ฌผํ์ ๊ตฌ๋งค์ ๊ตฌ๋งคํ ์ํ์ด ๋ฉ์ธ์ ๋ณด์ด๊ฒ๋ ๊ตฌํ
3. ๋ณด์ ํ ์ฝ์ธ์ด ๊ตฌ๋งค ๊ฐ๊ฒฉ๋ณด๋ค ๋ฎ์์ ๊ตฌ๋งค๋์ง ์๊ฒ๋ ๊ตฌํ

# 10/11

![](./video/2022-10-11.gif)

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. ์์ ์์ ๋ฌผ๊ฑด ๊ตฌ๋งค์ ์ฝ์ธ์ ์ฐจ๊ฐ์ํค๋ ๊ธฐ๋ฅ
2. ๊ตฌํ ๋ก์ง

```py
1. DB์ coin = 1์ธ ๋ฐ์ดํฐ ๊ฐ๋ค์ countํด์ ํ๋ฉด์ ๋ณด์ฌ์ค
2. ์์ ์์ ๋ฌผ๊ฑด์ ๊ตฌ๋งค(price)ํ ๊ฐ์ {% url 'posts:main'%}๋ก ์ ์ก.
3. views.py์ def main(request) ํจ์์์
if request.method == "POST" and request.POST.get("price") ๋ก์ง์ ๊ตฌ์ฑ.
4. Post.objects.order_by("coin").values()[0]์ c ๋ผ๋ ๋ณ์์ ํ ๋น
5. for k, v in c.items():
  if k == 'id':
    id_key = c[k]
๋ฅผ ํตํด์ id_key์ id๊ฐ์ ์ ์ฅ
6. post = Post.objects.get(id=id_key)๋ฅผ ํตํด ์ํ๋ ๋ฐ์ดํฐ ๊ฐ์ ๋ณ๊ฒฝ์ค๋น
7. post.coin = 2 ๋ฅผ ํตํด ๊ธฐ์กด์ coin = 1์ด์๋ DB๊ฐ์ 2๋ก ๋ณ๊ฒฝ
8. post.save()๋ฅผ ํตํด DB์ ์ฅ

๊ทธ๋ฆฌ๊ณ  coin = Post.objects.filter(coin=1).count()๋ก ์ค์ ํด์ ํ์ฌ ๊ฐ์ง๊ณ  ์๋ ์ฝ์ธ์ ์ถ๋ ฅ
```

## ๐จโ๐ป ๊ตฌํํ๋ฉด์ ์ด๋ ค์ ๋ ์ 

1. ๋จธ๋ฆฟ์์ผ๋ก๋ ๊ฐ๋จํ ๊ธฐ๋ฅ์ด๋ผ๊ณ  ์๊ฐํ๋๋ฐ ์ดํ์ด๋ผ๋ ์๊ฐ์ด ๊ฑธ๋ ธ๋ค. ์ฒ์์๋ DB๋ฅผ ๊ฑด๋๋ฆฌ์ง ์์ผ๋ฉด์ ๋ณ์ ์ ์ฅ์ ํตํด ๋ ๋๋ง์ ํ๋ ค๊ณ  ํ์ผ๋, ํ์ด์ง๋ฅผ ์๋ก๊ณ ์นจํ  ๋๋ง๋ค ์๋กญ๊ฒ ํจ์๊ฐ ์คํ๋๋ค๋ณด๋ ์ฝ์ธ์ ์ฐจ๊ฐํด๋ ๋ฆฌ์์ด ๋์๋ค.
2. ๋๋ฌธ์ DB๋ฅผ ๊ฑด๋๋ฆด ์ ๋ฐ์ ์๋ค๊ณ  ์๊ฐํ๊ณ , ORM querySet์ ํตํด์ ๋ณ๊ฒฝํ๊ธฐ ์ํ ๊ณผ์ ์ ๊ฑฐ์ณค๋ค.
3. ORM๊ณผ querySet ๊ฐ๋์ด ์ฝํ๋ค๋ณด๋, ์ํ์ฐฉ์ค๋ฅผ ๋ง์ด ๊ฒช์๊ณ , ๋์๋๋ฆฌ์ items๋ฅผ ํตํด์ ๋ณ๊ฒฝํ๊ณ ์ ํ๋ ๋ฐ์ดํฐ์ id๊ฐ์ ๋ณ์์ ์ ์ฅํ๋ค.
4. ์ง๊ธ ์๊ฐํด๋ณด๋ฉด ๋๊ฒ ๊ฐ๋จํ ๋ก์ง์ธ ๊ฒ ๊ฐ์๋ฐ, ๋ถ์กฑํ ์ ์ด ๋ง๋ค๋ณด๋ ์๊ฐ์ด ์ค๋๊ฑธ๋ ธ๋ ๊ฒ ๊ฐ๋ค.

# 10/12

![](./video/20221012.png)

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. ํ์๊ฐ์ ๊ธฐ๋ฅ์ ์ค๊ฐ์ ๋ฃ์ผ๋ ค๊ณ  ํ๋ค ๋ณด๋ ๊ธฐ์กด์ first_app์ ๋ด์ฉ๋ค์ด ๋ฐฉ๋ํด์ง๊ณ  ๊ด๋ฆฌํ๊ธฐ ์ด๋ ค์์ง ๊ฒ ๊ฐ์ ํ์๊ฐ์๊ณผ ์ ์ ๋ค์ ๊ด๋ฆฌํ  ์ ์๋ accounts app์ ์๋ก ์์ฑํ๊ณ  INSTALLD_APPS์ ์ฐ๊ฒฐ
2. my\_\_site๋จ์ urls.py์ accounts url์ includeํด์ฃผ๊ณ , accouts urls.py์ ์ฐ๊ฒฐ
3. ๊ธฐ์กด์ ์๋ DB๋ฅผ ์ญ์ ํ๊ณ  ์๋กญ๊ฒ migrate, accounts์ models.py๋ฅผ ์๋กญ๊ฒ ์์ฑํด์คฌ๊ธฐ ๋๋ฌธ์ ๊ธฐ์กด์ ์๋ ๋ฐ์ดํฐ๋ฅผ ์ญ์ ํ๊ณ  ์๋กญ๊ฒ migrationํจ
4. AbstractUser๋ฅผ ํตํด์ username, email, password ๋ฑ์ ๊ตฌํ / ์ ์ ๋ณ๋ก ๋ณด์ฌ์ง๋ ํ๋ฉด์ด ๋ฌ๋ผ์ผํ๊ธฐ ๋๋ฌธ์ ๊ธฐ์กด์ posts๋ก ์์ฑํ๋ ์ฑ๋ค์ accounts๋ก ์ฎ๊ฒจ์ผํ  ๊ฒ ๊ฐ์
5. ๊ทธ๋ ๋ค๋ฉด ์ ์ ๋ณ๋ก DB๋ฅผ ๋ค๋ฅด๊ฒ ์ค๊ณํด์ผํ๋..? ํ๋ ์๊ฐ๋ ๋ค์ด์ ๊ณต๋ถ ์์ 

# 10/13

![](./video/2022-10-13.png)

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. ๋ฐฐ๊ฒฝ์ ํฌ๋ฆฌ์ค๋ง์ค ๋์์ธ ์ถ๊ฐ. position: relative๋ฅผ ์ฃผ๊ณ  ๋ค๋ฅธ ๊ทธ ์์ ํ์ํ ์์๋ค์๊ฒ absolute๋ฅผ ๋ถ์ฌ.
2. ํ์ฌ๋ width๊ฐ์ ๊ณ ์ ์์ผ ๋จ์ง๋ง, ์ฌ์ฉ์์ viewํ๋ฉด์ ๋ฐ๋ผ ๋ฐ์ํ์ ๋ง๋ค์ด์ผ ํ  ๊ฒ ๊ฐ์
3. logout์ ํ์ ์ ๋ก๊ทธ์ธ ํ๋ฉด์ผ๋ก redirect์ค์ .
4. logout ์์๋ html๋จ์์ if๋ฌธ์ ํตํด ํ์๊ฐ์๊ณผ ๋ก๊ทธ์ธ ํญ๋ชฉ์ด ๋ณด์ด๊ฒ๋ ์ค์ 

# 10/15

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. @login_required๋ฅผ ์ฌ์ฉ

```py
from django.contrib.auth.decorators import login_required์ ํตํด detail, main, create, new, index, decorationํ์ด์ง๋ฅผ ๋ชจ๋ ๋ก๊ทธ์ธํ์ง ์์ผ๋ฉด ๋ชป๋ค์ด๊ฐ๊ฒ๋ ์ค์ 
```

2. html์์ ๋ก๊ทธ์ธํด์ผ ๋ณผ ์ ์๊ฒ๋ {% if request.user.is_authenticated %} {% endif %}๋ฅผ ์ฌ์ฉ.

3. accounts์ forms.py์์ CustomUserCreationForm์ ๋ง๋ค์ด์ UserCreationForm๋ฅผ ์์๋ฐ์. Django_bootstrap5๋ฅผ ์ด์ฉํด์signupํ์ด์ง์์ form์ผ๋ก ๋ ๋๋ง

# 10/17

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. ๋ฌผ๊ฑด ๊ตฌ๋งค์ html(name)๊ฐ์ ์๋ฒ์ ์ ๋ฌํด์ ์ฝ์ธ๊ฐฏ์๋งํผ ๋ฐ๋ณต๋ฌธ์ ์คํ, ORM์ ํตํด ์ฝ์ธ์ ์ค๋ฆ์ฐจ์์ผ๋ก ์ ๋ ฌํด์ ๊ฐ์ฅ ์์๊ฐ์ด ์๋ก ์ฌ๋ผ์ค๊ฒ ๋ง๋ค๊ณ , ์ฒซ๋ฒ์งธ ๊ฐ์ 2๋ก ๋ง๋ค์ด ์ค

```py
if request.method == "POST" and request.POST.get("price-3"):

  for _ in range(3):
      c = Post.objects.order_by("coin").values()[0]

      for k, v in c.items():
          if k == "id":
              id_key = c[k]
      post = Post.objects.get(id=id_key)
      post.coin = 2
      post.save()
```

2. Django์ ๋ด์ฅ๋์ด ์๋ messages ๋ฅผ ์ฌ์ฉ views.py์์๋ ๋ก์ง ์คํ์ messages.success(request, '๋ง์์ด ์ ๋ฌ๋์ด์!')์ด ์๋๋๊ฒ ๊ตฌํ, HTML์๋ {% if messages %}๋ฅผ ์ฌ์ฉํด์ messages๊ฐ ์์ผ๋ฉด ์๋ณด์ด๊ฒ, ์์ผ๋ฉด ๋ณด์ด๊ฒ๋ ๊ตฌํ

3. ๋ชจ๋ฐ์ผ ์์ฃผ๋ก ์๋น์ค๋ฅผ ์งํํ๊ธฐ ์ํด, min-width์ max-width๋ฅผ ์ค์ . min-width: 280px; max-width: 460px;๋ก ์ค์ ๊ฐ์ฅ์์ ํ๋ฉด์์๋ ๋ณด์ด๊ฒ๋ ์ค์ . ํฐ ํ๋ฉด์์๋ width๋ฅผ 460px๋ก ์ ํ

# 10/19

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. ๊ธฐ์กด์ model์ ์ฌ์ ์ํจ. Post ํด๋์ค์ user์ ForeignKey๋ฅผ ๋ฃ๊ณ , Comment ํด๋์ค์๋ ForeignKey๋ฅผ ์ถ๊ฐ. ๊ธฐ์กด์ Post.objects.all().count()๋ฅผ ํ์๋๋ฐ, ์ด๋ฌํ ๋ฐฉ์์ผ๋ก๋ ์ ์  ๊ฐ๊ฐ์ ๊ฒ์๋ฌผ์ ์นด์ดํธ ํ  ์ ์๋ค๋ ๊ฒ์ ๊นจ๋ฌ์. user id์ ๋ฐ๋ฅธ ํ๋ฉด๋ ๋๋ง๊ณผ ์นด์ดํธ๊ฐ ํ์ํจ์ ๊นจ๋ฌ์

```py
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField((""), auto_now_add=True)
    coin = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    coin = models.IntegerField(default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
```

2. ๊ตณ์ด new.html์์ ์์ฑ๋ด์ญ์ ๋ณด์ฌ์ค ํ์๊ฐ ์์ ๊ฒ ๊ฐ์์ ๊ณผ๊ฐํ๊ฒ ์ฝ๋๋ฅผ ์ญ์ . views.py์์๋ create -> new๋ก ๋์ด๊ฐ๋๋ฐ create๋ถ๋ถ์ ์ฝ๋๋ฅผ ๊ฐ์ํ ์ํด

3. ๋ชจ๋ธ์ ์ฌ์ค๊ณ ํด์ผ๋  ์๋ ์์ ๊ฒ ๊ฐ์. ์ํ๋ ์๋น์ค๋ ์ ์ ์๊ฒ ํฌ์คํ์ ์์ฑํ๋ ๊ฒ์ด๊ธฐ ๋๋ฌธ์ user.id๋ฅผ ์ค์ฌ์ผ๋ก posting์ด ๋์ด์ผ ํจ. ์ต์ํ์ง ์์ ๊ฐ๋๋ค์ด๋ค ๋ณด๋ ๊ณต๋ถ ํ์.

# 10/25

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. ์๋น์ค์ ๋ง๋ ๋ชจ๋ธ์ ์ฌ์ ์ํ๋๋ฐ ์์ด์ ์ด๋ ค์์ ๊ฒช๊ณ ์์. User๋ฅผ ์ค์ฌ์ผ๋ก title, content๋ฅผ ์๊ณ  ์ถ์ด์ User ํด๋์ค์์ ๋ชจ๋ธ์ ์ ์ํด์ผ๋๋์ง ์์๋ด์ผ ํ  ๊ฒ ๊ฐ์
2. ๋ชจ๋ธ์ ์ฌ์ ์ํ๋ฉด์ DB ๋ค๋ฃจ๋๋ฐ ์ต์ํด์ง๊ณ  ์๊ณ , People => Comment๋ฅผ 1:N์ผ๋ก ๊ตฌํํ๋ ค๊ณ  ํ์ผ๋, ๊ทธ๋ ๊ฒ ๊ตฌํํ๋ฉด ๋ฐ์ดํฐ ์ ์ฌํ๊ธฐ ์ง์ ๋ถํ  ๊ฒ ๊ฐ์

# 10/29

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. ์๋น์ค ์ด์์ค์ธ ๋กค๋งํ์ดํผ ์ ๋ด๊ฐ ๋ง๋๋ ค๋ ์๋น์ค์ ๊ตฌ์กฐ๊ฐ ๋น์ทํ๋ค๊ณ  ์๊ฐ๋์ด, ๋กค๋งํ์ดํผ์ url ๊ตฌ์กฐ์ ์ฝ๋๋ฅผ ๋ถ์ํด๋ณด๊ธฐ ์์

2. https://rollingpaper.site/ ์์ ๋กค๋งํ์ดํผ๋ฅผ ์์ํ๋ ค๋ฉด ๋ก๊ทธ์ธ์ ํ์์ ์ผ๋ก ํด์ผํจ. ๋ก๊ทธ์ธ์ ํ๊ณ  ๋กค๋งํ์ดํผ ๋ง๋ค๊ธฐ๋ฅผ ํด๋ฆญํ๋ฉด https://rollingpaper.site/create๋ก ์ด๋

3. ์ ๋ชฉ์๋ ฅํ๊ณ  ํ๋ง ์ค์ ํ ํ ๋กค๋งํ์ดํผ๋ฅผ ๋ง๋ค๋ฉด https://rollingpaper.site/rolls/939520 ์ ๊ฐ์ด ๋กค๋งํ์ดํผ๊ฐ ๋ง๋ค์ด์ง. ๋ค์ ์๋ ์ซ์๋ ๋กค๋งํ์ดํผ์ id๊ฐ์ผ๋ก ์ถ์ 

4. https://rollingpaper.site/rolls/939520 ๋ก ๋ค์ด์ค๋ฉด ํ์๊ฐ์์ด๋ ๋ก๊ทธ์ธ ํ ์ ์ ๊ฐ ์๋๋๋ผ๋ ๋๊ตฌ๋ผ๋ ๊ธ์ ์ธ ์ ์์.

5. ๊ธ์์ฑ ๋ฒํผ์ ๋๋ฅด๋ฉด https://rollingpaper.site/rolls/939520/editor ๋ก ์ด๋. ํด๋น ๋กค๋งํ์ดํผ id๊ฐ์ ๋ฐ๋ผ ์์ฑ๋๋ ๊ฒ ๊ฐ์.
![](./video/%EB%A1%A4%EB%A7%81%ED%8E%98%EC%9D%B4%ED%8D%BC.png)

## ๐จโ๐ป ์์ผ๋ก์ ๋ฐฉํฅ

1. ์ฒ์์ intro ํ์ด์ง์์ ๋ง๋ค๊ธฐ ๋ฒํผ์ ๋๋ฅด๊ฒ๋ ์ค์ (๋ก๊ทธ์ธ ๋์ด์๋์ง ์๋์ง์ ๋ฐ๋ผ ๋ถ๋ฅ)
2. ๋ก๊ทธ์ธ์ด ๋๋ค๋ฉด create ํ์ด์ง๋ก ์ด๋(+ nickname ์ค์ ) -> ๋ง๋ค๊ธฐ๋ฅผ ๋๋ฅด๋ฉด <int:tree_pk>๋ก ์ค์  -> ํด๋น url๋ก ์ฌ๋๋ค์๊ฒ ๊ณต์ ํ๊ฒ๋ ์ค์ 
3. ํด๋นํ์ด์ง์์ ๊ธ ์์ฑ์ ๋๋ฅด๋ฉด <int:tree_pk>/post ํ์ด์ง๋ก ์ด๋, ํด๋น tree.pk๊ฐ์ ๋ฐ๋ผ ์์ฑ๋๋๋ก ์ค์ 

# 11/03

## ๐ ๊ตฌํํ ๊ธฐ์ 

1. ์๋ก์ด model ์ค์ ๊ณผ url ์ค์ ์ ์ฌ์ ๋น, ํธ๋ฆฌ pk๋ฅผ ์ค์ฌ์ผ๋ก ๋ฐ์ดํฐ๋ฅผ ์ ์ฌํ  ์๊ฐ.
2. ์ฌ๋ฌ๊ฐ์ง ๋ง์ ธ๋ณด๊ณ  url๋ ์ฌ์ ๋น ํด๋ดค์ง๋ง, ์ ์ฅ๋ ๋ฐ์ดํฐ๊ฐ user pk์ tree pk๊ฐ ๊ฐ์
![](./video/20221103.png)
3. ํ์ฌ ๋ค๋ฅธ ํ๋ก์ ํธ๋ก ์๊ฐ์  ์ฌ์ ๊ฐ ์์ง๋ง, ๋ค๋ฅธ ํ๋ก์ ํธ์์ ๋ฐฐ์ด ๋ด์ฉ์ ํ ๋๋ก ๊ฐ์ธ ํ๋ก์ ํธ์ ์ ์ฉํด๋ณผ ์๊ฐ