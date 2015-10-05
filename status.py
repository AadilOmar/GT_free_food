
class Status:
  message = "" 
  status_id = ""
  status_type = ""
  link = ""
  num_likes = 0
  num_comments = 0
  num_shares = 0

  def __init__(self, status_id, message, status_type, link, date_created, num_likes, num_comments, num_shares):
    self.status_id = status_id
    self.message = message
    self.status_type = status_type
    self.link = link
    self.date_created = date_created
    self.num_likes = num_likes
    self.num_comments = num_comments
    self.num_shares = num_shares

  def toString(self):
    print (self, self.status_id, self.message, self.status_type, self.link, self.date_created, self.num_likes, self.num_comments, self.num_shares)  

  def basicTostring(self):
    print (self.message, self.date_created)

if __name__ == '__main__':
    newPage = Status()