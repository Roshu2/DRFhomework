# ๐DRFhomework
<a href="https://www.python.org" target="_blank" rel="noreferrer"> 
   <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 
</a> 
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> 
   <img src="https://images.velog.io/images/holawan/post/a6998da8-f1f8-4256-94cc-fcb77b2f08b7/django.png" alt="django" width="40" height="40"/> 
</a> 

## ๐1์ผ์ฐจ ๊ณผ์   
๊ณผ์ 
 1. args, kwargs๋ฅผ ์ฌ์ฉํ๋ ์์  ์ฝ๋ ์ง๋ณด๊ธฐ
 2. mutable๊ณผ immutable์ ์ด๋ค ํน์ฑ์ด ์๊ณ , ์ด๋ค ์๋ฃํ์ด ์ด๋์ ํด๋นํ๋์ง ์์ ํ๊ธฐ
 3. DB Field์์ ์ฌ์ฉ๋๋ Key ์ข๋ฅ์ ํน์ง ์์ ํ๊ธฐ
 4. django์์ queryset๊ณผ object๋ ์ด๋ป๊ฒ ๋ค๋ฅธ์ง ์์ ํ๊ธฐ    
<br>
์ ์ถ ํ์ผ<br>
drf1.py
<br><br>

## ๐2์ผ์ฐจ ๊ณผ์   
๊ณผ์ <br>

1. Django ํ๋ก์ ํธ๋ฅผ ์์ฑํ๊ณ , user ๋ผ๋ ์ฑ์ ๋ง๋ค์ด์ settings.py ์ ๋ฑ๋กํด๋ณด์ธ์.
2. user/models.py์ `Custom user model`์ ์์ฑํ ํ django์์ user table์ ์์ฑ ํ ๋ชจ๋ธ๋ก ์ฌ์ฉํ  ์ ์๋๋ก ์ค์ ํด์ฃผ์ธ์
3. user/models.py์ ์ฌ์ฉ์์ ์์ธ ์ ๋ณด๋ฅผ ์ ์ฅํ  ์ ์๋ `UserProfile` ์ด๋ผ๋ ๋ชจ๋ธ์ ์์ฑํด์ฃผ์ธ์
4. blog๋ผ๋ ์ฑ์ ๋ง๋  ํ settings.py์ ๋ฑ๋กํด์ฃผ์ธ์
5. blog/models.py์ <์นดํ๊ณ ๋ฆฌ ์ด๋ฆ, ์ค๋ช>์ด ๋ค์ด๊ฐ ์ ์๋ `Category`๋ผ๋ ๋ชจ๋ธ์ ๋ง๋ค์ด๋ณด์ธ์.
6. blog/models.py์ <๊ธ ์์ฑ์, ๊ธ ์ ๋ชฉ, ์นดํ๊ณ ๋ฆฌ, ๊ธ ๋ด์ฉ>์ด ๋ค์ด๊ฐ ์ ์๋ `Article` ์ด๋ผ๋ ๋ชจ๋ธ์ ๋ง๋ค์ด๋ณด์ธ์.(์นดํ๊ณ ๋ฆฌ๋ 2๊ฐ ์ด์ ์ ํํ  ์ ์์ด์ผ ํด์)
7. Article ๋ชจ๋ธ์์ ์ธ๋ ํค๋ฅผ ํ์ฉํด์ ์์ฑ์์ ์นดํ๊ณ ๋ฆฌ์ ๊ด๊ณ๋ฅผ ๋งบ์ด์ฃผ์ธ์
8. admin.py์ ๋ง๋ค์๋ ๋ชจ๋ธ๋ค์ ์ถ๊ฐํด ์ฌ์ฉ์์ ๊ฒ์๊ธ์ ์์ ๋กญ๊ฒ ์์ฑ, ์์  ํ  ์ ์๋๋ก ์ค์ ํด์ฃผ์ธ์
9. CBV ๊ธฐ๋ฐ์ผ๋ก ๋ก๊ทธ์ธ / ๋ก๊ทธ์์ ๊ธฐ๋ฅ์ ๊ตฌํํด์ฃผ์ธ์
10. CBV ๊ธฐ๋ฐ์ผ๋ก ๋ก๊ทธ์ธ ํ ์ฌ์ฉ์์ ๊ฒ์๊ธ์ ์ ๋ชฉ์ ๋ฆฌํดํด์ฃผ๋ ๊ธฐ๋ฅ์ ๊ตฌํํด์ฃผ์ธ์
<br><br>

