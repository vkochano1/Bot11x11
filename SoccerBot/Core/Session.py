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
        GlobalData.CurrentSession = self
        
        self.logger.info('Trying to login with UserID = %s, Password = %s' 
                         % (GlobalData.LoginUser, GlobalData.LoginPassword))
        
        GlobalData.CurrentSession.post(GlobalData.Site, data=logon)    

        if GlobalData.UserCfg == None:
            ID = self.findUserID()            
            GlobalData.UserCfg = UserConfig(GlobalData.LoginUser,ID)
            GlobalData.UserCfg.save()


        self.logger.info('Successfully logged in as %s(refID) ' % GlobalData.UserCfg.UserID )
        
        
    def findUserID(self):
        soup = GlobalData.CurrentSession.getContent(GlobalData.Site + '/index.php' )
        userID = soup.find("u", text = re.compile('ref='))
        extractedID = userID.text.split('=')[-1]     
        return extractedID
                
    def get(self, *args, **kwargs):
        kwargs['timeout'] = GlobalData.RequestTimeout
        return self.session.get(*args, **kwargs)

    def getContent(self, url, *args, **kwargs):
        response = self.get(url, *args, **kwargs)
        soup = BeautifulSoup(response.content, 'html5lib')
        return soup
        
    def post(self, *args, **kwargs):
        kwargs['timeout'] = GlobalData.RequestTimeout
        return self.session.post(*args, **kwargs)
