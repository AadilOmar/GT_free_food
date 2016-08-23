import urllib2
import json
import datetime
import csv
import time
from page import Page
from status import Status
import statusParser as Parser

allPages = []
statusLimit = 2
app_id = "708978925913200"
app_secret = "c3a5618b6f084fd41bcd593e2df95089" # DO NOT SHARE WITH ANYONE!
access_token = app_id + "|" + app_secret

def request_until_succeed(url):
    req = urllib2.Request(url)
    success = False
    while success is False:
        try: 
            response = urllib2.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception, e:
            print e
            time.sleep(5)
                
            print "Error for URL %s: %s" % (url, datetime.datetime.now())

    return response.read()


def getFacebookPageFeedData(page_id, access_token, num_statuses):
    
    # construct the URL string
    base = "https://graph.facebook.com"
    node = "/" + page_id + "/feed" 
    parameters = "/?fields=message,link,created_time,type,name,id,likes.limit(1).summary(true),comments.limit(1).summary(true),shares&limit=%s&access_token=%s" % (num_statuses, access_token) # changed
    url = base + node + parameters
    
    # retrieve data
    data = json.loads(request_until_succeed(url))
    return data
    

def createStatus(status):
    
    # The status is now a Python dictionary, so for top-level items,
    # we can simply call the key.
    
    # Additionally, some items may not always exist,
    # so must check for existence first
    
    status_id = status['id']
    status_message = '' if 'message' not in status.keys() else status['message'].encode('utf-8')
    # link_name = '' if 'name' not in status.keys() else status['name'].encode('utf-8')
    status_type = status['type']
    status_link = '' if 'link' not in status.keys() else status['link']
    print status['created_time']
    
    # Time needs special care since a) it's in UTC and
    # b) it's not easy to use in statistical programs.
    
    status_published = datetime.datetime.strptime(status['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
    status_published = status_published + datetime.timedelta(hours=-5) # EST
    status_published = status_published.strftime('%Y-%m-%d %H:%M:%S') # best time format for spreadsheet programs
    
    # Nested items require chaining dictionary keys.
    
    num_likes = 0 if 'likes' not in status.keys() else status['likes']['summary']['total_count']
    num_comments = 0 if 'comments' not in status.keys() else status['comments']['summary']['total_count']
    num_shares = 0 if 'shares' not in status.keys() else status['shares']['count']
    
    newStatus = Status(status_id, status_message, status_type, status_link, status_published, num_likes, num_comments, num_shares)
    return newStatus

def scrapeAllFbPages():


    num_processed = 0   # keep a count on how many we've processed

    for page in allPages:
        scrape_starttime = datetime.datetime.now()
        print page
        
        statuses = getFacebookPageFeedData(page.page_id, access_token, statusLimit)
        # print statuses
        print len(statuses)

        # data = status['data']

        print page
        newStatuses = []
        for status in statuses['data']:
            # print status
            newStatuses.append(createStatus(status))
            # print newStatus

        page.addStatuses(newStatuses)
        num_processed += 1     

    print "\nDone!\n%s Statuses Processed in %s" % (num_processed, datetime.datetime.now() - scrape_starttime)


def getAllStatuses():
    allStatuses = []
    for page in allPages:
        for status in page.statusList:
            print status
            allStatuses.append(status)
        # exit() 
    print "length of statuses", len(allStatuses)
    # print allStatuses
    return allStatuses            


def initPages():
    allPages.append(Page("Employer Relations at GT", "PAGE", "1", "1032976583394053"))
    allPages.append(Page("FreeFood at GT", "PAGE", "1", "296497732993"))
    allPages.append(Page("GT Class of 2017", "PAGE", "1", "539819086046638"))
    allPages.append(Page("GT Class of 2018", "PAGE", "1", "575425302530562"))
    allPages.append(Page("GT Class of 2019", "PAGE", "1", "761873287239333"))
    allPages.append(Page("GT Global Jackets", "PAGE", "1", "336123699816855"))
    allPages.append(Page("IEEE Innovation Team", "PAGE", "1", "140252826117138"))
    allPages.append(Page("GT Campus Services", "PAGE", "1", "582348801798914"))
    return allPages

if __name__ == '__main__':
  initPages()
  scrapeAllFbPages()

  allStatuses = getAllStatuses()

  # NewStatusList = []
  # for status in getAllStatuses():
  #   NewStatusList.append(status.toStringBasic())

  # # string = '\n'.join(NewStatusList)

  # # import sys
  # # sys.stdout = open('statuses.txt', 'w')
  # # print string

  # print NewStatusList

  # parseStatuses()  

# The CSV can be opened in all major statistical programs. Have fun! :)