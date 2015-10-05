from status import Status

class Page:
  name = ""
  pageType = ""
  priority = ""
  page_id =  ""
  statusList = []

  def __init__(self, name, pageType, priority, page_id):
    self.name = name
    self.pageType = pageType
    self.priority = priority
    self.page_id = page_id

  def addStatus(self, status):
    self.statusList.append(status)

  def toString(self):
    print (self.name, self.pageType, self.priority, self.page_id)      

if __name__ == '__main__':
    newPage = Page()
