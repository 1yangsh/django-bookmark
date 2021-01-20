### django 프로젝트 순서

> django를 이용한 북마크 웹사이트 만들기



#### 프로젝트 생성

> 프로젝트 및 앱 개발에 필요한 디렉토리와 파일 생성

- 프로젝트 생성

  - `django-admin startproject mybookmark`
  - 프로젝트 디렉토리로 이동
    
    - `cd mybookmark`
  - Visual Studio Code 실행
    
  - `code .`     # 현재 디렉토리에서 vsc 실행
    
  - 초기 테이블 생성

    - `python manage.py migrate`

      

- settings.py 설정

  - DATABASES

    ```python
    import os # 상단에 os모듈 import
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # 정확한 코드
    
    ```

  - TEMPLATES

    ```python
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    ```

  - Language / time_zome

    ```python
    LANGUAGE_CODE = 'ko-kr'
    
    TIME_ZONE = 'Asia/Seoul'
    ```

    

- admin 생성

  - `python manage.py createsuperuser`

    

- App 생성

  - `python manage.py startapp <앱이름>`

    

- settings.py 설정

  - INSTALLED_APPS

    ```python
    'bookmarkapp.apps.BookmarkappConfig', # 자신의 App 추가
    ```




---



#### 모델 생성

> 테이블 관련 내용 개발 (models.py, admin.py)

- 테이블 설계

  - models.py 

    ```python
    class Bookmark(models.Model):
        title = models.CharField(max_length=100, blank=True, null=True)
        url = models.URLField('url', unique=True)
    
        def __str__(self):
            return self.title
    ```

    

- admin 페이지에 반영할 테이블 등록

  - admin.py

    ```python
    from bookmarkapp.models import Bookmark
    class BookmarkAdmin(admin.ModelAdmin):
        list_display = ('title', 'url')
    
    
    admin.site.register(Bookmark, BookmarkAdmin)
    ```

    

- Database에 반영
  - 잡았던 모델을 형태대로 테이블 생성
  
    - `python manage.py makemigrations ` 
  
  - 실제 데이터베이스 반영
  
    - `python manage.py migrate`   
  
  - 테스트 서버에서 변경사항 확인
    - `python manage.py runserver 0.0.0.0:8000 `
      - 0.0.0.0 = 모든 사용자의 ip 허용 / 8000 = port 번호
      - 127.0.01 = 자신을 뜻하는 ip
    
    - 테이블 확인 방법
      - `python manage.py dbshell`  (db.sqlite3 이 있는 디렉토리에서)
      - `.table`   # 테이블 목록 보기
      - `PRAGMA table_info(bookmarkapp_bookmark)` # 테이블 정보 확인
    
    

---



#### URL conf 생성

> URL 및 뷰 매핑 관계를 정의 (urls.py)

- urls.py

  ```python
  from bookmarkapp.views import BookmarkLV, BookmarkDV
  
  path('bookmark/', BookmarkLV.as_view(), name='index'),
  path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),
  ```



#### View 생성

> 애플리케이션 로직 개발 (views.py)

- ListView와 DetailView를 상속받는 북마크 뷰 생성

  - views.py

    ```python
    from django.views.generic import ListView, DetailView # 뷰 상속
    from bookmarkapp.models import Bookmark  # 모델 클래스 import
    
    class BookmarkLV(ListView):
        model = Bookmark
    
    class BookmarkDV(DetailView):
        model = Bookmark
    ```



#### Template 생성

> 화면 UI 개발

- Template 생성
  - App 폴더에 `templates` 폴더 생성
  - templates 폴더에 `<app이름>`  폴더 생성
  - app이름 폴더 안에 `bookmark_list.html`  /  `bookmark_detail.html` 생성
    - django가 app이름 안에 있는 템플릿을 찾기 때문에
    - html 작성







