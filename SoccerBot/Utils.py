from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__ (self):
        HTMLParser.__init__(self)
        self.out = ''
    
    def handle_starttag(self, tag, attrs):
        if tag in ['table','tr','td', 'html','body', 'tbody','a']:
            href =''
            for  t, v in attrs:
                if t == 'href':
                    href = 'href=' + v
                                 
            self.out = self.out + '<%s %s>'% (tag, href)

    def handle_endtag(self, tag):
        if tag  in ['table','tr','td', 'html','body', 'tbody','a']: 
            self.out = self.out + '</%s>'% tag
        
    def handle_data(self, data):
        self.out = self.out + data
