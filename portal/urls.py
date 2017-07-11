from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^fill/$', views.fill, name="fill"),
]