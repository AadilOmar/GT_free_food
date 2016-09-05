
import smtplib
#gmailAccount.oy has username and password
import gmailAccount
import pymongo
from pymongo import MongoClient

def setup():
  client = MongoClient()
  # to use specific host + port-> client = MongoClient('localhost', 27017)
  db = client.free_food
  return db

def createUser(db, name, number, carrier):
  users = db.users
  thing = users.find({"number": number})
  if thing.count() == 0:
    users.insert({"name": name, "number": number, "carrier": carrier, "subscribed": True}, {"unique": True})
    print "user created"
  else:
    print "user with that number already exists" 

def startSubscription(db, number, carrier):
  print "STARTING!!!!"
  users = db.users
  users.update({"number": number, "carrier": carrier}, {"$set": {"subscribed": True}})
  #send text to person 

def endSubscription(db, number, carrier):
  users = db.users
  users.update({"number": number, "carrier": carrier}, {"$set": {"subscribed": False}})
  #send text to person 

def sendMessage(message):
  #send message to all users who are subscribed
  server = smtplib.SMTP( "smtp.gmail.com", 587 )
  server.starttls()
  server.login( username, password )

  db = setup()
  users = db.users
  usersToSend = users.find({"subscribed": True})
  print usersToSend.count()
  #for each user, send them the message based on their carrier
  for user in usersToSend:
    print "asfd"
    if(user['carrier'] == "ATT"): mmsnumber = "@mms.att.net"
    elif(user['carrier'] == "TMobile"): mmsnumber = "@tmomail.net"
    elif(user['carrier'] == "Sprint"): mmsnumber = "@page.nextel.com"
    elif(user['carrier'] == "Verison"): mmsnumber = "@vtext.com"
    else:
      print "failuyer"
    print user["number"]
    server.sendmail( 'gt_free_food',  user["number"] + mmsnumber, message)

# sendMessage("message to send")

# db = setup()
# createUser(db, "Aadil Omar", "6786025306", "ATT")

# db = setup()
# createUser(db, "BBCAadil Omar", "6786025306")