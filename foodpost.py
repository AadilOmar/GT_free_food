import pytz
from datetime import datetime


class FoodPost:

  def set_time_stamp(self):
    atlTZ = pytz.timezone('America/New_York')
    atl_now = datetime.now(atlTZ)
    self.timestamp = str(atl_now)


  def __init__(self, creator, user_id, date, time, location, food, score):
    self.creator = creator
    self.user_id = user_id
    self.date = str(date)
    self.time = str(time)
    self.location = location
    self.food = food
    self.score = score
    self.set_time_stamp()


  def toString(self):
    print (self.creator, self.date, self.time, self.location, self.food, self.score, self.timestamp)      

  def toJSON(self):
    return {"creator":self.creator, "user:id":self.user_id, "date":self.date, "time":self.time, "location":self.location, "food":self.food, "score":self.score, "timestamp":self.timestamp}      

if __name__ == '__main__':
    pass