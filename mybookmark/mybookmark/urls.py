from django.contrib import admin
from django.urls import path

from bookmarkapp.views import BookmarkLV, BookmarkDV

urlpatterns = [
    # http://127.0.0.1:8000/admin
    path('admin/', admin.site.urls),

    # http://127.0.0.1:8000/bookmark
    path('bookmark/', BookmarkLV.as_view(), name='index'),
    # http://127.0.0.1:8000/bookmark/?
    path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),
]
