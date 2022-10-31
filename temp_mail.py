#-------------------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------------------
import requests, random, string, time
#-------------------------------------------------------------------------------
# Class
#-------------------------------------------------------------------------------
class TempMail:

    #Constructor
    def __init__(self):
        self.__api = "https://www.1secmail.com/api/v1/"
        self.__domain_list = ["1secmail.com", "1secmail.net", "1secmail.org"]
        self.__domain = random.choice(self.__domain_list)
        self.__current_email = []

    #Get random email
    def get_random_email(self):
        username = "".join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
        domain   = self.__domain
        email    = username+"@"+domain
        return [username, domain, email]

    #Set email
    def set_email(self, arr):
        self.__current_email = arr

    #Get current email
    def get_current_email(self):
        return self.__current_email

    #Check mailbox
    def check_mailbox(self):
        req = requests.get(f"{self.__api}?action=getMessages&login={self.__current_email[0]}&domain={self.__current_email[1]}").json()
        length = len(req)
        if length == 0:
            return [400, "Mailbox is empty."]
        else:
            idList = []
            for i in req:
                for k,v in i.items():
                    if k == "id":
                        idList.append(v)
            return [200, idList]

    #Get message from mailbox
    def get_mail_from_mailbox(self, mail_id):
        return requests.get(f"{self.__api}?action=readMessage&login={self.__current_email[0]}&domain={self.__current_email[1]}&id={mail_id}").json()
