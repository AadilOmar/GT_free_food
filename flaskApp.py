from flask import Flask, Response, jsonify, request
from pymongo import MongoClient
from bson import BSON, json_util
import json
from foodpost import FoodPost
from user import User


app = Flask(__name__)


client = MongoClient('localhost', 27017)
db = client['free_food']


#testing route- indent not doing anything atm
@app.route('/accounts/show/')
def show_accounts():

	allUsers = db.users.find()
 	userList = []
 	for user in allUsers:
 		userList.append(user)
	return json.dumps(userList, sort_keys=True, indent=4, separators=(',', ': '), default=json_util.default)

#create account with name, phonenumber, and email
@app.route('/accounts/create/', methods=['POST'])
def create_account():
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

#creates post
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
	

@app.route('/posts/update')
def update_post():
	pass

@app.route('/posts/show')
def show_posts():
	pass


@app.route('/posts/rate')
def rate_post():
	pass




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')