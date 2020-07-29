import praw
import time
import logging

# P O S T   I D 
# Post id to spam with comments
POST_ID = 'xxxxxx'


logging.basicConfig(level=logging.INFO)

credential_list = list()

class credentials():
    def __init__(self, CID, CS, UN, PW, POST_ID):
        credential_list.append(self)
        self.CID = CID
        self.CS  = CS
        self.UN  = UN
        self.PW  = PW
        self.PID = POST_ID
        
        self.reddit = praw.Reddit(client_id = self.CID,
                        client_secret = self.CS,
                        username = self.UN,
                        password = self.PW,
                        user_agent = 'penissegs')

        self.submission = self.reddit.submission(id=self.PID)
    
    def post(self, comment="."):
        try:
            self.submission.reply(comment)
            logging.info(f"commented as {self.UN}")
        except Exception:
            pass

# C R E D E N T I A L S
# add new credentials here

a = credentials(CID, CS, UN, PW, POST_ID)

try:
    while 1:
        time.sleep(5)
        for credential_object in credential_list:
            credential_object.post(".")
except KeyboardInterrupt:
    exit()
