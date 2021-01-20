### django 프로젝트 순서

> django를 이용한 북마크 웹사이트 만들기



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
    
    