## ๐3์ผ์ฐจ ๊ณผ์   
๊ณผ์ <br>

1. blog ์ฑ์ <๊ฒ์๊ธ, ์ฌ์ฉ์, ๋ด์ฉ>์ด ํฌํจ๋ comment ํ์ด๋ธ์ ์์ฑํด์ฃผ์ธ์
2. ์ธ๋ ํค๋ฅผ ์ฌ์ฉํด์ Article, User ํ์ด๋ธ๊ณผ ๊ด๊ณ๋ฅผ ๋งบ์ด์ฃผ์ธ์
3. admin.py์ comment๋ฅผ ์ถ๊ฐํด ์์ ๋กญ๊ฒ ์์ฑ, ์์  ํ  ์ ์๋๋ก ํด์ฃผ์ธ์
4. serializer๋ฅผ ํ์ฉํด ๋ก๊ทธ์ธ ํ ์ฌ์ฉ์์ ๊ธฐ๋ณธ ์ ๋ณด์ ์์ธ ์ ๋ณด๋ฅผ ๋ฆฌํดํด ์ฃผ๋ ๊ธฐ๋ฅ์ ๋ง๋ค์ด์ฃผ์ธ์
5. 4๋ฒ์ serializer์ ์ถ๊ฐ๋ก ๋ก๊ทธ์ธ ํ ์ฌ์ฉ์์ ๊ฒ์๊ธ, ๋๊ธ์ ๋ฆฌํดํด์ฃผ๋ ๊ธฐ๋ฅ์ ๊ตฌํํด์ฃผ์ธ์
6. blog ์ฑ์ title / category / contents๋ฅผ ์๋ ฅ๋ฐ์์ ๊ฒ์๊ธ์ ์์ฑํ๋ ๊ธฐ๋ฅ์ ๊ตฌํํด์ฃผ์ธ์
 - ๋ง์ฝ title์ด 5์ ์ดํ๋ผ๋ฉด ๊ฒ์๊ธ์ ์์ฑํ  ์ ์๋ค๊ณ  ๋ฆฌํดํด์ฃผ์ธ์
 - ๋ง์ฝ contents๊ฐ 20์ ์ดํ๋ผ๋ฉด ๊ฒ์๊ธ์ ์์ฑํ  ์ ์๋ค๊ณ  ๋ฆฌํดํด์ฃผ์ธ์
 - ๋ง์ฝ ์นดํ๊ณ ๋ฆฌ๊ฐ ์ง์ ๋์ง ์์๋ค๋ฉด ์นดํ๊ณ ๋ฆฌ๋ฅผ ์ง์ ํด์ผ ํ๋ค๊ณ  ๋ฆฌํดํด์ฃผ์ธ์

7. custom permission class๋ฅผ ํ์ฉํด ๊ฐ์ ํ 3์ผ ์ด์ ์ง๋ ์ฌ์ฉ์๋ง ๊ฒ์๊ธ์ ์ธ ์ ์๋๋ก ํด์ฃผ์ธ์
 - ํ์คํธ ํ  ๋์๋ ๊ฐ์ ํ 3๋ถ ์ด์ ์ง๋ ์ฌ์ฉ์๊ฐ ๊ฒ์๊ธ์ ์ธ ์ ์๊ฒ ํด์ฃผ์ธ์
 - join_date๋ datetime field๋ก ๋ง๋ค์ด์ฃผ์ธ์
<br><br>

## ๐4์ผ์ฐจ ๊ณผ์   
๊ณผ์ <br>

