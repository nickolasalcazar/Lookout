from django.urls import path

urlpatterns = [
	path('', views.home, name='homepage'),
]