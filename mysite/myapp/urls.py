from django.urls import path

from . import views

urlpatterns = [
	path('',views.index),
	path('insert/',views.insert),
	path('insert/process',views.process),
	path('search/',views.search),
	path('search/search_result',views.search_result),
	path('listall/',views.listall),
	path('search_edit/',views.search_edit),
	path('search_edit/update',views.search_edit_content),
	path('search_edit/update_content',views.update_content),
	path('search_delete/',views.search_delete),
	path('search_delete/search_delete_content',views.search_delete_content),
	path('search_delete/delete_content',views.delete_content),
]