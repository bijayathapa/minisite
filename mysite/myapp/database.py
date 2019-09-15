import pymysql

from pymysql import Error

from django.shortcuts import render

from django.http import HttpResponse

DB_FILE = "testdb"

def create_connection():
	try:
		conn = pymysql.connect("localhost","root","",DB_FILE)
		print("connection successful")
	except Error as e:
		print(e)
	finally:
		conn.close()

def insert_into_table(id,name,address,email,mobile):
	sql_insert_query = """INSERT INTO tbl_person(person_id, person_name, person_address ,person_email, person_mobile)
	VALUES (%s,%s,%s,%s,%s)"""

	insert_values = (id,name,address,email,mobile)

	try:
		conn = pymysql.connect("localhost","root","",DB_FILE)
		cur = conn.cursor()
		cur.execute(sql_insert_query,insert_values)
		conn.commit()
		conn.close()
		print("Inserted")
	except Error as e:
		print(e)

def search(id):
	sql_search_query = """SELECT * FROM tbl_person WHERE person_id = %s """
	data = (id)
	try:
		conn = pymysql.connect("localhost","root","",DB_FILE)
		cur = conn.cursor()
		cur.execute(sql_search_query,data)
		result = cur.fetchone()
		print("searched")
	except Error as e:
		print(e)
	if result == None:
		context={
		'id':-1,
		'name':"",
		'address':"",
		'email':"",
		'mobile':""
	}
	else:
		context={
			'id':result[0],
			'name':result[1],
			'address':result[2],
			'email':result[3],
			'mobile':result[4]
		}	
	return context

def listall():
	sql_listall_query ="""SELECT * FROM tbl_person"""
	str_html ="<table border = 1><tr><td>ID</td><td>Name</td><td>Address</td><td>Email</td><td>Mobile</td></tr>"
	try:
		conn = pymysql.connect("localhost","root","",DB_FILE)
		cur = conn.cursor()
		cur.execute(sql_listall_query)
		result = cur.fetchall()
	except Error as e:
		print(e)
	for row in result:
		context = {
			'id':row[0],
			'name':row[1],
			'address':row[2],
			'email':row[3],
			'mobile':row[4]
		}
		str_html = str_html+"<tr><td>"+str(row[0])+"</td><td>"+str(row[1])+"</td><td>"+str(row[2])+"</td><td>"+str(row[3])+"</td><td>"+str(row[4])+"</td>"
	str_html = str_html+"</tr></table>"

	return str_html

def update(id,name,address,email,mobile):
	sql_update_query = """UPDATE tbl_person SET person_name = %s,person_address = %s,person_email = %s,person_mobile =%s 
	WHERE person_id = %s"""

	update_values = (name,address,email,mobile,id)
	try:
		conn = pymysql.connect("localhost","root","",DB_FILE)
		cur = conn.cursor()
		cur.execute(sql_update_query,update_values)
		conn.commit()
		conn.close()
		print("Updated")
	except Error as e:
		print(e)

def delete(id):
	sql_delete_query = """DELETE FROM tbl_person WHERE person_id = %s"""
	data = (id)
	try:
		conn = pymysql.connect("localhost","root","",DB_FILE)
		cur = conn.cursor()
		cur.execute(sql_delete_query,data)
		conn.commit()
		conn.close()
		print("Deleted")
	except Error as e:
		print(e)

