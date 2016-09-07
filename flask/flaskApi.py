from flask import Flask, Response, jsonify, request
from pymongo import MongoClient
from bson import BSON, json_util
import json
from foodpost import FoodPost
from user import User
import helpers as Helper

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client['free_food']

'''Dummy simple route'''
@app.route('/')
def index():
	return "Hello World"

'''Dummy simple route with form parameter'''
@app.route('/testpost/', methods=['POST'])
def testpost():
	testParam = request.form['testParam']
	return testParam


'''Testing route- indent not doing anything atm'''
@app.route('/users/show/')
def show_users():
	users = db.users.find()
 	allUsers = [user for user in users]
 	# return str(allUsers)
 	# return Helper.pretty_print_objects(userList)	
	return json.dumps(allUsers, sort_keys=True, indent=4, separators=(',', ': '), default=json_util.default)

'''Creates user with username, number, and email'''
@app.route('/users/create/', methods=['POST'])
def create_user():
	#update database and create user with name and phone number
 	users = db.users
	username = request.form['username']
	email = request.form['email']
	number = request.form['number']
 	duplicateNumber = users.find({"number": number}).count()
	if not duplicateNumber:
		newUser = User(username, email, number)
		users.insert(newUser.toJSON())
		return "user created"
	else:
		return "user with that number already exists"

'''Creates post and inserts into the db'''
@app.route('/posts/create/', methods=['POST'])
def create_post():
	posts = db.posts
	#username of creator
	creator = request.form['creator']
	user_id = request.form['user_id']
	date = request.form['date']
	time = request.form['time']
	location = request.form['location']
	food = request.form['food']
	score = request.form['score']
	foodpost = FoodPost(creator, user_id, date, time, location, food, score)
	posts.insert(foodpost.toJSON(), {"unique": True})
	return "post created"
	

@app.route('/posts/update/')
def update_post():
	pass

'''Returns all posts'''
@app.route('/posts/show/')
def show_posts():
	posts = db.posts.find()
	allPosts = [post for post in posts]
	return str(allPosts)
	# return Helper.pretty_print_objects(allPosts)
	# return json.dumps(allPosts, sort_keys=True, indent=4, separators=(',', ': '), default=json_util.default)


@app.route('/posts/rate')
def rate_post():
	pass




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')