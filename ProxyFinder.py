
import requests
import re

class ProxyFinder :
    def __init__(self):
        self.proxy_url = r"http://www.freeproxylists.com/load_fr_d1490410218.html"
        self.xpath = "//td"
        self.rxtr = "<tr>(.*?)</tr>"
        self.rxtd = "<td>(.*?)</td>"
        pass

    def find(self, xpath=None):
        proxy = []
        src = requests.get(self.proxy_url)
        content = self.unescape(src.content)
        matches = re.findall(self.rxtr, content)
        for m in matches :
            td = re.findall(self.rxtd, m)
            px = "%s:%s" %(td[0], td[1])
            proxy.append(px)
            #print(px)
        return proxy

    def unescape(self, s):
        s = s.replace("&lt;", "<")
        s = s.replace("&gt;", ">")
        # this has to be last:
        s = s.replace("&amp;", "&")
        return s