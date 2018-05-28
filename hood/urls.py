from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^business/', views.business, name='business'),
    url(r'^post/', views.post, name='post'),
    url(r'^create/post', views.new_post, name="new-post"),
    url(r'^hood/', views.hood, name='hood'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^update/hood', views.update_hood, name="update_hood"),
]
