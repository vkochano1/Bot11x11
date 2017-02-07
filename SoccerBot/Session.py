import requests
from Config import *
from bs4 import BeautifulSoup
import re
import logging
import LoggerConfig

class GameSession(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def initSession(self):

        
        logon = {
                'step' : '1',
                'login' : '1',
                 'userresl' : '1366x768',
                'useragent' : 'Mozilla 5.0',
                'useragent' : 'Mozilla 5.0',
                'auth_name': GlobalData.LoginUser,
                'auth_pass': GlobalData.LoginPassword,
                'auth_pass1': '',
                'userdate' : '12',
                'usertime' :  '62609'
            }
        #self-register 
        self.session = requests.Session()
        GlobalData.CurrentSession = self.session
        
        self.logger.info('Trying to login with UserID = %s, Password = %s' 
                         % (GlobalData.LoginUser, GlobalData.LoginPassword))
        
        GlobalData.CurrentSession.post(GlobalData.Site, data=logon)    
    
        GlobalData.UserID = self.findUserID()
        
        self.logger.info('Successfully logged in as %s(refID) ' % GlobalData.UserID )
        
    def findUserID(self):
        response = GlobalData.CurrentSession.get(GlobalData.Site + '/index.php' )
        soup = BeautifulSoup(response.content, 'html.parser')
        userID = soup.find("u", text = re.compile('ref='))
        extractedID = userID.text.split('=')[-1]
        return extractedID
                
    def get(self, *args, **kwargs):
        kwargs['timeout'] = 15
        self.session.get(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        kwargs['timeout'] = 15
        self.session.get(*args, **kwargs)
