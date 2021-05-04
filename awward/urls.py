from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns =[
    path('',views.index,name = 'index'),
    path('new/upload', views.upload_project, name='upload'),
    path('new/profile', views.add_profile, name='edit'),
    path('myprofile',views.my_profile,name ='myprofile'),
    path('oneproject/<id>', views.one_project, name='oneproject'),
    path('search/', views.search_project, name='search'),
    path('comment/(proj_id)/', views.add_comment, name='comment'),
    path('view_comment/(\d+)/', views.comment, name='view'),
    path('api/profile/', views.ProfileList.as_view(), name='profile'),
    path('api/project/', views.ProjectList.as_view(), name='project'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
