1. admin ํ์ด์ง์ user admin์ ๋ฑ๋กํ๊ณ , userprofile ํ์ด๋ธ์ user admin ํ์ด์ง์์ ๊ฐ์ด ๋ณด๊ณ  ์ค์  ํ  ์ ์๋๋ก ํด์ฃผ์ธ์
2. article ํ์ด๋ธ์ <๋ธ์ถ ์์ ์ผ์, ๋ธ์ถ ์ข๋ฃ ์ผ์>๋ฅผ ์ถ๊ฐํด์ฃผ์ธ์
3. article view์ ๊ฒ์๊ธ ์กฐํ ๊ธฐ๋ฅ์ ๋ง๋ค๋, ํ์ฌ ์ผ์๋ฅผ ๊ธฐ์ค์ผ๋ก ๋ธ์ถ ์์ ์ผ์์ ๋ธ์ถ ์ข๋ฃ ์ผ์ ์ฌ์ด์ ์๋ ํญ๋ชฉ๋ค๋ง ๋ฆฌํดํด์ฃผ๋๋ก ํํฐ๋ฅผ ์ค์ ํด์ฃผ์ธ์
 - ๋ฆฌํด ๋ฐ์ดํฐ๋ ๊ฒ์๊ธ ์์ฑ์ผ ๊ธฐ์ค์ผ๋ก ์ ๋ ฌํ์ฌ ์ต๊ทผ ์ด ๊ธ์ด ๊ฐ์ฅ ๋จผ์  ์ฌ๋ผ์ค๋๋ก ํด์ฃผ์ธ์
4. ๊ธฐ์กด article ์์ฑ ๊ธฐ๋ฅ์ ์ ์งํ๋, article์ admin user ํน์ ๊ฐ์ ํ 7์ผ์ด ์ง๋ ์ฌ์ฉ์๋ง ์์ฑ ๊ฐ๋ฅํ๋๋ก ํด์ฃผ์ธ์
 - ์กฐํ๋ ๋ก๊ทธ์ธ ํ ์ฌ์ฉ์์ ๋ํด์๋ง ๊ฐ๋ฅํ๋๋ก ์ค์ ํด์ฃผ์ธ์
<br><br>

## ๐งพ5์ผ์ฐจ ๊ณผ์   
๊ณผ์ <br>  

1. product๋ผ๋ ์ฑ์ ์๋ก ์์ฑํด์ฃผ์ธ์
2. product ์ฑ์์ <์์ฑ์, ์ ๋ชฉ, ์ธ๋ค์ผ, ์ค๋ช, ๋ฑ๋ก์ผ์, ๋ธ์ถ ์์ ์ผ, ๋ธ์ถ ์ข๋ฃ์ผ>๊ฐ ํฌํจ๋ product ํ์ด๋ธ์ ์์ฑํด์ฃผ์ธ์

3. django serializer์์ ๊ธฐ๋ณธ์ ์ผ๋ก ์ ๊ณตํ๋ validate / create / update ๊ธฐ๋ฅ์ ์ฌ์ฉํด event ํ์ด๋ธ์ ์์ฑ/์์  ๊ธฐ๋ฅ์ ๊ตฌํํด์ฃผ์ธ์
   * postman์ผ๋ก ํ์ผ์ ์๋ก๋ ํ  ๋๋ raw ๋์  form-data๋ฅผ ์ฌ์ฉํ๊ณ , Key type์ File๋ก ์ค์ ํด์ฃผ์ธ์

4. ๋ฑ๋ก๋ ์ด๋ฒคํธ ์ค ํ์ฌ ์๊ฐ์ด ๋ธ์ถ ์์ ์ผ๊ณผ ๋ธ์ถ ์ข๋ฃ ์ผ์ ์ฌ์ด์ ์๊ฑฐ๋, ๋ก๊ทธ์ธ ํ ์ฌ์ฉ์๊ฐ ์์ฑํ product ์ฟผ๋ฆฌ์์ ์ง๋ ฌํ ํด์ ๋ฆฌํดํด์ฃผ๋ serializer๋ฅผ ๋ง๋ค์ด์ฃผ์ธ์

5. product field๋ฅผ admin์์ ๊ด๋ฆฌํ  ์ ์๋๋ก ๋ฑ๋กํด์ฃผ์ธ์  
<br><br>  

## ๐ข6์ผ์ฐจ ๊ณผ์   
๊ณผ์ <br>  

