#this main method should be running continuously, checking if mail has any unread messages

from quickstart import *
import message_sender   


def getAllMessages():
    return    

#gets unread messages if they exist
def getUnreadMessages(all_messages):
    #gets all messages for gatechfreefood
    print all_messages, "==="
    unreadRaw = all_messages.list(userId='me', labelIds=["INBOX", "UNREAD"]).execute()
    unread = (unreadRaw['messages']) if (unreadRaw["resultSizeEstimate"] != 0) else []
    return unread

def getSender(rawMessages, message):
    return

def main():
    carrier = "ATT"
    ALLCARRIERS = ["ATT", "Sprint", "Verison", "TMobile", "Pinger"]
    # """Shows basic usage of the Gmail API.

    # Creates a Gmail API service object and outputs a list of label names
    # of the user's Gmail account.
    # """
    #setups database
    db = message_sender.setup()

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    rawMessages = service.users().messages()

    allMessages = getUnreadMessages(rawMessages)

    for message in allMessages:
        print ("message is: ", message)
        someM = rawMessages.get(userId='me', id=message['id']).execute()
        sender = someM['payload']['headers'][3]['value'].encode("utf8")
        encodedMessage = someM['snippet']
        # if exactly 10 or 11 digits, its a number. stringnum is num in string format 
        print ("SENDER: ", sender)
        stringNum = ""
        regexSearch = re.search('\D(\d{10})\D|\D(\d{11})\D', sender)
        if (regexSearch):
            stringNum = (regexSearch.string[regexSearch.start()+1:regexSearch.end()-1]) 
            textReceived = encodedMessage.lower()
            if (textReceived == "add me"):
                message_sender.createUser(db, "Aadil Omar", stringNum, carrier)
                print ("HE IS Subscribing")            
            elif (textReceived == "start"):
                message_sender.startSubscription(db, stringNum, carrier)
                print ("HE IS STARTING")
            elif (textReceived == "stop"):
                message_sender.Subscription(db, stringNum, carrier)            
                print ("HE IS STOPPING")
            else:
                print ("command not found")
            print (textReceived)


    #  **WORKS** marks all messages as read      
    # rawMessages.modify(userId='me', id=message['id'], body={"addLabelIds": [],"removeLabelIds": ["UNREAD"]}).execute()    

    # results = service.users().labels().list(userId='me').execute()
    # print (results)
    # labels = results.get('labels', [])

if __name__ == '__main__':
    main()