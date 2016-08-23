from status import Status
keywords = [""]

def parseAllStatuses(allStatuses):
  statusesWithFood = []
  for status in allStatuses:
    if statusDealsWithFood(status):
      statusesWithFood.append(status)
  return statusesWithFood  

def statusDealsWithFood(status):
  if("food" in status.message):
    return true
  return false

def filterByKeyword(allStatuses, keyword):
  return
