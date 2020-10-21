from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^accounts/profile/(\d+)',views.profile,name = 'profile'),
    url('^accounts/create',views.create,name = 'create'),
    url('^accounts/search',views.search,name = 'search'),
    url('^accounts/updateProfile',views.updateProfile,name = 'updateProfile'),
    url('^accounts/single/(\d+)',views.single,name = 'single'),
    url('^like/(\d+)',views.likePost,name= 'likePost'),
	url('^follow/(\d+)',views.follow,name="user_follow"),
	url('^editPost/(\d+)',views.editPost,name="editPost"),
    url('^accounts/login', views.login, name='login'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)