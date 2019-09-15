from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from myapp import database


def index(request):
	str_html = "<title>Home Page</title>"
	str_html = str_html+"<p><a href = 'insert'> INSERT RECORD</a><p>"
	str_html = str_html + "<p><a href = 'search'>SEARCH RECORD</a></p>"
	str_html = str_html + "<p><a href = 'listall'>DISPLAY RECORD</a></p>"
	str_html = str_html + "<p><a href = 'search_edit'>UPDATE RECORD</a></p>"
	str_html = str_html + "<p><a href = 'search_delete'>DELETE RECORD</a></p>"

	return HttpResponse(str_html) 

def insert(request):
	return render(request,'myapp/insert.html')

def process(request):
	id = request.POST.get('txt_id')
	name = request.POST.get('txt_name')
	address = request.POST.get('txt_address')
	email = request.POST.get('txt_email')
	mobile = request.POST.get('txt_mobile')

	values = {
		'id':id,
		'name':name,
		'address':address,
		'email':email,
		'mobile':mobile
	}
	database.create_connection()
	database.insert_into_table(id,name,address,email,mobile)
	return render(request,'myapp/result.html',values)

def search(request):
	return render(request,'myapp/search.html')

def search_result(request):
	id = request.POST.get('txt_id')
	return render(request,'myapp/search_result.html',database.search(id))

def listall(request):

	#return render(request,'myapp/listall.html',database.listall())
	
	return HttpResponse(database.listall())

def search_edit(request):
	return render(request,'myapp/search_edit.html')

def search_edit_content(request):
	id = request.POST.get('txt_id')
	return render(request,'myapp/search_edit_content.html',database.search(id))

def update_content(request):
	id = request.POST.get('txt_id')
	name = request.POST.get('txt_name')
	address = request.POST.get('txt_address')
	email = request.POST.get('txt_email')
	mobile = request.POST.get('txt_mobile')

	values = {
		'id':id,
		'name':name,
		'address':address,
		'email':email,
		'mobile':mobile
	}
	database.update(id,name,address,email,mobile)
	return render (request,'myapp/update_result.html',values)

def search_delete(request):
	return render(request,'myapp/search_delete.html')

def search_delete_content(request):
	id = request.POST.get('txt_id')
	return render(request,'myapp/search_delete_content.html',database.search(id))

def delete_content(request):
	id = request.POST.get('txt_id')
	database.delete(id)
	return render(request,'myapp/deleted.html')
