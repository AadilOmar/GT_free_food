from status import Status

class Page:
  name = ""
  pageType = ""
  priority = ""
  page_id =  ""

  def __init__(self, name, pageType, priority, page_id):
    self.name = name
    self.pageType = pageType
    self.priority = priority
    self.page_id = page_id
    self.statusList = []

  def addStatuses(self, statuses):
    for i in statuses:
      self.statusList.append(i)
    # print status

  def toString(self):
    print (self.name, self.pageType, self.priority, self.page_id)      
