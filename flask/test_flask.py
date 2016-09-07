#using pytest
from pymongo import MongoClient
import urllib2
import json
import urllib

#setup
client = MongoClient('localhost', 27017)
db = client['free_food']


'''Tests basic connection to server. Should return Hello World text'''
def test_basic_connection_to_server():
	URL = "http://localhost"
	response = urllib2.urlopen(URL).read()
	assert response == "Hello World"


'''Tests basic connection with an addition of a form field'''
def test_basic_connection_with_form_field():
	URL = "http://localhost/testpost/"
	data = urllib.urlencode({"testParam": "testParam"})
	response = urllib2.urlopen(URL, data).read()
	assert response == 'testParam'


'''Tests creating existing user. Should not create user and database shouldnt be changed'''
def test_create_existing_user():
	global client, db
	allUsers = db.users.find()
	numUsersInit = allUsers.count()
	firstUser = db.users.find()[0]

	#try adding user with a number that already exists
	URL = "http://localhost/users/create/"
	testUsername = "testUserName"
	testEmail = "testEmail"
	testNumber = firstUser['number']
	data = urllib.urlencode({"username": testUsername, "email": testEmail, "number": testNumber})
	response = urllib2.urlopen(URL, data).read()

	#count new users amount- after (hopefully failing to) add new user to database
	client = MongoClient('localhost', 27017)
	db = client['free_food']
	updatedUsers = db.users.find()
	updatedUsersNum = updatedUsers.count()

	#remove new user that was created
	db.users.remove({"email":"testEmail"})
	assert updatedUsersNum == numUsersInit


'''Tests creating a new user. Should update database with new user. Deletes the test user afterwards'''
def test_create_new_user():
	global client, db
	users = db.users.find()
	numUsersInit = users.count()

	URL = "http://localhost/users/create/"
	testUsername = "testUserName"
	testEmail = "testEmail"
	testNumber = "testNumber"
	data = urllib.urlencode({"username": testUsername, "email": testEmail, "number": testNumber})
	response = urllib2.urlopen(URL, data).read()
	
	#count new users amount- after adding new user to database
	client = MongoClient('localhost', 27017)
	db = client['free_food']
	updatedUsers = db.users.find()
	updatedUsersNum = updatedUsers.count()

	#remove new user that was created
	db.users.remove({"email":"testEmail"})

	assert updatedUsersNum == numUsersInit + 1
	
