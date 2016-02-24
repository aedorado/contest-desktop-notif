import urllib2
import time

class URL:

    def __init__(self, url):
        self.url = url

    def fetch(self):
        OK = False
        tries = 0
        while not OK:
            try:
                response = urllib2.urlopen(self.url)
                OK = True
            except urllib2.HTTPError as e:
                tries = tries + 1
                if tries >= 256:
                    return -1
        return response
