class User:

  # notifsFacebookPages = ['ALL', 'NONE']
  # notifsUserPosts = ['ALL', 'TOPRATED', 'NONE']

  defaultNotificationSettings = {
    'facebookPages' : 'ALL',
    'userPosts' : 'ALL'
  }


  def __init__(self, username = "", email = "", number = "", notificationSettings = defaultNotificationSettings):
    self.username = username
    self.email = email
    self.number = number
    self.notificationSettings = notificationSettings
    self.active = True

  def setName(self, status):
    self.statusList.append(status)

  def toString(self):
    print (self.username, self.email, self.number, self.notificationSettings, self.active)      

  def toJSON(self):
    return {"username":self.username, "email":self.email, "number":self.number, "notificationSettings":self.notificationSettings, "active":self.active}      

if __name__ == '__main__':
    pass


#gmail api key: AIzaSyAYcErn6w8Ji_EIg-xSrvGZPEk3KAxQrP8
#gmail oauth client id: 522584011010-bll62r88rgmug4um5re7s0qslsg5pmnr.apps.googleusercontent.com  
#gmail oauth client secret: G9raumBY8uj1AFyoOv2H0MFL