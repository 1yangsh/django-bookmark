from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # /blog/
    path('', PostLV.as_view(), name='post_list'),

    # /blog/post
    path('post/', PostLV.as_view(), name='post_list'),

    # /blog/post/{slug}
    path('post/<str:slug>', PostDV.as_view(), name='post_detail'),

    # /blog/archive
    path('archive/', PostAV.as_view(), name='post_archive'),

    # /blog/2018
    path('<int:year>/', PostYAV.as_view(), name='post_year_archive'),

    # /blog/2018/nov
    path('<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'),

    # /blog/2018/nov/12
    path('post/<int:year>/<str:month>/<int:day>',
         PostDAV.as_view(), name='post_day_archive'),

    # /blog/today/
    path('today/', PostTAV.as_view(), name='post_today_archive'),
]
