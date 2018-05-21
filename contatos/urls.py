from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('<int:contato_id>', views.get_contato_by_id)
]