1. product ์ฑ์ product ํ์ด๋ธ ๊ตฌ์ฑ์ <์์ฑ์, ์ธ๋ค์ผ, ์ํ ์ค๋ช, ๋ฑ๋ก์ผ์, ๋ธ์ถ ์ข๋ฃ ์ผ์, ๊ฐ๊ฒฉ, ์์  ์ผ์, ํ์ฑํ ์ฌ๋ถ>๋ก ๋ณ๊ฒฝํด์ฃผ์ธ์
2. django serializer๋ฅผ ์ฌ์ฉํด validate / create / update ํ๋ ๊ธฐ๋ฅ์ ๊ตฌํํด์ฃผ์ธ์
    1. custom validation ๊ธฐ๋ฅ์ ์ฌ์ฉํด ๋ธ์ถ ์ข๋ฃ ์ผ์๊ฐ ํ์ฌ๋ณด๋ค ๋ ์ด์  ์์ ์ด๋ผ๋ฉด ์ํ์ ๋ฑ๋กํ  ์ ์๋๋ก ํด์ฃผ์ธ์
    2. custom creator ๊ธฐ๋ฅ์ ์ฌ์ฉํด ์ํ ์ค๋ช์ ๋ง์ง๋ง์ "<๋ฑ๋ก ์ผ์>์ ๋ฑ๋ก๋ ์ํ์๋๋ค." ๋ผ๋ ๋ฌธ๊ตฌ๋ฅผ ์ถ๊ฐํด์ฃผ์ธ์
    3. custom update ๊ธฐ๋ฅ์ ์ฌ์ฉํด ์ํ์ด update ๋์ ๋ ์ํ ์ค๋ช์ ๊ฐ์ฅ ์ฒซ์ค์ "<์์  ์ผ์>์ ์์ ๋์์ต๋๋ค." ๋ผ๋ ๋ฌธ๊ตฌ๋ฅผ ์ถ๊ฐํด์ฃผ์ธ์
3. product ์ฑ์์ <์์ฑ์, ์ํ, ๋ด์ฉ, ํ์ , ์์ฑ์ผ>์ ๋ด๊ณ  ์๋ review ํ์ด๋ธ์ ๋ง๋ค์ด์ฃผ์ธ์
4. review ํ์ด๋ธ์ ๊ด๋ฆฌ์ ํ์ด์ง์์ ์์ ๋กญ๊ฒ ์ถ๊ฐ/์์  ํ  ์ ์๋๋ก ์ค์ ํด์ฃผ์ธ์
5. ํ์ฌ ๋ ์ง๋ฅผ ๊ธฐ์ค์ผ๋ก, ๋ธ์ถ ์ข๋ฃ ๋ ์ง๊ฐ ์ง๋์ง ์์๊ณ  ํ์ฑํ ์ฌ๋ถ๊ฐ True์ด๊ฑฐ๋ ๋ก๊ทธ์ธ ํ ์ฌ์ฉ์๊ฐ ๋ฑ๋ก ํ ์ํ๋ค์ ์ ๋ณด๋ฅผ serializer๋ฅผ ์ฌ์ฉํด ๋ฆฌํดํด์ฃผ์ธ์
6. 5๋ฒ ์ํ ์ ๋ณด๋ฅผ ๋ฆฌํด ํ  ๋ ์ํ์ ๋ฌ๋ฆฐ review์ ํ๊ท  ์ ์๋ฅผ ํจ๊ป ๋ฆฌํดํด์ฃผ์ธ์
    1. ํ๊ท  ์ ์๋ (๋ฆฌ๋ทฐ ํ์ ์ ํฉ/๋ฆฌ๋ทฐ ๊ฐฏ์)๋ก ๊ตฌํด์ฃผ์ธ์
    2. ์์ฑ ๋ ๋ฆฌ๋ทฐ๋ ๋ชจ๋ returnํ๋ ๊ฒ์ด ์๋, ๊ฐ์ฅ ์ต๊ทผ ๋ฆฌ๋ทฐ 1๊ฐ๋ง ๋ฆฌํดํด์ฃผ์ธ์
7. ๋ก๊ทธ์ธ ํ์ง ์์ ์ฌ์ฉ์๋ ์ํ ์กฐํ๋ง ๊ฐ๋ฅํ๊ณ , ํ์๊ฐ์ ์ดํ 3์ผ ์ด์ ์ง๋ ์ฌ์ฉ์๋ง ์ํ์ ๋ฑ๋ก ํ  ์ ์๋๋ก ๊ถํ์ ์ค์ ํด์ฃผ์ธ์
<br><br>


